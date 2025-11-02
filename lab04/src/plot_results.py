# plot_results.py
"""
Модуль для визуализации результатов измерений производительности алгоритмов
сортировки.
Использует pandas и matplotlib для построения графиков и анализа данных.
"""

import pandas as pd
import matplotlib.pyplot as plt


def plot_time_vs_size(df):
    """Строит графики зависимости времени выполнения от размера массива для
    случайных данных."""
    random_df = df[df["Тип данных"] == "random"]

    plt.figure(figsize=(10, 6))
    for algo in random_df["Алгоритм"].unique():
        subset = random_df[random_df["Алгоритм"] == algo]
        plt.plot(subset["Размер"], subset["Время (сек)"],
                 marker="o", label=algo)

    plt.title("Зависимость времени сортировки "
              "от размера массива (random data)")
    plt.xlabel("Размер массива")
    plt.ylabel("Время выполнения (сек)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("plot_time_vs_size.png", dpi=300)
    plt.show()


def plot_time_vs_data_type(df, fixed_size=5000):
    """Строит график зависимости времени выполнения от типа данных для
    фиксированного размера."""
    fixed_df = df[df["Размер"] == fixed_size]

    plt.figure(figsize=(10, 6))
    for algo in fixed_df["Алгоритм"].unique():
        subset = fixed_df[fixed_df["Алгоритм"] == algo]
        plt.plot(subset["Тип данных"], subset["Время (сек)"],
                 marker="o", label=algo)

    plt.title(f"Зависимость времени сортировки от "
              f"типа данных (n = {fixed_size})")
    plt.xlabel("Тип данных")
    plt.ylabel("Время выполнения (сек)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("plot_time_vs_data_type.png", dpi=300)
    plt.show()


def summarize_results(df):
    """Создает сводную таблицу со средним временем выполнения для каждого
    алгоритма и типа данных."""
    summary = df.groupby(["Алгоритм",
                          "Тип данных"])["Время (сек)"].mean().reset_index()
    summary.to_csv("summary_results.csv", index=False)
    print("Сводная таблица сохранена в summary_results.csv")
    return summary


if __name__ == "__main__":
    df = pd.read_csv("results.csv")

    print("📊 Загружены результаты:")
    print(df.head())

    # Сводная таблица
    summary = summarize_results(df)

    # Построение графиков
    plot_time_vs_size(df)
    plot_time_vs_data_type(df)
