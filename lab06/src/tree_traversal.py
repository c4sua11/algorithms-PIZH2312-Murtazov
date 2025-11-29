from typing import List, Optional
from binary_search_tree import TreeNode


class TreeTraversal:
    """
    Класс для реализации алгоритмов обхода дерева.
    """

    @staticmethod
    def in_order(node: Optional[TreeNode]) -> List[int]:
        """
        Центрированный обход (Left -> Root -> Right).
        Рекурсивная версия.

        Сложность: O(N).
        """
        res = []
        if node:
            res = TreeTraversal.in_order(node.left)
            res.append(node.val)
            res = res + TreeTraversal.in_order(node.right)
        return res

    @staticmethod
    def pre_order(node: Optional[TreeNode]) -> List[int]:
        """
        Прямой обход (Root -> Left -> Right).
        Рекурсивная версия.

        Сложность: O(N).
        """
        res = []
        if node:
            res.append(node.val)
            res = res + TreeTraversal.pre_order(node.left)
            res = res + TreeTraversal.pre_order(node.right)
        return res

    @staticmethod
    def post_order(node: Optional[TreeNode]) -> List[int]:
        """
        Обратный обход (Left -> Right -> Root).
        Рекурсивная версия.

        Сложность: O(N).
        """
        res = []
        if node:
            res = TreeTraversal.post_order(node.left)
            res = res + TreeTraversal.post_order(node.right)
            res.append(node.val)
        return res

    @staticmethod
    def in_order_iterative(root: Optional[TreeNode]) -> List[int]:
        """
        Центрированный обход с использованием стека.

        Сложность: O(N).
        """
        res = []
        stack: List[TreeNode] = []
        curr = root

        while curr is not None or len(stack) > 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res
