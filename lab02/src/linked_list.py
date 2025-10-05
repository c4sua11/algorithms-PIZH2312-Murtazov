class Node:
    """Класс узла связного списка"""
    def __init__(self, data):
        self.data = data        # O(1) — присвоение значения
        self.next = None        # O(1) — ссылка на следующий элемент


class LinkedList:
    """Класс односвязного списка"""
    def __init__(self):
        self.head = None        # O(1) — указатель на первый элемент
        self.tail = None        # O(1) — указатель на последний элемент

    def insert_at_start(self, data):
        """Вставка элемента в начало списка"""
        new_node = Node(data)   # O(1) — создание узла
        new_node.next = self.head  # O(1) — связь нового узла со старым первым
        self.head = new_node       # O(1) — обновляем голову списка
        if self.tail is None:      # O(1) — если список пуст
            self.tail = new_node   # O(1)
        # Итоговая сложность: O(1)

    def insert_at_end(self, data):
        """Вставка элемента в конец списка"""
        new_node = Node(data)   # O(1)
        if self.tail:           # O(1) — если хвост уже есть
            self.tail.next = new_node  # O(1)
            self.tail = new_node       # O(1)
        else:
            self.head = new_node  # O(1) — если список пуст
            self.tail = new_node  # O(1)
        # Итоговая сложность: O(1)

    def delete_from_start(self):
        """Удаление элемента из начала списка"""
        if self.head is None:   # O(1) — проверка пустоты
            return None
        deleted_value = self.head.data  # O(1)
        self.head = self.head.next      # O(1)
        if self.head is None:           # O(1)
            self.tail = None            # O(1)
        return deleted_value
        # Итоговая сложность: O(1)

    def traversal(self):
        """Обход списка (возвращает элементы в виде списка)"""
        elements = []
        current = self.head
        while current:          # выполняется n раз
            elements.append(current.data)  # O(1) на шаг
            current = current.next        # O(1)
        return elements
        # Итоговая сложность: O(n)
