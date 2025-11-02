"""
Реализации пяти алгоритмов сортировки:
- bubble_sort
- selection_sort
- insertion_sort
- merge_sort
- quick_sort

Каждая функция сортирует копию входного списка и возвращает её.
Докстринги включают временную и пространственную сложность.
"""

from typing import List, Sequence


def sorted_copy(arr: Sequence[int]) -> List[int]:
    """Возвращает копию списка для сортировки (не мутирует вход)."""
    return list(arr)


def is_sorted(arr: Sequence[int]) -> bool:
    """Проверяет, отсортирован ли массив по неубыванию."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


# ----------------------
# 1. Bubble Sort
# ----------------------
def bubble_sort(arr: Sequence[int]) -> List[int]:
    """
    Пузырьковая сортировка (in-place, но возвращаем копию).

    Временная сложность:
      - Лучший: O(n) (если оптимизировать и не делать проходы,
      когда нет обменов).
      - Средний: O(n^2).
      - Худший: O(n^2).

    Пространственная сложность:
      - O(1) дополнительной памяти (in-place).
    """
    a = sorted_copy(arr)
    n = len(a)
    # Внешний цикл: O(n)
    for i in range(n):
        swapped = False
        # Внутренний цикл: O(n - i)
        for j in range(0, n - i - 1):
            # Сравнение соседних элементов: O(1)
            if a[j] > a[j + 1]:
                # Обмен элементов: O(1)
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


# ----------------------
# 2. Selection Sort
# ----------------------
def selection_sort(arr: Sequence[int]) -> List[int]:
    """
    Сортировка выбором.

    Временная сложность:
      - Лучший: O(n^2).
      - Средний: O(n^2).
      - Худший: O(n^2).

    Пространственная сложность:
      - O(1) дополнительной памяти (in-place).
    """
    a = sorted_copy(arr)
    n = len(a)
    # Проходим по всем позициям i: O(n)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a


# ----------------------
# 3. Insertion Sort
# ----------------------
def insertion_sort(arr: Sequence[int]) -> List[int]:
    """
    Сортировка вставками.

    Временная сложность:
      - Лучший: O(n) (если массив уже отсортирован).
      - Средний: O(n^2).
      - Худший: O(n^2).

    Пространственная сложность:
      - O(1) дополнительной памяти (in-place).
    """
    a = sorted_copy(arr)
    n = len(a)
    # i от 1 до n-1: O(n)
    for i in range(1, n):
        key = a[i]  # O(1)
        j = i - 1
        # Сдвигаем элементы больше key вправо: O(k) где k — число сдвигов
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# ----------------------
# 4. Merge Sort
# ----------------------
def merge(left: List[int], right: List[int]) -> List[int]:
    """Слить два отсортированных списка в один."""
    i = j = 0
    merged: List[int] = []
    # Слияние: O(len(left) + len(right))
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Добавляем остатки: O(remaining)
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    return merged


def merge_sort(arr: Sequence[int]) -> List[int]:
    """
    Сортировка слиянием (рекурсивная).

    Временная сложность:
      - Лучший: O(n log n).
      - Средний: O(n log n).
      - Худший: O(n log n).

    Пространственная сложность:
      - O(n) дополнительной памяти для слияния.
    """
    a = list(arr)
    n = len(a)
    if n <= 1:
        return a
    mid = n // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)


# ----------------------
# 5. Quick Sort
# ----------------------
def quick_sort(arr: Sequence[int]) -> List[int]:
    """
    Быстрая сортировка (рекурсивная, на месте в идеале, здесь —
    функциональная версия).

    Временная сложность:
      - Лучший: O(n log n).
      - Средний: O(n log n).
      - Худший: O(n^2) (например, при уже отсортированном массиве и
        выборе первого элемента как опорного).

    Пространственная сложность:
      - O(log n) в среднем для рекурсивного стека (в рекурсивной реализации).
      - Дополнительная память зависит от реализации; здесь мы используем
        список для результатов (не in-place).
    """
    a = list(arr)
    n = len(a)
    if n <= 1:
        return a
    # Выбираем опорный элемент — медиану из трёх для надёжности
    mid = n // 2
    pivots = (a[0], a[mid], a[-1])
    pivot = sorted(pivots)[1]
    less: List[int] = []
    equal: List[int] = []
    greater: List[int] = []
    # Разбиение: O(n)
    for x in a:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return quick_sort(less) + equal + quick_sort(greater)


# ----------------------
# Самопроверка (короткие тесты)
# ----------------------
if __name__ == "__main__":
    tests = [
        [],
        [1],
        [2, 1],
        [3, 1, 2],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [2, 3, 2, 1, 0, 5, 3],
    ]

    algos = [
        ("bubble_sort", bubble_sort),
        ("selection_sort", selection_sort),
        ("insertion_sort", insertion_sort),
        ("merge_sort", merge_sort),
        ("quick_sort", quick_sort),
    ]

    for name, func in algos:
        for t in tests:
            res = func(t)
            if not is_sorted(res):
                raise AssertionError(
                    f"{name} failed on input {t}. Got {res}"
                )
    print("All sorting algorithms passed basic tests.")
