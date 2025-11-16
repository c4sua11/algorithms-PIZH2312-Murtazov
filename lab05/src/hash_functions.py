"""
Модуль с реализацией хеш-функций для строковых ключей.
Содержит три функции:
1. Простая сумма кодов символов
2. Полиномиальная хеш-функция
3. DJB2
Все функции возвращают индекс в пределах размера хеш-таблицы.
"""


def simple_hash(key: str, table_size: int) -> int:
    """
    Простая хеш-функция: сумма кодов символов по модулю размера таблицы.
    Применимость: только для учебных целей, распределение среднее.
    Сложность: O(n), где n - длина строки.
    """
    return sum(ord(char) for char in key) % table_size


def polynomial_hash(key: str, table_size: int, p: int = 31) -> int:
    """
    Полиномиальная хеш-функция.
    hash = (key[0]*p^(n-1) + key[1]*p^(n-2) + ... + key[n-1]) % table_size
    Применимость: хорошее распределение для строк разной длины.
    Сложность: O(n), где n - длина строки.
    :param key: строковый ключ
    :param table_size: размер хеш-таблицы
    :param p: основание полинома, обычно простое число
    :return: индекс в хеш-таблице
    """
    hash_value = 0
    for char in key:
        hash_value = (hash_value * p + ord(char)) % table_size
    return hash_value


def djb2_hash(key: str, table_size: int) -> int:
    """
    Хеш-функция DJB2.
    Алгоритм: hash = 5381, затем hash = hash * 33 + c для каждого символа.
    Применимость: эффективная и популярная функция с хорошим распределением.
    Сложность: O(n), где n - длина строки.
    :param key: строковый ключ
    :param table_size: размер хеш-таблицы
    :return: индекс в хеш-таблице
    """
    hash_value = 5381
    for char in key:
        hash_value = ((hash_value << 5) +
                      hash_value) + ord(char)  # hash * 33 + ord(char)
    return hash_value % table_size


# Пример тестирования функций
if __name__ == "__main__":
    test_keys = ["apple", "banana", "orange", "grape"]
    table_size_example = 10

    print("Simple Hash:")
    for key in test_keys:
        print(f"{key}: {simple_hash(key, table_size_example)}")

    print("\nPolynomial Hash:")
    for key in test_keys:
        print(f"{key}: {polynomial_hash(key, table_size_example)}")

    print("\nDJB2 Hash:")
    for key in test_keys:
        print(f"{key}: {djb2_hash(key, table_size_example)}")
