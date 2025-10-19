"""

Практические задачи с использованием рекурсии:
1. Бинарный поиск
2. Рекурсивный обход файловой системы
3. Задача "Ханойские башни"
"""

import os


# -----------------------------
# 1. Бинарный поиск (рекурсивный)
# -----------------------------
def binary_search(arr, target, left=0, right=None):
    """
    Рекурсивный бинарный поиск.
    Время: O(log n)
    Глубина рекурсии: log n
    """
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1  # элемент не найден

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)


# -----------------------------
# 2. Рекурсивный обход файловой системы
# -----------------------------
def traverse_directory(path, depth=0):
    """
    Рекурсивный обход директорий.
    Время: O(n), где n = количество файлов/директорий
    Глубина рекурсии: зависит от глубины вложенности
    """
    if not os.path.exists(path):
        print("Путь не существует")
        return

    indent = "  " * depth
    if os.path.isfile(path):
        print(f"{indent}- {os.path.basename(path)}")
    else:
        print(f"{indent}+ {os.path.basename(path)}")
        for entry in os.listdir(path):
            traverse_directory(os.path.join(path, entry), depth + 1)


# -----------------------------
# 3. Задача "Ханойские башни"
# -----------------------------
def hanoi(n, source='A', target='C', auxiliary='B', moves=None):
    """
    Рекурсивное решение Ханойских башен.
    Время: O(2^n)
    Глубина рекурсии: n
    """
    if moves is None:
        moves = []

    if n == 1:
        moves.append(f"Переместить диск 1 с {source} на {target}")
    else:
        hanoi(n - 1, source, auxiliary, target, moves)
        moves.append(f"Переместить диск {n} с {source} на {target}")
        hanoi(n - 1, auxiliary, target, source, moves)

    return moves


# -----------------------------
# Примеры вызова
# -----------------------------
if __name__ == "__main__":
    # Бинарный поиск
    arr = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    idx = binary_search(arr, target)
    print(f"Бинарный поиск: элемент {target} найден на индексе {idx}\n")

    # Рекурсивный обход файловой системы
    print("Обход текущей директории:")
    traverse_directory('.', depth=0)
    print()

    # Ханойские башни
    print("Ханойские башни для 3 дисков:")
    moves = hanoi(3)
    for move in moves:
        print(move)
