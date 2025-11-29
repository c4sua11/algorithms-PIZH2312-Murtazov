import sys
import random
import timeit
import matplotlib.pyplot as plt
from binary_search_tree import BinarySearchTree

# Увеличиваем лимит рекурсии для работы с глубокими деревьями (sorted input)
sys.setrecursionlimit(20000)


def measure_search_time(elements: list, search_ops: int = 1000) -> float:
    """
    Создает дерево из elements и замеряет время поиска.
    """
    bst = BinarySearchTree()
    for el in elements:
        bst.insert(el)

    # Генерация случайных ключей для поиска
    search_keys = [random.choice(elements) for _ in range(search_ops)]

    # Функция для timeit
    def run_search():
        for key in search_keys:
            bst.search(key)

    # Замер времени (1 запуск, так как внутри уже цикл из 1000 операций)
    time = timeit.timeit(run_search, number=1)
    return time


def run_experiments():
    # Размеры массивов для теста (5+ размеров для оценки "4")
    sizes = [100, 500, 1000, 2000, 5000, 7500]

    times_random = []
    times_sorted = []

    print('Starting performance analysis...')
    print(f"{'Size':<10} | {'Random (sec)':<15} | {'Sorted (sec)':<15}")
    print("-" * 45)

    for size in sizes:
        # 1. Случайные данные (Сбалансированное дерево в среднем случае)
        random_data = list(range(size))
        random.shuffle(random_data)
        t_rand = measure_search_time(random_data)
        times_random.append(t_rand)

        # 2. Отсортированные данные (Вырожденное дерево -> связный список)
        # Берем меньший размер для sorted, иначе рекурсия упадет или будет
        # очень долго (O(N) поиск). Для корректного сравнения на графике
        # обычно ограничивают sorted, но здесь оставим равные size,
        # но будьте готовы к долгому выполнению на больших N.
        # Для безопасности на больших N ограничим sorted данные до 3000
        if size <= 3000:
            sorted_data = list(range(size))
            t_sort = measure_search_time(sorted_data)
            times_sorted.append(t_sort)
        else:
            times_sorted.append(None)

        print(f"{size:<10} | {t_rand:<15.6f} | "
              f"{str(t_sort) if size <= 3000 else 'Skipped':<15}")

    # Построение графиков
    plt.figure(figsize=(10, 6))

    # График для случайных данных
    plt.plot(sizes, times_random, label='Random Input (Avg O(log N))',
             marker='o', color='green')

    # График для отсортированных данных (фильтруем None)
    valid_sorted_sizes = [s for s, t in zip(sizes, times_sorted) if t]
    valid_sorted_times = [t for t in times_sorted if t]

    plt.plot(valid_sorted_sizes, valid_sorted_times,
             label='Sorted Input (Worst O(N))',
             marker='x', color='red', linestyle='--')

    plt.title('BST Search Performance: Random vs Sorted Input')
    plt.xlabel('Number of Elements (N)')
    plt.ylabel('Time for 1000 searches (seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('bst_performance.png')
    print("\nГрафик сохранен как 'bst_performance.png'")


if __name__ == '__main__':
    run_experiments()
