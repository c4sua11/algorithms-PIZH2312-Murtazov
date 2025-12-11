import sys
from typing import List, Dict, Optional

# Увеличим лимит рекурсии для глубоких вызовов
# (например, для LCS на длинных строках)
sys.setrecursionlimit(2000)


def fib_top_down(n: int, memo: Optional[Dict[int, int]] = None) -> int:
    """
    Вычисление n-го числа Фибоначчи: Нисходящий подход (с мемоизацией).

    :param n: Порядковый номер числа Фибоначчи.
    :param memo: Словарь для кэширования результатов.
    :return: Значение числа Фибоначчи.

    Временная сложность: O(n) - каждый подзадача решается 1 раз.
    Пространственная сложность: O(n) - глубина стека + память под словарь.
    """
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    # Рекурсивный вызов с сохранением результата
    memo[n] = fib_top_down(n - 1, memo) + fib_top_down(n - 2, memo)
    return memo[n]


def fib_bottom_up(n: int) -> int:
    """
    Вычисление n-го числа Фибоначчи: Восходящий подход (табличный).

    :param n: Порядковый номер числа.
    :return: Значение числа.

    Временная сложность: O(n) - линейный проход.
    Пространственная сложность:
    O(n) - под массив (можно оптимизировать до O(1)).
    """
    if n <= 1:
        return n

    # Инициализация таблицы
    dp: List[int] = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def knapsack_0_1(capacity: int, weights: List[int], values: List[int]) -> int:
    """
    Задача о рюкзаке 0-1: Восходящий подход (2D таблица).

    :param capacity: Вместимость рюкзака (W).
    :param weights: Список весов предметов.
    :param values: Список стоимостей предметов.
    :return: Максимальная стоимость.

    Временная сложность: O(N * W), где N - кол-во предметов, W - вместимость.
    Пространственная сложность: O(N * W) - под таблицу dp.
    """
    n_items = len(weights)
    # Создаем таблицу размером (N+1) x (W+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n_items + 1)]

    for i in range(1, n_items + 1):
        for w in range(1, capacity + 1):
            weight = weights[i - 1]
            value = values[i - 1]

            if weight <= w:
                # Максимум: либо берем предмет
                # (и вычитаем его вес), либо не берем
                dp[i][w] = max(
                    value + dp[i - 1][w - weight],  # Берем
                    dp[i - 1][w]                    # Не берем
                )
            else:
                # Предмет не влезает, оставляем предыдущий результат
                dp[i][w] = dp[i - 1][w]

    return dp[n_items][capacity]


def lcs_top_down(s1: str, s2: str, i: int, j: int,
                 memo: Optional[Dict[str, int]] = None) -> int:
    """
    Наибольшая общая подпоследовательность (LCS): Нисходящий подход.

    :param s1: Первая строка.
    :param s2: Вторая строка.
    :param i: Текущий индекс в s1.
    :param j: Текущий индекс в s2.
    :param memo: Словарь для мемоизации.
    :return: Длина LCS.

    Временная сложность: O(N * M), где N и M - длины строк.
    Пространственная сложность: O(N * M) - память под memo и стек.
    """
    if memo is None:
        memo = {}

    key = f"{i},{j}"

    if key in memo:
        return memo[key]

    # Базовый случай: строки закончились
    if i == len(s1) or j == len(s2):
        return 0

    if s1[i] == s2[j]:
        # Символы совпали, увеличиваем счетчик и двигаем оба индекса
        res = 1 + lcs_top_down(s1, s2, i + 1, j + 1, memo)
    else:
        # Символы разные, ветвимся: пропускаем символ в s1 или в s2
        res = max(
            lcs_top_down(s1, s2, i + 1, j, memo),
            lcs_top_down(s1, s2, i, j + 1, memo)
        )

    memo[key] = res
    return res


def lcs_bottom_up(s1: str, s2: str) -> int:
    """
    Наибольшая общая подпоследовательность (LCS): Восходящий подход.

    :param s1: Первая строка.
    :param s2: Вторая строка.
    :return: Длина LCS.

    Временная сложность: O(N * M).
    Пространственная сложность: O(N * M) - таблица dp.
    """
    n, m = len(s1), len(s2)
    # Таблица (n+1) x (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                # Если символы равны, берем значение по диагонали + 1
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                # Иначе берем максимум сверху или слева
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]
