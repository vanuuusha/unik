#y = (a*x_k + c) mod m
# iteration process
import matplotlib.pyplot as plt


def random_gen(n=10000, x0=1):
    m = 1024*81*625*(49*49)
    b = 4*3*5*7
    a = b+1
    c = 17
    y = []
    for i in range(n):
        y.append((a*x0 + c) % m)
        x0 = y[-1]

    # y_max = max(y)
    # y_min = min(y)
    # b = 1
    # a = 0
    # y = [a + (y_i - y_min) / (y_max - y_min) * (b - a) for y_i in y]
    # y_1 = [y_i for i, y_i in enumerate(y) if i % 2 == 0]
    # y_2 = [y_i for i, y_i in enumerate(y) if i % 2 == 1]
    return y_1, y_2


if __name__ == '__main__':
    x, y = random_gen()
    plt.figure(figsize=(16, 16), dpi=80)
    plt.scatter(x, y, s=4)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()