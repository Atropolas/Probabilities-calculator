import numpy as np
from math import factorial as f

# Количество итераций (точность вычислений)
n = 100000

a = input("Что будем смотреть:" + "\n" + "1. Номинал" + "\n" + "2. Масть" + "\n" + "3. Козырь"+"\n" + "Ваш выбор: ")


def koz(n):
    vod = input("Введите комбинацию: ")
    z = 0
    x = np.array([1, 0])
    x = np.repeat(x, [8, 27], axis=0)
    for i in range(1, n):
        y = np.random.choice(x, size=6, replace=False)
        summ = sum(y)
        if summ == int(vod):
            z = 1 + z
    answer = z / n * 100
    print(repr(answer))


def mast(n):
    vod = input("Введите комбинацию: ")
    b = len(vod)
    z = 0
    x = np.array([1000, 100, 10, 1])
    x = np.repeat(x, 9, axis=0)

    for i in range(1, n):
        y = np.random.choice(x, size=6, replace=False)
        summ = list(str(sum(y)))
        vod = list(vod)
        while len(summ) < 4:
            summ.insert(0, 0)
        if summ[0:b] == vod[0:b]:
            z = 1 + z
    answer = z*f(4)/f(4-b) / n * 100
    print(repr(answer))


def nominal(n):
    vod = input("Введите комбинацию: ")
    b = len(vod)
    z = 0
    x = np.array([100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1])
    x = np.repeat(x, 9, axis=0)
    for i in range(1, n):
        y = np.random.choice(x, size=6, replace=False)
        summ = list(str(sum(y)))
        vod = list(vod)
        while len(summ) < 9:
            summ.insert(0, 0)
        if summ[0:b] == vod[0:b]:
            z = 1 + z
    answer = z*f(9)/f(9-b) / n * 100
    print(repr(answer))


if a == "1":
    nominal(n)
elif a == "2":
    mast(n)
elif a == "3":
    koz(n)



