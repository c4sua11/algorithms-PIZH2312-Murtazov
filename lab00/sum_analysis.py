# sum_analysis.py
import random
import timeit
from typing import List  # Для аннотации типов
import matplotlib.pyplot as plt


def calculate_sum() -> None:
    """Считает сумму двух введённых чисел и выводит результат."""
    a: int = int(input())  # O(1) - чтение одного числа
    b: int = int(input())  # O(1) - чтение второго числа
    result: int = a + b    # O(1) - одно сложение
    print(result)           # O(1) - вывод результата
    # Общая сложность: O(1)


def sum_array(arr: List[int]) -> int:
    """Возвращает сумму всех элементов массива.

    Сложность: O(N), где N - длина массива.
    """
    total: int = 0          # O(1) - инициализация переменной
    for num in arr:         # O(N) - проход по всем элементам
        total += num        # O(1) - операция сложения и присваивания
    return total            # O(1) - возврат результата
    # Общая сложность: O(N)


def measure_time(func, data) -> float:
    """Измеряет время выполнения функции в секундах."""
    start_time: float = timeit.default_timer()
    func(data)
    end_time: float = timeit.default_timer()
    return end_time - start_time

# Характеристики ПК
pc_info = """
Характеристики ПК для тестирования:
- Процессор: Intel Core i5-10400f @ 2.90GHz
- Оперативная память: 32 GB DDR4
- ОС: Windows 11
- Python: 3.11.2
"""
print(pc_info)

def main() -> None:
    """Проводит эксперименты по суммированию массивов и строит график."""
    # Размеры массивов для экспериментов
    sizes: List[int] = [1000, 5000, 10000, 50000, 100000, 500000]
    times: List[float] = []

    for size in sizes:
        arr: List[int] = [random.randint(1, 100) for _ in range(size)]
        execution_time: float = timeit.timeit(lambda: sum_array(arr), number=5) / 5
        times.append(execution_time)
        print(f'N={size}, время={execution_time:.6f} сек')

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, 'bo-', label='Измеренное время')
    plt.xlabel('Размер массива (N)')
    plt.ylabel('Время выполнения (сек)')
    plt.title('Зависимость времени суммирования массива от N')
    plt.grid(True)
    plt.legend()
    plt.savefig('time_complexity_plot.png', dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    # calculate_sum()  # Раскомментировать для проверки задачи с 2 числами
    main()
