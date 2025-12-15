import heapq
from typing import List, Dict, Tuple
from graph_representation import AdjacencyListGraph


def dijkstra(graph: AdjacencyListGraph, start_node: int) -> Dict[int, int]:
    """
    Алгоритм Дейкстры для поиска кратчайших путей от стартовой вершины.
    Работает только с неотрицательными весами.

    Сложность:
        Временная: O(E * log V) при использовании бинарной кучи.
        Пространственная: O(V + E).
    """
    # Инициализация расстояний бесконечностью
    distances: Dict[int, int] = {
        v: float('inf') for v in range(graph.num_vertices)
    }
    distances[start_node] = 0

    # Очередь с приоритетом хранит кортежи (расстояние, вершина)
    priority_queue: List[Tuple[int, int]] = [(0, start_node)]

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)

        # Если нашли более короткий путь ранее, пропускаем
        if current_dist > distances[current_node]:
            continue

        # Проходим по соседям
        for neighbor, weight in graph.get_edges_with_weights(current_node):
            distance = current_dist + weight

            # Релаксация ребра
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # Отфильтруем недостижимые вершины (по желанию)
    return {k: v for k, v in distances.items() if v != float('inf')}
