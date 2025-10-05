import timeit
from collections import deque
from linked_list import LinkedList


def test_list_insert_front(n=1000):
    """Вставка в начало списка"""
    data = []
    for i in range(n):
        data.insert(0, i)  # O(n) на каждую вставку


def test_linkedlist_insert_front(n=1000):
    """Вставка в начало связного списка"""
    ll = LinkedList()
    for i in range(n):
        ll.insert_at_start(i)  # O(1) на каждую вставку


def test_list_pop_front(n=1000):
    """Удаление из начала списка"""
    data = [i for i in range(n)]
    for _ in range(n):
        data.pop(0)  # O(n) на каждое удаление


def test_deque_popleft(n=1000):
    """Удаление из начала очереди на deque"""
    d = deque(range(n))
    for _ in range(n):
        d.popleft()  # O(1) на каждое удаление


if __name__ == "__main__":
    n = 1000
    print("=== Вставка в начало ===")
    print("list.insert(0, x):", timeit.timeit(
        lambda: test_list_insert_front(n), number=1))
    print("LinkedList.insert_at_start:", timeit.timeit(
        lambda: test_linkedlist_insert_front(n), number=1))

    print(
        "\n=== Удаление из начала ===")
    print("list.pop(0):", timeit.timeit(
        lambda: test_list_pop_front(n), number=1))
    print("deque.popleft():", timeit.timeit(
        lambda: test_deque_popleft(n), number=1))
