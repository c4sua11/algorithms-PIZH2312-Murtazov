"""
Рекурсивные функции:
- factorial(n)
- fibonacci(n)  (наивная рекурсия)
- power(a, n)   (быстрое возведение в степень, рекурсивно)
Каждая функция содержит комментарий с оценкой временной сложности
и глубины рекурсии.
"""

from __future__ import annotations
from typing import Union

Number = Union[int, float]


def factorial(n: int) -> int:
    """
    Рекурсивное вычисление факториала n!.

    :param n: неотрицательное целое число
    :return: n!

    Сложность по времени: O(n).
    Глубина рекурсии: O(n) (максимальная глубина вызовов равна n).
    """
    if n < 0:
        raise ValueError("factorial: n must be >= 0")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    Наивная рекурсивная реализация n-го числа Фибоначчи.

    :param n: неотрицательное целое число
    :return: n-е число Фибоначчи (F(0)=0, F(1)=1)

    Сложность по времени: O(2^n) (экспоненциальная).
    Глубина рекурсии: O(n) (максимальная глубина — n).
    Примечание: количество рекурсивных вызовов растёт экспоненциально,
    поэтому этот вариант применяется только для небольших n.
    """
    if n < 0:
        raise ValueError("fibonacci: n must be >= 0")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def power(a: Number, n: int) -> Number:
    """
    Быстрое возведение в степень (рекурсивно, exponentiation by squaring).

    :param a: основание (int или float)
    :param n: целая неотрицательная степень
    :return: a ** n

    Идея: a^n = (a^(n//2))^2   если n чётно
           a^n = a * a^(n-1)    если n нечётно

    Сложность по времени: O(log n) рекурсивных умножений.
    Глубина рекурсии: O(log n) (логарифмическая глубина вызовов).
    """
    if n < 0:
        raise ValueError("power: n must be >= 0")
    if n == 0:
        return 1  # a^0 == 1
    if n == 1:
        return a
    half = power(a, n // 2)
    if n % 2 == 0:
        return half * half
    return a * half * half


if __name__ == "__main__":
    print("factorial(0) =", factorial(0))      # 1
    print("factorial(5) =", factorial(5))      # 120

    print("fibonacci(0) =", fibonacci(0))      # 0
    print("fibonacci(1) =", fibonacci(1))      # 1
    print("fibonacci(6) =", fibonacci(6))      # 8

    print("power(2, 0) =", power(2, 0))        # 1
    print("power(2, 10) =", power(2, 10))      # 1024
