# Лабораторная работа 6
Шаг 1. Оставив представленный ниже код, переписать функции для нахождения чисел с помощью Cython, запустить timeit с аналогичными параметрами и сравнить два варианта, построить график. С помощью annotate=True сгенерируйте html (где визуализировано взаимодействие с Python-интерпретатором) и приложите его к отчету.

![image](https://github.com/user-attachments/assets/1d4ca0be-68e5-4103-a4b2-65dfe02759c4)

![image](https://github.com/user-attachments/assets/a7227971-37d5-46fb-8a72-c1ff41f528c7)

```
fermat_factorization_project/
│
├── baseline/                  # Базовая (Python) версия
│   ├── ferma_fact.py          # Исходный Python-код
│   └── main.py                # Тестирование производительности
│
├── cython_version/            # Cython-версия
│   ├── ferma_fact_cy.pyx      # Cython-реализация
│   ├── setup.py               # Настройка компиляции Cython
│   └── main_cy.py             # Запуск тестирования Cython
│
├── multiprocessing/           # Версия с параллелизацией
│   ├── parallel_cy.py         # Параллельная Cython-версия
│   └── parallel_py.py         # Параллельная Python-версия
│
├── nogil/                     # Версия с отключением GIL
│   ├── ferma_fact_nogil.pyx   # Реализация с with nogil
│   ├── setup_nogil.py         # setup.py для nogil-версии
│   └── main_nogil.py          # Тестирование nogil
│
├── requirements.txt           # Необходимые библиотеки
└── report/                    # Папка под графики
```

1
![image](https://github.com/user-attachments/assets/fc430bfd-e4c8-45e4-bb3e-accb3541809c)
2
![image](https://github.com/user-attachments/assets/74392a84-b094-4caa-acec-09ee903ca6d8)
3

![image](https://github.com/user-attachments/assets/8248616a-d8a2-4dcf-a50b-05a1f6531560)

![image](https://github.com/user-attachments/assets/74b942f2-cf1a-435c-8a74-ecff1d8dbee8)

![image](https://github.com/user-attachments/assets/27efd435-6eed-4ff5-bcc9-a0b86f2c7099)

![image](https://github.com/user-attachments/assets/1f19e559-fc7c-4665-8090-ee7e75a91dce)
