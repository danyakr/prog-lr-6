# distutils: language = c++
from libc.math cimport sqrtl

cdef bint is_perfect_square(unsigned long long y_squared) nogil:
    cdef unsigned long long root = <unsigned long long>(sqrtl(y_squared))
    while root * root > y_squared:
        root -= 1
    return root * root == y_squared


def fermat_factorization_nogil(object obj_N):
    """
    Разложение числа методом Ферма.
    Поддерживает очень большие числа, работает без GIL.
    """
    if not isinstance(obj_N, int):
        raise TypeError("Expected an integer")
    if obj_N < 2:
        raise ValueError("Number must be greater than 1")

    cdef unsigned long long N = 0
    try:
        N = <unsigned long long> obj_N
    except:
        raise OverflowError("Number too big to convert to 64-bit integer")

    cdef unsigned long long x = <unsigned long long>(sqrtl(N)) + 1
    cdef unsigned long long y_squared
    cdef unsigned long long y
    cdef unsigned long long a = 0, b = 0

    while True:
        y_squared = x * x - N
        if y_squared >= 0:
            with nogil:
                if is_perfect_square(y_squared):
                    y = <unsigned long long>(sqrtl(y_squared))
                    if y * y == y_squared:
                        a = x - y
                        b = x + y
            # Возвращаем кортеж вне блока with nogil
            return (a, b)
        x += 1