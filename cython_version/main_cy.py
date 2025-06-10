import timeit
from ferma_fact_cy import fermat_factorization_cy

TEST_LST = [101, 9973, 104729, 101909, 609133, 1300039, 9999991, 99999959, 99999971, 3000009, 700000133, 61335395416403926747]

if __name__ == '__main__':
    time_res = timeit.repeat(
        "res = [fermat_factorization_cy(i) for i in TEST_LST]",
        globals=globals(),
        number=10,
        repeat=1
    )
    print("Cython Time:", time_res)