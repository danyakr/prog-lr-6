import math

def fermat_factorization_cy(N):
    if N % 2 == 0:
        return (2, N // 2)

    x = math.isqrt(N) + 1

    while True:
        y_squared = x * x - N
        if y_squared >= 0:
            y = math.isqrt(y_squared)
            if y * y == y_squared:
                return (x - y, x + y)
        x += 1