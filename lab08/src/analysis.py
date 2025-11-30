# analysis.py
import timeit
import random
import string
from greedy_algorithms import (
    interval_scheduling,
    fractional_knapsack,
    huffman_coding,
    Item
)


def test_knapsack_01_failure():
    """
    Демонстрация того, что жадный алгоритм НЕ работает для 0-1 рюкзака
    (когда предметы нельзя делить).
    """
    print("\n=== Анализ: Жадный подход vs 0-1 Рюкзак ===")
    capacity = 50
    # Предметы: (стоимость, вес)
    # Удельная стоимость:
    # 1: 60/10 = 6.0
    # 2: 100/20 = 5.0
    # 3: 120/30 = 4.0
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]

    print(f"Предметы: {items}")
    print(f"Вместимость: {capacity}")

    # Жадный выбор (по удельной стоимости):
    # 1. Берем Item(60, 10). Осталось места: 40. Value: 60.
    # 2. Берем Item(100, 20). Осталось места: 20. Value: 160.
    # 3. Item(120, 30) не влезает.
    # Итог жадного: 160.

    # Оптимальный выбор:
    # Берем Item(100, 20) и Item(120, 30). Вес 50/50.
    # Итог оптимальный: 220.

    print("Жадный выбор (берем по max удельной цене):")
    print(" -> Берем (60, 10) и (100, 20). Итог = 160.")

    print("Оптимальный выбор (полный перебор):")
    print(" -> Берем (100, 20) и (120, 30). Итог = 220.")
    print("Вывод: Жадный алгоритм не гарантирует оптимум для 0-1 рюкзака.")


def benchmark_huffman():
    """Замер производительности алгоритма Хаффмана."""
    print("\n=== Замеры времени: Huffman Coding ===")
    sizes = [1000, 10000, 100000, 500000]
    print(f"{'Size (chars)':<15} | {'Time (sec)':<15}")
    print("-" * 35)

    for size in sizes:
        # Генерируем случайный текст
        text = ''.join(random.choices(
            string.ascii_letters + string.digits, k=size))

        t = timeit.timeit(lambda: huffman_coding(text), number=10) / 10
        print(f"{size:<15} | {t:<15.5f}")


if __name__ == "__main__":
    # 1. Тест интервалов
    intervals = [(1, 4), (3, 5),
                 (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11)]
    selected = interval_scheduling(intervals)
    print(f"Interval Scheduling Result: {selected}")

    # 2. Тест дробного рюкзака
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]
    val = fractional_knapsack(items, 50)
    print("Fractional Knapsack Value: "
          f"{val}")  # Ожидается 240.0 (60 + 100 + 2/3 * 120)

    # 3. Тест Хаффмана
    text = "banana"
    codes = huffman_coding(text)
    print(f"Huffman Codes for 'banana': {codes}")

    # 4. Демонстрация проблемы 0-1 и замеры
    test_knapsack_01_failure()
    benchmark_huffman()
