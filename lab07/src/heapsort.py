from typing import List
from asa_heap import MinHeap


def heapsort(array: List[int]) -> List[int]:
    """
    Сортирует массив с использованием MinHeap.
    Примечание: так как используется MinHeap, мы извлекаем элементы
    от наименьшего к наибольшему, получая отсортированный массив.

    Временная сложность:
        - Построение кучи: O(N)
        - Извлечение N элементов: N * O(log N)
        - Итого: O(N log N)
    """
    heap = MinHeap()
    heap.build_heap(array)  # Эффективное построение за O(N)

    sorted_array = []
    while True:
        val = heap.extract()
        if val is None:
            break
        sorted_array.append(val)

    return sorted_array
