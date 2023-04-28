import math
import time

import matplotlib.pyplot as plt
from laba1 import random_gen
from scipy.stats import norm
import numpy as np

def make_gaus():
    x1, y1 = random_gen(x0=2)
    x2, y2 = random_gen(x0=3)
    x1.extend(y1)
    x2.extend(y2)
    U1, U2 = x1, x2
    # U1, U2 - случайно распрделенные величины

    X, Y = [], []
    start = time.time()
    for i in range(len(U1)):
        X.append(math.sqrt(-2 * math.log(U2[i])) * math.cos(2 * math.pi * U1[i]))
    for i in range(len(U1)):
        Y.append(math.sqrt(-2 * math.log(U2[i])) * math.sin(2 * math.pi * U1[i]))
    print(time.time() - start)
    return X, Y


def F(x):
    """
    Вычисляет значение функции F(x) для заданного аргумента x, используя разложение в степенной ряд.
    """
    result = 0
    for n in range(0, 100):
        numerator = (-1) ** n * x ** (2 * n + 1)
        denominator = np.math.factorial(n) * (2 * n + 1) * 2 ** n
        result += numerator / denominator
    result *= 1 / np.sqrt(2 * np.pi)
    return result


def newton(y, tol=1e-3, maxiter=1000):
    x = 1
    for i in range(maxiter):
        fx = norm.cdf(x) - y
        fprime_x = norm.pdf(x)
        delta = fx / fprime_x
        x -= delta
        if abs(norm.cdf(x) - y) < tol:
            return x

    # Если решение не было найдено, вызывается исключение
    raise ValueError(f"Не удалось найти решение после {maxiter} итераций")


def make_gaus_not_yavno():
    x1, y1 = random_gen(x0=2)
    x2, y2 = random_gen(x0=3)
    x1.extend(y1)
    x2.extend(y2)
    U1, U2 = x1, x2
    X, Y = [], []
    start = time.time()
    for i in range(len(U1)):
        X.append(newton(U1[i]))
    for i in range(len(U2)):
        Y.append(newton(U2[i]))
    print(time.time() - start)
    return X, Y


if __name__ == '__main__':
    x, y = make_gaus_not_yavno()
    plt.figure(figsize=(16, 16), dpi=80)
    plt.scatter(x, y, s=4)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()