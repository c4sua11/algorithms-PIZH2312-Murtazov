# performance_test.py
import timeit
import random
import matplotlib.pyplot as plt
from typing import List
from asa_heap import MinHeap


def measure_build_time_sequential(data: List[int]) -> float:
    """
    Замеряет время построения кучи последовательными вставками (insert).
    """
    heap = MinHeap()
    start = timeit.default_timer()
    for item in data:
        heap.insert(item)
    return timeit.default_timer() - start


def measure_build_time_optimized(data: List[int]) -> float:
    """
    Замеряет время построения кучи методом build_heap (Floyd's algorithm).
    """
    heap = MinHeap()
    start = timeit.default_timer()
    heap.build_heap(data)
    return timeit.default_timer() - start


def run_experiments() -> None:
    """
    Запускает серию тестов и строит график.
    """
    sizes = [1000, 5000, 10000, 20000, 50000, 100000]
    times_seq = []
    times_opt = []

    print(f"{'Size':<10} | {'Sequential (s)':<15} | {'Optimized (s)':<15}")
    print("-" * 45)

    for size in sizes:
        # Генерируем случайный массив
        data = [random.randint(0, 1000000) for _ in range(size)]

        # Усредняем по 5 запускам для точности
        t_seq = timeit.timeit(
            lambda: measure_build_time_sequential(data), number=5
        ) / 5

        t_opt = timeit.timeit(
            lambda: measure_build_time_optimized(data), number=5
        ) / 5

        times_seq.append(t_seq)
        times_opt.append(t_opt)

        print(f"{size:<10} | {t_seq:<15.5f} | {t_opt:<15.5f}")

    # Визуализация
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_seq,
             label='Sequential Insert O(N log N)', marker='o')
    plt.plot(sizes, times_opt, label='Build Heap O(N)', marker='s')

    plt.title('Сравнение методов построения кучи (MinHeap)')
    plt.xlabel('Количество элементов (N)')
    plt.ylabel('Время выполнения (секунды)')
    plt.legend()
    plt.grid(True)
    plt.savefig('heap_performance.png')
    print("\nГрафик сохранен в файл 'heap_performance.png'")
    plt.show()


if __name__ == '__main__':
    run_experiments()
