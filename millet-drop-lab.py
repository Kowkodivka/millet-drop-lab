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
from scipy.stats import t as student_t

H = 27.0 / 100
H_INSTR_ERR = 0.05 / 100

N_GRAINS = 68
ROW_LENGTH = 139.4 / 1000
ROW_INSTR_ERR = 0.05 / 100
D = ROW_LENGTH / N_GRAINS
D_ERR = ROW_INSTR_ERR / N_GRAINS

T_INSTR_ERR = 0.01

G = 10
RHO_DIFF = 50

ALPHA = 0.95
BINS = 20

FILE_NAME = "data.csv"


def main() -> None:
    print(f"Средний диаметр крупинки d = {D * 1000:.3f} мм")
    print(f"Погрешность диаметра Delta d = {D_ERR * 1000:.4f} мм")

    t = np.loadtxt(FILE_NAME, delimiter=",", skiprows=1, usecols=1)
    n = len(t)

    plt.figure(figsize=(10, 7))
    counts, bin_edges, _ = plt.hist(
        t,
        bins=BINS,
        edgecolor="black",
        color="skyblue",
        label="Экспериментальные данные",
    )

    plt.xlabel("Время падения $t$, с")
    plt.ylabel("Число крупинок, шт")
    plt.title("Гистограмма времени падения крупинок пшена")
    plt.grid(axis="y", alpha=0.3)

    plt.savefig("figures/hist.png", dpi=300, bbox_inches="tight")

    mode_idx = np.argmax(counts)
    t_mode = (bin_edges[mode_idx] + bin_edges[mode_idx + 1]) / 2
    print(f"Ширина интервала гистограммы = {bin_edges[1] - bin_edges[0]:.4f} с")
    print(f"Наиболее вероятное время t = {t_mode:.3f} с")

    sigma = np.std(t, ddof=1)
    print(f"Среднеквадратичное отклонение sigma = {sigma:.4f} с")

    t_mean = np.mean(t)
    print(f"Среднее время падения t_mean = {t_mean:.4f} с")

    t_alpha_n = student_t.ppf((1 + ALPHA) / 2, df=n - 1)
    print(f"Коэффициент Стьюдента t_alpha,n (n={n}) = {t_alpha_n:.3f}")

    t_mean_rand_err = t_alpha_n * sigma / np.sqrt(n)
    t_mean_err = np.sqrt(t_mean_rand_err**2 + T_INSTR_ERR**2)
    print(f"Случайная погрешность среднего Delta t_sl = {t_mean_rand_err:.4f} с")
    print(f"Полная погрешность среднего Delta t = {t_mean_err:.4f} с")

    v = H / t_mean
    v_err = v * np.sqrt((H_INSTR_ERR / H) ** 2 + (t_mean_err / t_mean) ** 2)
    print(f"Средняя скорость падения v = {v:.4f} м/с")
    print(f"Погрешность скорости Delta v = {v_err:.4f} м/с")

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
    plt.xlabel("Время падения $t$, с")
    plt.ylabel("Число крупинок, шт")
    plt.title("Сравнение гистограммы с нормальным распределением")
    plt.legend()
    plt.grid(axis="y", alpha=0.3)
    plt.savefig("figures/hist_with_gauss.png", dpi=300, bbox_inches="tight")

    eta = D**2 * G * RHO_DIFF / (18 * v)
    eta_err = eta * np.sqrt((2 * D_ERR / D) ** 2 + (v_err / v) ** 2)
    print(f"Коэффициент вязкости eta = {eta:.4e} Па*с")
    print(f"Погрешность коэффициента вязкости Delta eta = {eta_err:.4e} Па*с")
    print(f"Относительная погрешность eta = {eta_err / eta * 100:.2f} %")


if __name__ == "__main__":
    main()
