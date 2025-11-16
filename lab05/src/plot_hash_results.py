"""
Эксперимент для сравнения производительности хеш-таблиц и хеш-функций.
Измеряет время вставки и поиск,
строит графики зависимости от коэффициента заполнения.
Строит гистограммы распределения коллизий для разных хеш-функций.
"""

import random
import string
import time
import matplotlib.pyplot as plt
from typing import Callable, List

from hash_functions import simple_hash, polynomial_hash, djb2_hash
from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableOpenAddressing

NUM_KEYS = 1000
TABLE_SIZE = 1009  # простое число для лучшего распределения
FILL_FACTORS = [0.1, 0.3, 0.5, 0.7, 0.9]


def generate_keys(num_keys: int, length: int = 6) -> List[str]:
    """Генерация случайных строковых ключей."""
    # Используем фиксированный seed для воспроизводимости
    random.seed(42)
    return [''.join(random.choices(string.ascii_lowercase, k=length))
            for _ in range(num_keys)]


def measure_time_chaining(keys: List[str], fill_factor: float) -> float:
    """Измеряет среднее время вставки в таблицу с цепочками."""
    size = int(TABLE_SIZE / fill_factor)
    ht = HashTableChaining(size=size, hash_func=simple_hash)
    start = time.time()
    for key in keys[:int(len(keys) * fill_factor)]:
        ht.insert(key, key)
    return time.time() - start


def measure_time_open_addressing(keys: List[str], method:
                                 str, fill_factor: float) -> float:
    """Измеряет среднее время вставки в таблицу с открытой адресацией."""
    size = int(TABLE_SIZE / fill_factor)
    ht = HashTableOpenAddressing(size=size)
    start = time.time()
    for key in keys[:int(len(keys) * fill_factor)]:
        ht.insert(key, key, method=method)
    return time.time() - start


def measure_search_time_chaining(keys: List[str], fill_factor: float,
                                 hash_func: Callable[[str,
                                                      int], int]) -> float:
    """Измеряет время поиска всех ключей в таблице с цепочками."""
    size = int(TABLE_SIZE / fill_factor)
    ht = HashTableChaining(size=size, hash_func=hash_func)
    # Вставляем только нужное количество ключей
    subset_keys = keys[:int(len(keys) * fill_factor)]
    for key in subset_keys:
        ht.insert(key, key)

    start = time.time()
    for key in subset_keys:
        _ = ht.search(key)
    return time.time() - start


def collisions_chaining(keys: List[str], hash_func:
                        Callable[[str, int], int]) -> List[int]:
    """Подсчёт распределения цепочек (коллизий) для таблицы с цепочками."""
    ht = HashTableChaining(size=TABLE_SIZE, hash_func=hash_func)
    for key in keys:
        ht.insert(key, key)
    return ht.get_chain_lengths()


if __name__ == "__main__":
    keys = generate_keys(NUM_KEYS)

    # График времени вставки для разных методов
    times_chaining, times_linear, times_double = [], [], []

    for fill in FILL_FACTORS:
        t_chain = measure_time_chaining(keys, fill)
        t_linear = measure_time_open_addressing(keys, "linear", fill)
        t_double = measure_time_open_addressing(keys, "double", fill)

        times_chaining.append(t_chain)
        times_linear.append(t_linear)
        times_double.append(t_double)

    plt.figure(figsize=(10, 6))
    plt.plot(FILL_FACTORS, times_chaining,
             marker='o', label='Chaining (Simple Hash)')
    plt.plot(FILL_FACTORS, times_linear,
             marker='s', label='Open Addressing (Linear)')
    plt.plot(FILL_FACTORS, times_double,
             marker='^', label='Open Addressing (Double)')
    plt.xlabel('Коэффициент заполнения')
    plt.ylabel('Время вставки (с)')
    plt.title('Зависимость времени вставки от коэффициента заполнения')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Гистограммы коллизий для разных хеш-функций (Chaining)
    hash_funcs: dict[str, Callable[[str, int], int]] = {
        'Simple': simple_hash,
        'Polynomial': polynomial_hash,
        'DJB2': djb2_hash
    }

    plt.figure(figsize=(15, 5))
    for i, (name, func) in enumerate(hash_funcs.items(), 1):
        chain_lengths = collisions_chaining(keys, func)
        plt.subplot(1, 3, i)
        max_bin = min(max(chain_lengths) + 1, 20)
        plt.hist(chain_lengths, bins=range(0, max_bin + 1),
                 color='skyblue', edgecolor='black')
        plt.xlabel('Длина цепочки')
        plt.ylabel('Количество ячеек')
        plt.title(f'Хеш-функция: {name}')
        plt.yscale('log')  # логарифмическая шкала для наглядности
    plt.tight_layout()
    plt.show()
