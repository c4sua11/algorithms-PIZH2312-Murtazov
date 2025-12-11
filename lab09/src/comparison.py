import timeit
import matplotlib.pyplot as plt

# Импорт наших функций
from dynamic_programming import fib_top_down, fib_bottom_up, lcs_top_down
from dynamic_programming import lcs_bottom_up


def measure_time(func, *args, number: int = 100) -> float:
    """Замеряет среднее время выполнения функции."""
    timer = timeit.Timer(lambda: func(*args))
    # Возвращаем время в микросекундах
    return (timer.timeit(number=number) / number) * 1_000_000


def compare_fibonacci():
    """Сравнение подходов для чисел Фибоначчи."""
    ns = [10, 20, 50, 100, 200, 500]
    times_top_down = []
    times_bottom_up = []

    print(f"{'N':<10} {'Top-Down (мкс)':<20} {'Bottom-Up (мкс)':<20}")
    print("-" * 50)

    for n in ns:
        # Для Top-Down важно создавать новый словарь memo каждый раз,
        # иначе замер будет некорректным (ответ возьмется из кэша)
        t_td = measure_time(fib_top_down, n, {}, number=50)
        t_bu = measure_time(fib_bottom_up, n, number=50)

        times_top_down.append(t_td)
        times_bottom_up.append(t_bu)

        print(f"{n:<10} {t_td:<20.4f} {t_bu:<20.4f}")

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(ns, times_top_down, label='Fib Top-Down '
             '(Memoization)', marker='o')
    plt.plot(ns, times_bottom_up, label='Fib Bottom-Up '
             '(Tabulation)', marker='x')
    plt.title('Сравнение подходов ДП: Числа Фибоначчи')
    plt.xlabel('N (номер числа)')
    plt.ylabel('Время (мкс)')
    plt.legend()
    plt.grid(True)
    plt.savefig('fib_comparison.png')
    print("\nГрафик сохранен как 'fib_comparison.png'")


def compare_lcs():
    """Сравнение подходов для LCS."""
    print("\nСравнение LCS для строк одинаковой длины:")
    lengths = [5, 10, 15, 20, 50]

    print(f"{'Len':<10} {'Top-Down (мкс)':<20} {'Bottom-Up (мкс)':<20}")
    print("-" * 50)

    for length in lengths:
        s1 = "A" * length
        s2 = "A" * (length // 2) + "B" * (length - length // 2)

        t_td = measure_time(lcs_top_down, s1, s2, 0, 0, {}, number=20)
        t_bu = measure_time(lcs_bottom_up, s1, s2, number=20)

        print(f"{length:<10} {t_td:<20.4f} {t_bu:<20.4f}")


if __name__ == "__main__":
    print("=== Анализ производительности ===")
    compare_fibonacci()
    compare_lcs()

    print("\nВывод:")
    print("1. Оба подхода имеют схожую "
          "асимптотику O(N) для Фибоначчи и O(NM) для LCS.")
    print("2. Bottom-Up (табличный метод) "
          "часто работает быстрее на практике, так как")
    print("   исключает накладные расходы на "
          "рекурсивные вызовы (переполнение стека,")
    print("   создание фреймов функций).")
