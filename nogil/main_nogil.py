from ferma_fact_nogil import fermat_factorization_nogil
import timeit

TEST_LST = [101, 9973, 104729, 101909, 609133, 1300039, 9999991, 99999959, 99999971, 3000009, 700000133,
                6133539541640392674]

if __name__ == '__main__':
    time_res = timeit.repeat(
        "list(map(fermat_factorization_nogil, TEST_LST))",
        globals=globals(),
        number=10,
        repeat=1
    )
    print("NoGIL Time:", time_res)