#линейный когруэнтный метод
# m > 0 - модуль
# 0 <= a < m - множитель
# 0 <= c < m - приращение
# 0 <= X0 < m- начальное значение

# последовательность Xn+1 = (a*Xn + c) mod m
# для того чтобы период последовательности был равен m необходимо:
# 1) c и m взаимно простые
# 2) a-1 кратно p для каждого простого p - делителя m
# 3) Если m кратно 4, то и a-1 кратно 4

import matplotlib.pyplot as plt



def random_gen(n=10000, x0=1):
    m = 1024*81*625*(49*49)
    a = 4*3*5*7+1
    c = 17
    x = []
    for i in range(n):
        x.append((a*x0 + c) % m)
        x0 = x[-1]
    # x - последовательность из случайных чисел
    x_max = max(x)
    x = [i/x_max for i in x]
    # разобьем эту последовательность на две подпоследовательности случанйхы величин
    x_1 = [value for i,value in enumerate(x) if i % 2 == 0]
    x_2 = [value for i, value in enumerate(x) if i % 2 == 1]
    # получили две последовательности С.В.
    return x_1, x_2

def break_random_gen(n=10000, x0=1):
    m = 1024 * 81 * 625 * (49 * 49)
    a = 4 * 3 * 5 + 1 # не выполняем условия про простые числа
    c = 17
    x = []
    for i in range(n):
        x.append((a * x0 + c) % m)
        x0 = x[-1]
    # x - последовательность из случайных чисел
    x_max = max(x)
    x = [i / x_max for i in x]
    # разобьем эту последовательность на две подпоследовательности случанйхы величин
    x_1 = [value for i, value in enumerate(x) if i % 2 == 0]
    x_2 = [value for i, value in enumerate(x) if i % 2 == 1]
    # получили две последовательности С.В.
    return x_1, x_2


def draw_random_value_0_1():
    x, y = random_gen()
    plt.figure(figsize=(16, 16), dpi=80)
    plt.scatter(x, y, s=4)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def draw_random_value_0_1_break():
    x, y = break_random_gen()
    plt.figure(figsize=(16, 16), dpi=80)
    plt.scatter(x, y, s=4)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


if __name__ == '__main__':
    draw_random_value_0_1_break()