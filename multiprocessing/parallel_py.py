from concurrent.futures import ProcessPoolExecutor
from baseline.ferma_fact import fermat_factorization
import timeit

def parallel_factorization(numbers, workers=4):
    with ProcessPoolExecutor(max_workers=workers) as executor:
        return list(executor.map(fermat_factorization, numbers))

if __name__ == '__main__':
    TEST_LST = [
        101,
        9973,
        104729,
        101909,
        609133,
        1300039,
        9999991,
        99999959,
        99999971,
        3000009,
        700000133,
        61335395416403926747,
    ]

    # Замеряем время выполнения
    duration = timeit.timeit(
        "parallel_factorization(TEST_LST, workers=4)",
        globals=globals(),
        number=1  # Количество повторов
    )

    print(f"Время выполнения: {duration:.4f} секунд")

    # Выводим результаты
    result = parallel_factorization(TEST_LST, workers=4)
    print("Результаты факторизации:")
    print(result)