# Лабораторная работа 6


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


![image](https://github.com/user-attachments/assets/fc430bfd-e4c8-45e4-bb3e-accb3541809c)


![image](https://github.com/user-attachments/assets/74392a84-b094-4caa-acec-09ee903ca6d8)


![image](https://github.com/user-attachments/assets/8248616a-d8a2-4dcf-a50b-05a1f6531560)


![image](https://github.com/user-attachments/assets/74b942f2-cf1a-435c-8a74-ecff1d8dbee8)


![image](https://github.com/user-attachments/assets/27efd435-6eed-4ff5-bcc9-a0b86f2c7099)


![image](https://github.com/user-attachments/assets/1f19e559-fc7c-4665-8090-ee7e75a91dce)
