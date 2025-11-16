"""
Модуль для бенчмаркинга производительности хеш-таблиц.
Измеряет время вставки, поиска и удаления элементов
для разных реализаций хеш-таблиц при различных коэффициентах заполнения.
"""

import time
from typing import Callable, Tuple, Union
from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableOpenAddressing

# Тип для фабрики таблицы — возвращает либо Chaining, либо Open Addressing
TableType = Union[HashTableChaining, HashTableOpenAddressing]


def benchmark_table(
    table_factory: Callable[[], TableType],
    n_ops: int = 1000,
    load_factor: float = 0.5
) -> Tuple[float, float, float]:
    """
    Измеряет время выполнения трёх основных операций:
    - вставка n_ops новых элементов
    - поиск n_ops элементов
    - удаление n_ops элементов

    :param table_factory: callable, возвращающий новый экземпляр таблицы
    :param n_ops: количество операций для замера
    :param load_factor: коэффициент заполнения таблицы перед замерами
    :return: кортеж (время_вставки, время_поиска, время_удаления) в секундах
    """
    tbl = table_factory()

    # Предварительно заполняем таблицу до приблизительного load_factor
    capacity = tbl.size
    prefill_count = int(capacity * load_factor)
    for i in range(prefill_count):
        tbl.insert(f"pre{i}", i)

    # Генерируем ключи для тестирования
    test_keys = [f"key_{i}" for i in range(n_ops)]

    # Вставка
    start = time.perf_counter()
    for i, k in enumerate(test_keys):
        tbl.insert(k, i)
    t_insert = time.perf_counter() - start

    # Поиск
    start = time.perf_counter()
    for k in test_keys:
        tbl.search(k)
    t_search = time.perf_counter() - start

    # Удаление
    start = time.perf_counter()
    for k in test_keys:
        tbl.delete(k)
    t_delete = time.perf_counter() - start

    return t_insert, t_search, t_delete


if __name__ == "__main__":
    # Коэффициенты заполнения, для которых будем тестировать
    load_factors = [0.1, 0.3, 0.5, 0.7, 0.9]

    print("=== Результаты бенчмарка ===")

    for factor in load_factors:
        print(f"\nКоэффициент заполнения: {factor}")

        # Тестируем Chaining
        t_ins, t_sch, t_del = benchmark_table(
            lambda: HashTableChaining(size=1009),
            n_ops=500,
            load_factor=factor
        )
        print(f"  Chaining (вставка, поиск, "
              f"удаление): {t_ins:.6f}, {t_sch:.6f}, {t_del:.6f}")

        # Тестируем Open Addressing с линейным пробированием
        try:
            t_ins, t_sch, t_del = benchmark_table(
                lambda: HashTableOpenAddressing(size=1009),
                n_ops=500,
                load_factor=factor
            )
            print(f"  Open Addressing (Linear) "
                  f"(вст., поис., уд.): {t_ins:.6f}, {t_sch:.6f}, {t_del:.6f}")
        except Exception as e:
            print(f"  Open Addressing (Linear) — ошибка при α={factor}: {e}")
