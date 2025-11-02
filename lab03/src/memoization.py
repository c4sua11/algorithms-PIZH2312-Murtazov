"""
Мемоизация рекурсивных функций на примере чисел Фибоначчи.
Сравнение наивной и мемоизированной реализации по времени выполнения
и количеству рекурсивных вызовов. Замер памяти добавлен.
"""

import time
import tracemalloc
import matplotlib.pyplot as plt
from functools import lru_cache

# -----------------------------
# Наивная рекурсивная версия
# -----------------------------
call_count_naive = 0


def fibonacci_naive(n: int) -> int:
    global call_count_naive
    call_count_naive += 1
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


# -----------------------------
# Мемоизированная версия
# -----------------------------
call_count_memo = 0


@lru_cache(maxsize=None)
def fibonacci_memo(n: int) -> int:
    global call_count_memo
    call_count_memo += 1
    if n <= 1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)


# -----------------------------
# Замеры времени и памяти
# -----------------------------
def measure_time_and_memory(func, n: int):
    tracemalloc.start()
    start = time.perf_counter()
    func(n)
    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end - start, peak / 1024  # в КБ


if __name__ == "__main__":
    ns = list(range(5, 36, 5))
    naive_times = []
    memo_times = []
    naive_memory = []
    memo_memory = []

    for n in ns:
        # Наивная версия
        call_count_naive = 0
        t, mem = measure_time_and_memory(fibonacci_naive, n)
        naive_times.append(t)
        naive_memory.append(mem)

        # Мемоизированная версия
        call_count_memo = 0
        fibonacci_memo.cache_clear()
        t, mem = measure_time_and_memory(fibonacci_memo, n)
        memo_times.append(t)
        memo_memory.append(mem)

    # Вывод для консоли
    for i, n in enumerate(ns):
        print(f"n={n}: Наивная: {naive_times[i]:.4f}s, "
              f"память={naive_memory[i]:.2f} КБ | "
              f"Мемоизация: {memo_times[i]:.4f}s, "
              f"память={memo_memory[i]:.2f} КБ")

    # -----------------------------
    # Построение графика времени
    # -----------------------------
    plt.figure(figsize=(8, 5))
    plt.plot(ns, naive_times, marker='o', label="Наивная рекурсия")
    plt.plot(ns, memo_times, marker='s', label="Мемоизация (lru_cache)")
    plt.title("Сравнение времени вычисления чисел Фибоначчи")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # -----------------------------
    # Построение графика памяти
    # -----------------------------
    plt.figure(figsize=(8, 5))
    plt.plot(ns, naive_memory, marker='o', label="Наивная рекурсия")
    plt.plot(ns, memo_memory, marker='s', label="Мемоизация (lru_cache)")
    plt.title("Пиковое потребление памяти при вычислении чисел Фибоначчи")
    plt.xlabel("n")
    plt.ylabel("Память (КБ)")
    plt.legend()
    plt.grid(True)
    plt.show()
