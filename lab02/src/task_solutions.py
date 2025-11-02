from collections import deque


def check_brackets(expression: str) -> bool:
    """
    Проверка сбалансированности скобок.
    Используется стек (list).
    Сложность: O(n).
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack


def print_queue_simulation(tasks: list[str]) -> None:
    """
    Симуляция очереди печати.
    Используется deque.
    Сложность: O(n).
    """
    queue = deque(tasks)
    while queue:
        current_task = queue.popleft()
        print(f"Печатается: {current_task}")


def is_palindrome(sequence: str) -> bool:
    """
    Проверка, является ли строка палиндромом.
    Используется deque.
    Сложность: O(n).
    """
    d = deque(sequence)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


if __name__ == "__main__":
    # Тесты для скобок
    print("Сбалансированные скобки:", check_brackets("{[()]}"))
    print("Несбалансированные скобки:", check_brackets("{[(])}"))

    # Тест очереди печати
    print("\nСимуляция печати:")
    print_queue_simulation(["Документ1", "Документ2", "Документ3"])

    # Тест палиндрома
    print("\nПроверка палиндромов:")
    print("level ->", is_palindrome("level"))
    print("python ->", is_palindrome("python"))
