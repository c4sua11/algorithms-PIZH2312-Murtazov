import random
import time
import matplotlib.pyplot as plt

def linear_search(arr: list[int], target: int) -> int:
    """
    Линейный поиск элемента в массиве.
    Сложность: O(n)
    """
    for i in range(len(arr)):  # O(n)
        if arr[i] == target:  # O(1)
            return i  # O(1)
    return -1  # O(1)
# Общая сложность: O(n)


def binary_search(arr: list[int], target: int) -> int:
    """
    Бинарный поиск элемента в отсортированном массиве.
    Сложность: O(log n)
    """
    left = 0  # O(1)
    right = len(arr) - 1  # O(1)

    while left <= right:  # O(log n)
        mid = (left + right) // 2  # O(1)

        if arr[mid] == target:  # O(1)
            return mid  # O(1)
        elif arr[mid] < target:  # O(1)
            left = mid + 1  # O(1)
        else:
            right = mid - 1  # O(1)
    return -1  # O(1)
# Общая сложность: O(log n)

def generate_array(size: int) -> list[int]:
    """
    Генерация отсортированного массива целых чисел от 0 до size-1.
    Сложность: O(n)
    """
    return list(range(size))  # O(n)

def measure_time(func, arr: list[int], target: int,
                 repeats: int = 5) -> float:
    """
    Замер среднего времени выполнения функции поиска.
    Сложность: O(repeats * сложность func)
    """
    total_time = 0.0  # O(1)

    for _ in range(repeats):  # O(repeats)
        start = time.perf_counter()  # O(1)
        func(arr, target)  # O(n) или O(log n)
        end = time.perf_counter()  # O(1)
        total_time += (end - start)  # O(1)

    return total_time / repeats  # O(1)

def run_experiments() -> dict:
    """
    Запускает эксперименты для линейного и бинарного поиска
    на массивах разных размеров и в 4 сценариях.
    """
    sizes = [1000, 2000, 5000, 10_000, 50_000,
             100_000, 500_000, 1_000_000]

    results: dict = {
        'linear': {'first': [], 'middle': [], 'last': [], 'absent': []},
        'binary': {'first': [], 'middle': [], 'last': [], 'absent': []}
    }

    for size in sizes:
        arr = generate_array(size)  # O(n)

        # Линейный поиск
        results['linear']['first'].append(
            measure_time(linear_search, arr, arr[0])
        )
        results['linear']['middle'].append(
            measure_time(linear_search, arr, arr[size // 2])
        )
        results['linear']['last'].append(
            measure_time(linear_search, arr, arr[-1])
        )
        results['linear']['absent'].append(
            measure_time(linear_search, arr, -1)
        )

        # Бинарный поиск
        results['binary']['first'].append(
            measure_time(binary_search, arr, arr[0])
        )
        results['binary']['middle'].append(
            measure_time(binary_search, arr, arr[size // 2])
        )
        results['binary']['last'].append(
            measure_time(binary_search, arr, arr[-1])
        )
        results['binary']['absent'].append(
            measure_time(binary_search, arr, -1)
        )

    return {'sizes': sizes, 'results': results}

def plot_results(data: dict) -> None:
    """
    График в линейном масштабе.
    """
    sizes = data['sizes']
    results = data['results']

    plt.figure(figsize=(12, 6))

    for case, times in results['linear'].items():
        plt.plot(sizes, times, marker='o', label=f'Linear - {case}')

    for case, times in results['binary'].items():
        plt.plot(sizes, times, marker='x', linestyle='--',
                 label=f'Binary - {case}')

    plt.xlabel('Размер массива (N)')
    plt.ylabel('Время (секунды)')
    plt.title('Сравнение линейного и бинарного поиска')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_results_log(data: dict) -> None:
    """
    График в логарифмическом масштабе по оси Y.
    """
    sizes = data['sizes']
    results = data['results']

    plt.figure(figsize=(12, 6))

    for case, times in results['linear'].items():
        plt.plot(sizes, times, marker='o', label=f'Linear - {case}')

    for case, times in results['binary'].items():
        plt.plot(sizes, times, marker='x', linestyle='--',
                 label=f'Binary - {case}')

    plt.xlabel('Размер массива (N)')
    plt.ylabel('Время (секунды, log scale)')
    plt.title('Сравнение линейного и бинарного поиска (логарифмический масштаб)')
    plt.yscale('log')
    plt.legend()
    plt.grid(True, which='both')
    plt.show()

if __name__ == '__main__':
    data = run_experiments()

    # Табличка с первыми результатами
    print('Размеры массивов:', data['sizes'])
    print()
    for algo in ['linear', 'binary']:
        print(f'Алгоритм: {algo}')
        for case in ['first', 'middle', 'last', 'absent']:
            times = data['results'][algo][case]
            print(f'  Сценарий {case:7}: {times}')
        print()

    # Графики
    plot_results(data)
    plot_results_log(data)
