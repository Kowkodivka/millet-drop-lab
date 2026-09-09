# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "matplotlib>=3.11.1",
#     "numpy>=2.5.3",
#     "scipy>=1.18.1",
# ]
# ///

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

H = 27.0 / 100
D = 2.05 / 1000
G = 10
RHO_DIFF = 50

BINS = 20

FILE_NAME = "data.csv"


def main() -> None:
    t = np.loadtxt(FILE_NAME, delimiter=",", skiprows=1, usecols=1)

    plt.figure(figsize=(10, 7))
    counts, bin_edges, _ = plt.hist(
        t,
        bins=BINS,
        edgecolor="black",
        color="skyblue",
        label="Экспериментальные данные",
    )

    plt.xlabel("Время падения, с")
    plt.ylabel("Число крупинок")
    plt.title("Гистрограмма времени падения крупинок пшена")
    plt.grid(axis="y", alpha=0.3)

    plt.savefig("figures/hist.png", dpi=300, bbox_inches="tight")

    mode_idx = np.argmax(counts)
    t_mode = (bin_edges[mode_idx] + bin_edges[mode_idx + 1]) / 2
    print(f"Наиболее вероятное время t = {t_mode:.2f} с")

    sigma = np.std(t, ddof=1)
    print(f"Среднеквадратичное отклонение sigma = {sigma:.2f} с")

    t_mean = np.mean(t)
    v = H / t_mean
    print(f"Средняя скорость падения v = {v:.2f} м/с")

    x = np.linspace(t.min(), t.max(), 200)

    bin_width = bin_edges[1] - bin_edges[0]

    gauss = norm.pdf(x, t_mean, sigma)
    gauss_scaled = gauss * len(t) * bin_width

    plt.plot(
        x,
        gauss_scaled,
        "r-",
        linewidth=2,
        label="Теоретическое нормальное распределение",
    )
    plt.xlabel("Время падения, с")
    plt.ylabel("Число крупинок")
    plt.title("Сравнение гистограммы с нормальным распределением")
    plt.legend()
    plt.grid(axis="y", alpha=0.3)
    plt.savefig("figures/hist_with_gauss.png", dpi=300, bbox_inches="tight")

    eta = D**2 * G * RHO_DIFF / (18 * v)
    print(f"Коэффициент вязкости eta = {eta:.2e} Па*с")


if __name__ == "__main__":
    main()
