from typing import List, Set, Deque
from collections import deque
from graph_representation import AdjacencyListGraph


def bfs(graph: AdjacencyListGraph, start_node: int) -> List[int]:
    """
    Обход в ширину (BFS).
    Использует очередь. Находит кратчайшие пути в невзвешенном графе.

    Сложность:
        Временная: O(V + E).
        Пространственная: O(V) для хранения visited и очереди.
    """
    visited: Set[int] = set()
    queue: Deque[int] = deque([start_node])
    visited.add(start_node)
    result: List[int] = []

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def dfs_iterative(graph: AdjacencyListGraph, start_node: int) -> List[int]:
    """
    Обход в глубину (DFS) - итеративный подход.
    Использует стек.

    Сложность:
        Временная: O(V + E).
        Пространственная: O(V) для стека.
    """
    visited: Set[int] = set()
    stack: List[int] = [start_node]
    result: List[int] = []

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)
            result.append(current)

            # Добавляем соседей в стек в обратном порядке,
            # чтобы извлекать их в прямом
            neighbors = graph.get_neighbors(current)
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


def dfs_recursive(
    graph: AdjacencyListGraph,
    current: int,
    visited: Set[int],
    result: List[int]
) -> None:
    """
    Рекурсивный хелпер для DFS.
    Сложность: O(V + E).
    """
    visited.add(current)
    result.append(current)

    for neighbor in graph.get_neighbors(current):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)


# --- Практическая задача 1: Поиск компонент связности ---

def find_connected_components(graph: AdjacencyListGraph) -> List[List[int]]:
    """
    Находит все компоненты связности в неориентированном графе.

    Алгоритм:
    Проходим по всем вершинам. Если вершина не посещена, запускаем
    BFS/DFS и записываем весь обход как одну компоненту.

    Сложность: O(V + E).
    """
    visited: Set[int] = set()
    components: List[List[int]] = []

    for i in range(graph.num_vertices):
        if i not in visited:
            # Новая компонента
            component_nodes: List[int] = []

            # Локальный BFS/DFS для сбора компоненты
            queue: Deque[int] = deque([i])
            visited.add(i)

            while queue:
                node = queue.popleft()
                component_nodes.append(node)

                for neighbor in graph.get_neighbors(node):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            components.append(component_nodes)

    return components


# --- Практическая задача 2: Топологическая сортировка ---

def topological_sort(graph: AdjacencyListGraph) -> List[int]:
    """
    Топологическая сортировка (для ориентированных ациклических графов - DAG).
    Использует DFS. Вершина добавляется в результат,
    когда обработаны все её дети.
    В конце список переворачивается.

    Сложность: O(V + E).
    """
    visited: Set[int] = set()
    stack: List[int] = []  # Используем как список для результата

    # Внутренняя функция для рекурсии
    def dfs(u: int):
        visited.add(u)
        for v in graph.get_neighbors(u):
            if v not in visited:
                dfs(v)
        # Добавляем в стек после посещения всех потомков
        stack.append(u)

    for i in range(graph.num_vertices):
        if i not in visited:
            dfs(i)

    # Результат нужно развернуть (или считывать со стека с конца)
    return stack[::-1]
