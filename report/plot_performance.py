import matplotlib.pyplot as plt

times = {
    'Baseline': 446.53,
    'Cython': 194.78,
    'Cython (Parallel)': 9.8,
    'Cython (NoGIL with threads)': 0.00296,
    'Python (Parallel)': 22.1
}

plt.figure(figsize=(10, 6))
plt.bar(times.keys(), times.values())
plt.ylabel('Время выполнения (секунды)')
plt.title('Сравнение методов разложения Ферма')
plt.grid(True)
plt.savefig('all_comparisons.png')
plt.show()
