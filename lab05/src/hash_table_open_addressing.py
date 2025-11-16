"""
Модуль с реализацией хеш-таблицы с открытой адресацией.
Поддерживает линейное пробирование и
двойное хеширование для разрешения коллизий.
Все операции имеют среднюю сложность O(1), худшую O(n).
"""

from typing import Any, Optional
from hash_functions import simple_hash, djb2_hash


class HashTableOpenAddressing:
    """Хеш-таблица с открытой адресацией."""

    def __init__(self, size: int = 10) -> None:
        """
        Инициализация таблицы.

        :param size: размер хеш-таблицы
        """
        self.size: int = size
        self.table: list[Optional[tuple[str, Any]]] = [None] * size

    def _probe_linear(self, key: str, i: int) -> int:
        """Линейное пробирование: (h + i) % size"""
        return (simple_hash(key, self.size) + i) % self.size

    def _probe_double(self, key: str, i: int) -> int:
        """Двойное хеширование: (h1 + i*h2) % size"""
        h1 = simple_hash(key, self.size)
        h2 = 1 + djb2_hash(key, self.size - 1)
        return (h1 + i * h2) % self.size

    def insert(self, key: str, value: Any, method: str = "linear") -> None:
        """
        Вставка элемента в таблицу.

        Средняя сложность: O(1)
        Худший случай: O(n), если таблица почти полна.

        :param key: ключ для вставки
        :param value: значение
        :param method: "linear" для
        линейного пробирования, "double" для двойного хеширования
        """
        for i in range(self.size):
            index = (self._probe_linear(key, i) if method == "linear"
                     else self._probe_double(key, i))
            entry = self.table[index]
            if entry is None or entry[0] == key:
                self.table[index] = (key, value)
                return
        raise Exception("Хеш-таблица переполнена")

    def search(self, key: str, method: str = "linear") -> Optional[Any]:
        """
        Поиск элемента по ключу.

        Средняя сложность: O(1)
        Худший случай: O(n)

        :param key: ключ для поиска
        :param method: метод пробирования
        :return: значение или None, если ключ не найден
        """
        for i in range(self.size):
            index = (self._probe_linear(key, i) if method == "linear"
                     else self._probe_double(key, i))
            entry = self.table[index]
            if entry is None:
                return None
            if entry[0] == key:
                return entry[1]
        return None

    def delete(self, key: str, method: str = "linear") -> bool:
        """
        Удаление элемента по ключу.

        Средняя сложность: O(1)
        Худший случай: O(n)

        :param key: ключ для удаления
        :param method: метод пробирования
        :return: True, если элемент был удалён, иначе False
        """
        for i in range(self.size):
            index = (self._probe_linear(key, i) if method == "linear"
                     else self._probe_double(key, i))
            entry = self.table[index]
            if entry is None:
                return False
            if entry[0] == key:
                self.table[index] = None
                return True
        return False

    def __str__(self) -> str:
        """Вывод таблицы для визуальной проверки."""
        result = []
        for i, entry in enumerate(self.table):
            result.append(f"{i}: {entry}")
        return "\n".join(result)


# Пример тестирования
if __name__ == "__main__":
    ht = HashTableOpenAddressing(size=7)
    keys = ["apple", "banana", "orange", "grape", "lemon"]
    for k in keys:
        ht.insert(k, len(k), method="linear")

    print("Таблица после вставок (линейное пробирование):")
    print(ht)

    print("\nПоиск 'banana':", ht.search("banana", method="linear"))
    print("Поиск 'pear':", ht.search("pear", method="linear"))

    print("\nУдаление 'orange':", ht.delete("orange", method="linear"))
    print("Таблица после удаления:")
    print(ht)

    print("\nТест двойного хеширования:")
    ht_double = HashTableOpenAddressing(size=7)
    for k in keys:
        ht_double.insert(k, len(k), method="double")
    print(ht_double)
