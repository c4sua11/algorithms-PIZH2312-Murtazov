from typing import List, Tuple


class AdjacencyMatrixGraph:
    """
    Представление графа в виде матрицы смежности.

    Потребление памяти: O(V^2), где V - количество вершин.
    Эффективен для плотных графов и быстрой проверки наличия ребра.
    """

    def __init__(self, num_vertices: int, directed: bool = False) -> None:
        self.num_vertices = num_vertices
        self.directed = directed
        # Инициализация матрицы нулями
        self.matrix: List[List[int]] = [
            [0] * num_vertices for _ in range(num_vertices)
        ]

    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """
        Добавление ребра.
        Сложность: O(1) - прямой доступ по индексу.
        """
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.matrix[u][v] = weight
            if not self.directed:
                self.matrix[v][u] = weight

    def remove_edge(self, u: int, v: int) -> None:
        """
        Удаление ребра.
        Сложность: O(1).
        """
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.matrix[u][v] = 0
            if not self.directed:
                self.matrix[v][u] = 0

    def get_neighbors(self, u: int) -> List[int]:
        """
        Получение списка соседей вершины.
        Сложность: O(V) - необходимо пройти весь ряд матрицы.
        """
        neighbors: List[int] = []
        if 0 <= u < self.num_vertices:
            for v in range(self.num_vertices):
                if self.matrix[u][v] != 0:
                    neighbors.append(v)
        return neighbors


class AdjacencyListGraph:
    """
    Представление графа в виде списка смежности.

    Потребление памяти: O(V + E), где V - вершины, E - ребра.
    Эффективен для разреженных графов и итерации по соседям.
    """

    def __init__(self, num_vertices: int, directed: bool = False) -> None:
        self.num_vertices = num_vertices
        self.directed = directed
        # Список списков кортежей (сосед, вес)
        self.adj_list: List[List[Tuple[int, int]]] = [
            [] for _ in range(num_vertices)
        ]

    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """
        Добавление ребра.
        Сложность: O(1) - добавление в конец списка (амортизированное).
        """
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.adj_list[u].append((v, weight))
            if not self.directed:
                self.adj_list[v].append((u, weight))

    def remove_edge(self, u: int, v: int) -> None:
        """
        Удаление ребра.
        Сложность: O(K), где K - степень вершины (количество соседей).
        В худшем случае O(V).
        """
        if 0 <= u < self.num_vertices:
            # Пересоздаем список без удаляемого ребра
            self.adj_list[u] = [
                (node, w) for node, w in self.adj_list[u] if node != v
            ]

        if not self.directed and 0 <= v < self.num_vertices:
            self.adj_list[v] = [
                (node, w) for node, w in self.adj_list[v] if node != u
            ]

    def get_neighbors(self, u: int) -> List[int]:
        """
        Получение списка соседей вершины.
        Сложность: O(K), где K - количество соседей (копирование списка).
        """
        if 0 <= u < self.num_vertices:
            return [node for node, _ in self.adj_list[u]]
        return []

    def get_edges_with_weights(self, u: int) -> List[Tuple[int, int]]:
        """Вспомогательный метод для получения соседей с весами."""
        if 0 <= u < self.num_vertices:
            return self.adj_list[u]
        return []
