"""
Генерация тестовых массивов.

Типы данных:
- random         — случайный порядок
- sorted         — уже отсортированный
- reversed       — отсортированный в обратном порядке
- almost_sorted  — почти отсортированный (95% упорядочено, 5% перемешано)

Размеры:
- 100
- 1000
- 5000
- 10000

Для воспроизводимости устанавливается seed.
"""

import random
from typing import Dict, List


def generate_random_array(size: int) -> List[int]:
    """Случайный массив целых чисел."""
    return [random.randint(0, size * 10) for _ in range(size)]


def generate_sorted_array(size: int) -> List[int]:
    """Отсортированный по возрастанию массив."""
    return list(range(size))


def generate_reversed_array(size: int) -> List[int]:
    """Отсортированный по убыванию массив."""
    return list(range(size, 0, -1))


def generate_almost_sorted_array(size: int,
                                 percent_unsorted: float = 0.05) -> List[int]:
    """
    Почти отсортированный массив: 95% упорядочено, 5% перемешано.

    percent_unsorted — доля элементов, которые будут перемешаны (0.0–1.0).
    """
    arr = list(range(size))
    count_to_shuffle = int(size * percent_unsorted)
    indices = random.sample(range(size), count_to_shuffle)
    random.shuffle(indices)
    for i in range(0, len(indices) - 1, 2):
        arr[indices[i]], arr[indices[i + 1]] = (
            arr[indices[i + 1]],
            arr[indices[i]]
        )
    return arr


def generate_all_datasets(
    sizes=(100, 1000, 5000, 10000), seed: int = 42
) -> Dict[str, Dict[int, List[int]]]:
    """
    Генерация всех наборов данных для тестирования сортировок.
    Возвращает словарь: {type -> {size -> list}}.
    """
    random.seed(seed)
    datasets: Dict[str, Dict[int, List[int]]] = {
        "random": {},
        "sorted": {},
        "reversed": {},
        "almost_sorted": {},
    }

    for size in sizes:
        datasets["random"][size] = generate_random_array(size)
        datasets["sorted"][size] = generate_sorted_array(size)
        datasets["reversed"][size] = generate_reversed_array(size)
        datasets["almost_sorted"][size] = generate_almost_sorted_array(size)

    return datasets


if __name__ == "__main__":
    data = generate_all_datasets()
    for dtype, sets in data.items():
        print(f"\nТип данных: {dtype}")
        for size, arr in sets.items():
            print(f"  {size} элементов → первые 10: {arr[:10]}")
