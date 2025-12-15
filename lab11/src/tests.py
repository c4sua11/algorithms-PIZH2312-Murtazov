import unittest
from string_algorithms import (
    compute_prefix_function,
    compute_z_function,
    kmp_search,
    z_function_search,
    rabin_karp_search,
    is_cyclic_shift
)


class TestStringAlgorithms(unittest.TestCase):

    def setUp(self):
        self.text = "ababcabcabababd"
        self.pattern = "ababd"
        # Индекс вхождения: text заканчивается на ababd, длина 15, паттерн 5.
        # Индекс = 10.

    def test_prefix_function(self):
        s = "ababa"
        # pi: a->0, ab->0, aba->1, abab->2, ababa->3
        expected = [0, 0, 1, 2, 3]
        self.assertEqual(compute_prefix_function(s), expected)

    def test_z_function(self):
        s = "abacaba"
        # z: [0, 0, 1, 0, 3, 0, 1]
        # (для первого элемента Z-функция обычно не определена или равна 0/len)
        expected = [0, 0, 1, 0, 3, 0, 1]
        self.assertEqual(compute_z_function(s), expected)

    def test_kmp_search(self):
        # Обычный поиск
        self.assertEqual(kmp_search(self.text, self.pattern), [10])
        # Множественные вхождения
        self.assertEqual(kmp_search("aaaaa", "aa"), [0, 1, 2, 3])
        # Нет вхождений
        self.assertEqual(kmp_search("abcdef", "xyz"), [])

    def test_z_search(self):
        self.assertEqual(z_function_search(self.text, self.pattern), [10])
        self.assertEqual(z_function_search("aaaaa", "aa"), [0, 1, 2, 3])
        self.assertEqual(z_function_search("abcdef", "xyz"), [])

    def test_rabin_karp_search(self):
        self.assertEqual(rabin_karp_search(self.text, self.pattern), [10])
        self.assertEqual(rabin_karp_search("aaaaa", "aa"), [0, 1, 2, 3])

    def test_cyclic_shift(self):
        self.assertTrue(is_cyclic_shift("abcde", "cdeab"))
        self.assertTrue(is_cyclic_shift("abcde", "abcde"))
        self.assertFalse(is_cyclic_shift("abcde", "abced"))
        self.assertFalse(is_cyclic_shift("abc", "def"))


if __name__ == "__main__":
    unittest.main()
