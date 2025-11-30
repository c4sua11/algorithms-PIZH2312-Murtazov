import heapq
from collections import Counter
from typing import List, Tuple, Dict, Optional, NamedTuple


class Item(NamedTuple):
    """Представление предмета для задачи о рюкзаке."""
    value: int
    weight: int


class Node:
    """Узел дерева для кодирования Хаффмана."""
    def __init__(self, char: Optional[str], freq: int):
        self.char = char
        self.freq = freq
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

    def __lt__(self, other: 'Node') -> bool:
        return self.freq < other.freq


def interval_scheduling(intervals:
                        List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Задача о выборе заявок (Interval Scheduling).
    Выбирает максимальное количество непересекающихся интервалов.

    Стратегия: Выбирать интервал с самым ранним временем окончания.

    Сложность: O(N log N) из-за сортировки.
    """
    # Сортируем по времени окончания (второй элемент кортежа)
    sorted_intervals = sorted(intervals, key=lambda x: x[1])

    result = []
    last_end_time = -1

    for start, end in sorted_intervals:
        if start >= last_end_time:
            result.append((start, end))
            last_end_time = end

    return result


def fractional_knapsack(items: List[Item], capacity: int) -> float:
    """
    Задача о непрерывном (дробном) рюкзаке.
    Максимизирует стоимость, можно брать части предметов.

    Стратегия: Выбирать предметы с
    максимальной удельной стоимостью (value / weight).

    Сложность: O(N log N) из-за сортировки.
    """
    # Сортируем по удельной стоимости убыванию
    sorted_items = sorted(items, key=lambda x:
                          x.value / x.weight, reverse=True)

    total_value = 0.0
    current_capacity = capacity

    for item in sorted_items:
        if current_capacity == 0:
            break

        if item.weight <= current_capacity:
            # Берем предмет целиком
            current_capacity -= item.weight
            total_value += item.value
        else:
            # Берем часть предмета
            fraction = current_capacity / item.weight
            total_value += item.value * fraction
            current_capacity = 0

    return total_value


def huffman_coding(text: str) -> Dict[str, str]:
    """
    Алгоритм Хаффмана для сжатия данных.
    Строит оптимальные префиксные коды символов.

    Стратегия: Объединять два узла с наименьшей частотой.

    Сложность: O(N log N), где N - количество уникальных символов.
    """
    if not text:
        return {}

    # Подсчет частот
    frequency = Counter(text)
    heap: List[Node] = []  # Явно указываем тип для MyPy

    # Создаем начальные узлы и кладем в кучу
    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    # Строим дерево
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

    root = heap[0] if heap else None  # Обрабатываем случай пустого списка
    codes: Dict[str, str] = {}

    # Рекурсивный обход для генерации кодов
    def generate_codes(node: Optional[Node], current_code: str) -> None:
        if node is None:
            return

        # Если это лист (символ)
        if node.char is not None:
            # Если строка пустая, но у нас один символ, присваиваем "0"
            codes[node.char] = current_code if current_code else "0"
            return

        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root, "")
    return codes
