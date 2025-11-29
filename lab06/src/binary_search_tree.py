from typing import Optional


class TreeNode:
    """
    Узел бинарного дерева поиска.
    """

    def __init__(self, key: int) -> None:
        self.val: int = key
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


class BinarySearchTree:
    """
    Класс, реализующий бинарное дерево поиска (BST).
    """

    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None

    def insert(self, key: int) -> None:
        """
        Вставляет значение в дерево.

        Временная сложность:
            - Средняя: O(log N)
            - Худшая: O(N) (вырожденное дерево)
        """
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node: TreeNode, key: int) -> None:
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key: int) -> Optional[TreeNode]:
        """
        Ищет узел с заданным значением.

        Временная сложность:
            - Средняя: O(log N)
            - Худшая: O(N)
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node: Optional[TreeNode],
                          key: int) -> Optional[TreeNode]:
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def find_min(self, node: TreeNode) -> TreeNode:
        """
        Находит узел с минимальным значением в поддереве.

        Сложность: O(H), где H - высота дерева.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, key: int) -> None:
        """
        Удаляет значение из дерева.

        Временная сложность:
            - Средняя: O(log N)
            - Худшая: O(N)
        """
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node: Optional[TreeNode],
                          key: int) -> Optional[TreeNode]:
        if node is None:
            return node

        if key < node.val:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.val:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Случай 1: Нет детей или один ребенок
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Случай 2: Два ребенка
            # Находим минимальный элемент в правом поддереве
            temp = self.find_min(node.right)
            node.val = temp.val
            # Удаляем этот минимальный элемент
            node.right = self._delete_recursive(node.right, temp.val)

        return node

    def is_valid_bst(self) -> bool:
        """
        Проверяет, является ли дерево корректным BST.

        Сложность: O(N), так как посещаем каждый узел.
        """
        return self._is_valid_helper(self.root, float('-inf'), float('inf'))

    def _is_valid_helper(self, node: Optional[TreeNode],
                         min_val: float, max_val: float) -> bool:
        if node is None:
            return True

        if not (min_val < node.val < max_val):
            return False

        return (self._is_valid_helper(node.left, min_val, node.val) and
                self._is_valid_helper(node.right, node.val, max_val))
