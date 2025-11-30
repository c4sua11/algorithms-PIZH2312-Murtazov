import matplotlib.pyplot as plt  # type: ignore
import networkx as nx  # type: ignore
import timeit
import random
import string
import heapq
from collections import Counter
from typing import Optional, List  # Добавили List

# Импортируем класс Node
from greedy_algorithms import Node


def build_huffman_tree_root(text: str) -> Optional[Node]:
    """
    Вспомогательная функция, которая строит дерево Хаффмана
    и возвращает КОРЕНЬ (для визуализации).
    """
    if not text:
        return None

    frequency = Counter(text)

    # ИСПРАВЛЕНИЕ 2: Явная аннотация типа для кучи
    heap: List[Node] = []

    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        # Создаем внутренний узел (char=None)
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

    return heap[0]


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Рекурсивно добавляет узлы и ребра в граф networkx.
    """
    if node is None:
        return

    # Уникальный идентификатор для networkx
    node_id = id(node)

    label = f"'{node.char}'\n{node.freq}" if node.char else f"{node.freq}"

    graph.add_node(node_id, label=label, pos=(x, y))

    if node.left:
        left_x = x - 1 / (2 ** layer)
        left_y = y - 1
        graph.add_edge(node_id, id(node.left))
        add_edges(graph, node.left, pos, x=left_x, y=left_y, layer=layer + 1)

    if node.right:
        right_x = x + 1 / (2 ** layer)
        right_y = y - 1
        graph.add_edge(node_id, id(node.right))
        add_edges(graph, node.right,
                  pos, x=right_x, y=right_y, layer=layer + 1)


def draw_huffman_tree():
    """Визуализация дерева Хаффмана."""
    text = "abracadabra"
    root = build_huffman_tree_root(text)

    if not root:
        print("Text is empty.")
        return

    G = nx.DiGraph()
    add_edges(G, root, None)

    pos = nx.get_node_attributes(G, 'pos')
    labels = nx.get_node_attributes(G, 'label')

    plt.figure(figsize=(10, 6))
    plt.title(f"Дерево Хаффмана для строки: '{text}'")

    nx.draw(G, pos, labels=labels, with_labels=True,
            node_size=2000, node_color="lightblue",
            font_size=9, font_weight="bold", arrows=False)

    plt.savefig('huffman_tree.png')
    print("График дерева сохранен в 'huffman_tree.png'")
    # plt.show() # Можно закомментировать, если мешает всплывающее окно


def plot_performance():
    """Построение графика зависимости времени."""
    from greedy_algorithms import huffman_coding

    sizes = [1000, 5000, 10000, 20000, 50000, 100000]
    times: List[float] = []  # Аннотация типа для списка времен

    print("Замер производительности...")
    for size in sizes:
        text = ''.join(random.choices(string.ascii_letters, k=size))
        t = timeit.timeit(lambda: huffman_coding(text), number=5) / 5
        times.append(t)
        print(f"Size: {size}, Time: {t:.5f}s")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, 'o-',
             color='green', label='Huffman Coding O(N log N)')

    plt.title("Зависимость времени выполнения от длины текста")
    plt.xlabel("Количество символов (N)")
    plt.ylabel("Время выполнения (сек)")
    plt.grid(True)
    plt.legend()

    plt.savefig('huffman_performance.png')
    print("График производительности сохранен в 'huffman_performance.png'")
    # plt.show()


if __name__ == "__main__":
    draw_huffman_tree()
    plot_performance()
