from typing import List, Union


def coin_change(coins: List[int], amount: int) -> Union[int, float]:
    """
    Задача: Размен монет (минимальное количество).

    :param coins: Список номиналов монет.
    :param amount: Сумма, которую нужно набрать.
    :return: Минимальное количество монет или -1
    (бесконечность), если невозможно.

    Временная сложность: O(amount * len(coins)).
    Пространственная сложность: O(amount).
    """
    # Инициализируем массив "бесконечностью".
    # amount + 1, так как монет не может быть больше,
    # чем сама сумма (при монетах = 1).
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for x in range(1, amount + 1):
        for coin in coins:
            if x - coin >= 0:
                # min(текущее, 1 монета + решение для остатка)
                dp[x] = min(dp[x], 1 + dp[x - coin])

    return dp[amount] if dp[amount] != float('inf') else -1


def longest_increasing_subsequence(arr: List[int]) -> int:
    """
    Задача: Наибольшая возрастающая подпоследовательность (LIS).

    :param arr: Входной массив чисел.
    :return: Длина LIS.

    Временная сложность: O(N^2).
    Пространственная сложность: O(N).
    """
    if not arr:
        return 0

    n = len(arr)
    # dp[i] хранит длину LIS, заканчивающейся на индексе i
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                # Если элемент i больше элемента j, можно продлить
                # последовательность
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# Пример проверки
if __name__ == "__main__":
    print("Coins [1, 3, 4], amount 6: "
          f"{coin_change([1, 3, 4], 6)}")  # Ожидается 2 (3+3)
    print("LIS [10, 9, 2, 5, 3, 7, 101, 18]: "
          f"{longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])}")
