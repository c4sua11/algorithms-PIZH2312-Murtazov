"""
Модуль для эмпирического анализа производительности алгоритмов сортировки.
Использует данные, сгенерированные в generate_data.py, и
сортировки из sorts.py.
"""

import time
import pandas as pd
from generate_data import generate_all_datasets
from sorts import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
)

# Список тестируемых алгоритмов
SORT_FUNCTIONS = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
}


def measure_time(sort_func, data):
    """Измеряет время выполнения одной сортировки на копии массива."""
    data_copy = data.copy()
    start = time.perf_counter()
    sort_func(data_copy)
    end = time.perf_counter()
    return end - start


def run_performance_tests():
    """Проводит замеры времени для всех алгоритмов и наборов данных."""
    datasets = generate_all_datasets()
    results = []

    for data_type, size_dict in datasets.items():
        for n, arr in size_dict.items():
            print(f"\n📊 Тест: {data_type}, размер {n}")
            for name, func in SORT_FUNCTIONS.items():
                elapsed = measure_time(func, arr)
                print(f"{name:15} | {elapsed:.6f} сек")
                results.append({
                    "Тип данных": data_type,
                    "Размер": n,
                    "Алгоритм": name,
                    "Время (сек)": elapsed
                })

    # Конвертация в DataFrame для дальнейшего анализа
    df = pd.DataFrame(results)
    df.to_csv("results.csv", index=False)
    print("\n Все результаты сохранены в results.csv")
    return df


if __name__ == "__main__":
    df_results = run_performance_tests()
    print(df_results.head())
