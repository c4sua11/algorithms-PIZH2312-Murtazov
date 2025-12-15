from typing import List


# =============================================================================
# 1. ПРЕФИКС-ФУНКЦИЯ И KMP
# =============================================================================

def compute_prefix_function(s: str) -> List[int]:
    """
    Вычисляет префикс-функцию для строки s.
    pi[i] - длина наибольшего собственного префикса подстроки s[0..i],
    который также является суффиксом этой подстроки.

    Сложность:
        Временная: O(n)
        Пространственная: O(n)
    """
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def kmp_search(text: str, pattern: str) -> List[int]:
    """
    Алгоритм Кнута-Морриса-Пратта (KMP) для поиска всех вхождений
    pattern в text.

    Сложность:
        Временная: O(N + M), где N - длина текста, M - длина паттерна.
        Пространственная: O(M) для массива pi.
    """
    if not pattern:
        return []

    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)

    matches = []
    j = 0  # индекс в pattern

    for i in range(n):  # индекс в text
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i - m + 1)
            j = pi[j - 1]

    return matches


# =============================================================================
# 2. Z-ФУНКЦИЯ И ПОИСК С ЕЕ ПОМОЩЬЮ
# =============================================================================

def compute_z_function(s: str) -> List[int]:
    """
    Вычисляет Z-функцию для строки s.
    z[i] - длина наибольшего общего префикса строки s и ее суффикса s[i..].

    Сложность:
        Временная: O(n)
        Пространственная: O(n)
    """
    n = len(s)
    z = [0] * n
    l, r = 0, 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z


def z_function_search(text: str, pattern: str) -> List[int]:
    """
    Поиск подстроки с использованием Z-функции.
    Использует конкатенацию: P + '#' + T.

    Сложность:
        Временная: O(N + M).
        Пространственная: O(N + M) для создания новой строки и массива Z.
    """
    if not pattern:
        return []

    # Специальный символ, которого нет в тексте и паттерне
    concat = pattern + "#" + text
    z = compute_z_function(concat)

    matches = []
    p_len = len(pattern)

    # Проходим по Z-массиву начиная с области текста
    # (индексы от p_len + 1 до конца)
    for i in range(p_len + 1, len(concat)):
        if z[i] == p_len:
            # Индекс в исходном тексте = i - (длина паттерна + 1)
            matches.append(i - p_len - 1)

    return matches


# =============================================================================
# 3. ДОПОЛНИТЕЛЬНЫЙ АЛГОРИТМ: РАБИН-КАРП
# =============================================================================

def rabin_karp_search(text: str, pattern: str) -> List[int]:
    """
    Алгоритм Рабина-Карпа с использованием полиномиального хеширования.

    Сложность:
        В среднем: O(N + M).
        В худшем (много коллизий): O(N * M).
    """
    if not pattern or len(pattern) > len(text):
        return []

    n, m = len(text), len(pattern)
    alphabet_size = 256
    modulus = 101  # Простое число для модуля

    p_hash = 0
    t_hash = 0
    h = 1

    # Значение h = pow(alphabet_size, m-1) % modulus
    for i in range(m - 1):
        h = (h * alphabet_size) % modulus

    # Вычисляем хеш паттерна и первого окна текста
    for i in range(m):
        p_hash = (alphabet_size * p_hash + ord(pattern[i])) % modulus
        t_hash = (alphabet_size * t_hash + ord(text[i])) % modulus

    matches = []

    # Проходим по тексту
    for i in range(n - m + 1):
        # Если хеши совпадают, проверяем символы (защита от коллизий)
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                matches.append(i)

        # Вычисляем хеш для следующего окна
        if i < n - m:
            t_hash = (alphabet_size * (t_hash - ord(text[i]) * h) +
                      ord(text[i + m])) % modulus

            # Если получили отрицательное значение
            if t_hash < 0:
                t_hash += modulus

    return matches


# =============================================================================
# 4. ПРАКТИЧЕСКИЕ ЗАДАЧИ
# =============================================================================

def is_cyclic_shift(s1: str, s2: str) -> bool:
    """
    Проверяет, является ли строка s2 циклическим сдвигом s1.
    Пример: 'abcde' и 'cdeab' -> True.

    Решение:
    Если длины равны, то s2 должна быть подстрокой s1 + s1.
    Использует KMP (или любой быстрый поиск) под капотом.

    Сложность: O(N).
    """
    if len(s1) != len(s2):
        return False

    # s1 + s1 содержит все циклические сдвиги s1
    doubled_s1 = s1 + s1

    # Используем наш KMP для поиска
    matches = kmp_search(doubled_s1, s2)

    return len(matches) > 0
