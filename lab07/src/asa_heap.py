from typing import List, Optional


class MinHeap:
    """
    Реализация структуры данных Min-Heap (Минимальная куча) на основе массива.
    """

    def __init__(self) -> None:
        """Инициализация пустой кучи."""
        self.heap: List[int] = []

    def _parent(self, index: int) -> int:
        """Возвращает индекс родителя."""
        return (index - 1) // 2

    def _left_child(self, index: int) -> int:
        """Возвращает индекс левого потомка."""
        return 2 * index + 1

    def _right_child(self, index: int) -> int:
        """Возвращает индекс правого потомка."""
        return 2 * index + 2

    def _swap(self, i: int, j: int) -> None:
        """Меняет местами элементы по индексам i и j."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, index: int) -> None:
        """
        Поднимает элемент вверх по дереву для восстановления свойств кучи.

        Временная сложность: O(log N) в худшем случае проход от листа до корня.
        """
        while index > 0 and self.heap[index] < self.heap[self._parent(index)]:
            parent_idx = self._parent(index)
            self._swap(index, parent_idx)
            index = parent_idx

    def _sift_down(self, index: int) -> None:
        """
        Опускает элемент вниз по дереву для восстановления свойств кучи.

        Временная сложность: O(log N) - высота дерева.
        """
        size = len(self.heap)
        while True:
            left = self._left_child(index)
            right = self._right_child(index)
            smallest = index

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def insert(self, value: int) -> None:
        """
        Вставляет элемент в кучу.

        Временная сложность: O(log N).
        """
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract(self) -> Optional[int]:
        """
        Удаляет и возвращает минимальный элемент (корень).

        Временная сложность: O(log N).
        """
        if not self.heap:
            return None

        min_val = self.heap[0]
        last_val = self.heap.pop()

        if self.heap:
            self.heap[0] = last_val
            self._sift_down(0)

        return min_val

    def peek(self) -> Optional[int]:
        """
        Возвращает минимальный элемент без удаления.

        Временная сложность: O(1).
        """
        return self.heap[0] if self.heap else None

    def build_heap(self, array: List[int]) -> None:
        """
        Строит кучу из произвольного массива.
        Использует алгоритм Флойда (просеивание вниз).

        Временная сложность: O(N).
        """
        self.heap = array[:]
        # Начинаем с последнего элемента, у которого есть потомки
        start_idx = (len(self.heap) // 2) - 1
        for i in range(start_idx, -1, -1):
            self._sift_down(i)
