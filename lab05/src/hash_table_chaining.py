"""
Модуль с реализацией хеш-таблицы с методом цепочек (Chaining).
Поддерживает операции вставки, поиска и удаления.
Все операции имеют среднюю сложность O(1 + α), где α - коэффициент заполнения.
"""

from typing import Any, List, Optional, Callable
from hash_functions import simple_hash


class HashTableChaining:
    """Хеш-таблица с методом цепочек."""

    def __init__(self, size: int = 10,
                 hash_func: Callable[[str, int], int] = simple_hash) -> None:
        """
        Инициализация таблицы.

        :param size: начальный размер хеш-таблицы
        :param hash_func: хеш-функция, по умолчанию simple_hash
        """
        self.size: int = size
        self.table: List[List[tuple[str, Any]]] = [[] for _ in range(size)]
        self.hash_func = hash_func

    def insert(self, key: str, value: Any) -> None:
        """
        Вставка элемента в таблицу.

        Средняя сложность: O(1 + α)
        Худший случай: O(n) если все элементы попадут в одну цепочку.

        :param key: ключ для вставки
        :param value: значение
        """
        index = self.hash_func(key, self.size)
        # Проверка на существующий ключ и обновление значения
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Добавление нового элемента
        self.table[index].append((key, value))

    def search(self, key: str) -> Optional[Any]:
        """
        Поиск элемента по ключу.

        Средняя сложность: O(1 + α)
        Худший случай: O(n)

        :param key: ключ для поиска
        :return: значение или None, если ключ не найден
        """
        index = self.hash_func(key, self.size)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key: str) -> bool:
        """
        Удаление элемента по ключу.

        Средняя сложность: O(1 + α)
        Худший случай: O(n)

        :param key: ключ для удаления
        :return: True, если элемент был удалён, иначе False
        """
        index = self.hash_func(key, self.size)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

    def get_chain_lengths(self) -> List[int]:
        """Возвращает список длин цепочек."""
        return [len(bucket) for bucket in self.table]

    def __str__(self) -> str:
        """Вывод таблицы для визуальной проверки."""
        result = []
        for i, bucket in enumerate(self.table):
            result.append(f"{i}: {bucket}")
        return "\n".join(result)
