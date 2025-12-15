import timeit
import random
import matplotlib.pyplot as plt
from typing import Callable

from string_algorithms import (
    kmp_search,
    z_function_search,
    rabin_karp_search
)


def generate_random_string(length: int, alphabet: str = "ACGT") -> str:
    """Генерация случайной строки (например,
    ДНК для большого кол-ва совпадений)."""
    return ''.join(random.choice(alphabet) for _ in range(length))


def measure_time(algorithm: Callable,
                 text: str, pattern: str, runs: int = 10) -> float:
    """Замер среднего времени выполнения."""
    timer = timeit.Timer(lambda: algorithm(text, pattern))
    total_time = timer.timeit(number=runs)
    return (total_time / runs) * 1000  # мс


def run_experiments():
    print("Запуск экспериментального исследования...")

    # Параметры теста
    text_lengths = [1000, 5000, 10000, 20000, 50000]
    pattern_len = 100

    times_kmp = []
    times_z = []
    times_rk = []
    times_native = []  # Встроенный find (для сравнения)

    for n in text_lengths:
        text = generate_random_string(n)
        pattern = generate_random_string(pattern_len)
        # Гарантируем, что паттерн есть в
        # тексте (в конце), чтобы не было раннего выхода
        text = text[:-pattern_len] + pattern

        times_kmp.append(measure_time(kmp_search, text, pattern))
        times_z.append(measure_time(z_function_search, text, pattern))
        times_rk.append(measure_time(rabin_karp_search, text, pattern))

        # Сравнение со встроенным
        # методом str.find (наивный оптимизированный на C)
        # Оборачиваем find, чтобы сигнатура совпадала
        def native_search(t, p):
            return t.find(p)
        times_native.append(measure_time(native_search, text, pattern))

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(text_lengths, times_kmp, 'o-', label='KMP')
    plt.plot(text_lengths, times_z, 's-', label='Z-Function Search')
    plt.plot(text_lengths, times_rk, '^-', label='Rabin-Karp')
    # Native обычно слишком быстрый, можно не рисовать или рисовать пунктиром
    plt.plot(text_lengths, times_native, '--',
             color='gray', alpha=0.5, label='Native (find)')

    plt.title(f'Сравнение алгоритмов поиска (Pattern len = {pattern_len})')
    plt.xlabel('Длина текста (N)')
    plt.ylabel('Время выполнения (мс)')
    plt.legend()
    plt.grid(True)

    filename = 'string_algorithms_benchmark.png'
    plt.savefig(filename)
    print(f"График сохранен в файл: {filename}")
    # plt.show()


if __name__ == "__main__":
    run_experiments()
