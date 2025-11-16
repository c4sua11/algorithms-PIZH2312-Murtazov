"""
Набор простых юнит-тестов для проверки работоспособности
реализованных хеш-таблиц. Тесты не используют pytest, можно запускать напрямую.
Каждый тест возвращает True при успехе, иначе — False.
"""

from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableOpenAddressing


def test_chaining_insert_search() -> bool:
    """
    Тестирует вставку и поиск в хеш-таблице с цепочками.
    """
    table = HashTableChaining(size=5)
    table.insert("key1", 100)
    table.insert("key2", 200)
    table.insert("key3", 300)

    assert table.search("key1") == 100
    assert table.search("key2") == 200
    assert table.search("key3") == 300
    assert table.search("nonexistent") is None

    return True


def test_chaining_delete() -> bool:
    """
    Тестирует удаление элемента из хеш-таблицы с цепочками.
    """
    table = HashTableChaining(size=3)
    table.insert("delete_me", 42)
    assert table.search("delete_me") == 42

    success = table.delete("delete_me")
    assert success is True
    assert table.search("delete_me") is None

    # Попытка удалить несуществующий ключ
    fail = table.delete("no_such_key")
    assert fail is False

    return True


def test_open_addressing_linear_probe() -> bool:
    """
    Тестирует вставку, поиск и удаление в хеш-таблице с линейным пробированием.
    """
    table = HashTableOpenAddressing(size=5)
    table.insert("a", 1, method="linear")
    table.insert("b", 2, method="linear")
    table.insert("c", 3, method="linear")

    assert table.search("a", method="linear") == 1
    assert table.search("b", method="linear") == 2
    assert table.search("c", method="linear") == 3

    # Удаление
    success = table.delete("b", method="linear")
    assert success is True
    assert table.search("b", method="linear") is None

    return True


def test_open_addressing_double_hashing() -> bool:
    """
    Тестирует двойное хеширование.
    """
    table = HashTableOpenAddressing(size=7)
    table.insert("first", 10, method="double")
    table.insert("second", 20, method="double")
    table.insert("third", 30, method="double")

    assert table.search("first", method="double") == 10
    assert table.search("second", method="double") == 20
    assert table.search("third", method="double") == 30

    # Удаление
    removed = table.delete("second", method="double")
    assert removed is True
    assert table.search("second", method="double") is None

    return True


def test_chaining_collision_handling() -> bool:
    """
    Проверяет, как таблица с цепочками справляется с коллизиями.
    """
    table = HashTableChaining(size=2)
    table.insert("key1", 1)
    table.insert("key2", 2)
    table.insert("key3", 3)

    assert table.search("key1") == 1
    assert table.search("key2") == 2
    assert table.search("key3") == 3

    # Удаление из середины цепочки
    table.delete("key2")
    assert table.search("key2") is None
    assert table.search("key1") == 1
    assert table.search("key3") == 3

    return True


if __name__ == "__main__":
    all_tests = [
        ("Chaining Insert/Search", test_chaining_insert_search),
        ("Chaining Delete", test_chaining_delete),
        ("Open Addressing Linear", test_open_addressing_linear_probe),
        ("Open Addressing Double Hashing",
         test_open_addressing_double_hashing),
        ("Chaining Collision Handling", test_chaining_collision_handling),
    ]

    passed = 0
    total = len(all_tests)

    for test_name, test_func in all_tests:
        try:
            result = test_func()
            if result:
                print(f"[✓] {test_name}: Пройден")
                passed += 1
            else:
                print(f"[✗] {test_name}: Провал (функция вернула False)")
        except AssertionError as e:
            print(f"[✗] {test_name}: Ошибка утверждения -> {e}")
        except Exception as e:
            print(f"[✗] {test_name}: Исключение -> {e}")

    print(f"\nРезультат: {passed}/{total} тестов пройдено.")
