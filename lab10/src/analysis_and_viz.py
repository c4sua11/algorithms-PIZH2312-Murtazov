import timeit
import random
import matplotlib.pyplot as plt

from graph_representation import AdjacencyMatrixGraph, AdjacencyListGraph
from graph_traversal import bfs, find_connected_components, topological_sort


def generate_random_graph_data(num_vertices: int, density: float = 0.3):
    """Генерация списка ребер для графа."""
    edges = []
    # Максимальное кол-во ребер в ориентированном графе V*(V-1)
    # Для теста генерируем случайные
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and random.random() < density:
                edges.append((i, j))
    return edges


def measure_performance():
    sizes = [50, 100, 200, 300, 400]
    density = 0.2  # Разреженный граф

    times_matrix_creation = []
    times_list_creation = []
    times_matrix_bfs = []  # BFS для матрицы реализуем "на лету" или адаптируем
    times_list_bfs = []

    print(f"Запуск замеров (плотность графа {density})...")

    for n in sizes:
        edges = generate_random_graph_data(n, density)

        # 1. Замер создания AdjacencyMatrixGraph
        def create_matrix():
            g = AdjacencyMatrixGraph(n)
            for u, v in edges:
                g.add_edge(u, v)
            return g

        t_mat = timeit.timeit(create_matrix, number=10)
        times_matrix_creation.append(t_mat / 10)

        # 2. Замер создания AdjacencyListGraph
        def create_list():
            g = AdjacencyListGraph(n)
            for u, v in edges:
                g.add_edge(u, v)
            return g

        t_list = timeit.timeit(create_list, number=10)
        times_list_creation.append(t_list / 10)

        # Подготовка графов для замера обхода
        g_list = create_list()
        # Для чистоты эксперимента нужно реализовать BFS для матрицы,
        # но в рамках лабы часто сравнивают просто операции.
        # Здесь замерим BFS на списке как базовую метрику масштабируемости.

        t_bfs = timeit.timeit(lambda: bfs(g_list, 0), number=10)
        times_list_bfs.append(t_bfs / 10)

    # Визуализация 1: Создание графа
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, times_matrix_creation, 'o-', label='Matrix Creation')
    plt.plot(sizes, times_list_creation, 'x-', label='List Creation')
    plt.xlabel('Количество вершин (V)')
    plt.ylabel('Время (сек)')
    plt.title('Сравнение времени создания представлений графа')
    plt.legend()
    plt.grid(True)
    plt.savefig('graph_creation_benchmark.png')
    print("График создания сохранен: graph_creation_benchmark.png")

    # Визуализация 2: BFS масштабируемость
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, times_list_bfs,
             's-', color='green', label='BFS (Adj List)')
    plt.xlabel('Количество вершин (V)')
    plt.ylabel('Время (сек)')
    plt.title('Масштабируемость BFS от размера графа')
    plt.legend()
    plt.grid(True)
    plt.savefig('bfs_scalability.png')
    print("График BFS сохранен: bfs_scalability.png")

    # plt.show() # Раскомментировать, если запускаете локально с GUI


if __name__ == "__main__":
    measure_performance()

    # Демонстрация работы топологической сортировки
    print("\n--- Тест Топологической сортировки (одевание) ---")
    # Граф "Одевание":
    # 0:Трусы -> 1:Брюки, 0:Трусы -> 2:Туфли
    # 3:Носки -> 2:Туфли
    # 1:Брюки -> 2:Туфли (спорно, но пусть будет)
    # 4:Рубашка -> 5:Галстук -> 6:Пиджак
    dag = AdjacencyListGraph(7, directed=True)
    dag.add_edge(0, 1)  # трусы -> брюки
    dag.add_edge(0, 2)  # трусы -> туфли
    dag.add_edge(3, 2)  # носки -> туфли
    dag.add_edge(1, 2)  # брюки -> туфли
    dag.add_edge(4, 5)  # рубашка -> галстук
    dag.add_edge(5, 6)  # галстук -> пиджак

    sorted_nodes = topological_sort(dag)
    print(f"Порядок действий: {sorted_nodes}")

    # Демонстрация компонент связности
    print("\n--- Тест Компонент связности ---")
    g_conn = AdjacencyListGraph(6)  # 0-1-2, 3-4, 5
    g_conn.add_edge(0, 1)
    g_conn.add_edge(1, 2)
    g_conn.add_edge(3, 4)
    comps = find_connected_components(g_conn)
    print(f"Компоненты: {comps}")
