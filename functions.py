# тут реализованы тестовые функции, чтобы не писать все это в jupyter-notebook
#

import math
from interval import imath
from interval import fpu
from interval import interval


# простая функция
def F_0(x):
    return (x[0] ** 2) / 2 - (x[1] ** 2) / 4 + 3


def F_0_i(x):
    return (x[0] ** 2) / 2 - (x[1] ** 2) / 4 + 3


# Функция Экли
def F_1(x):
    return -20 * math.exp(-0.2 * math.sqrt(0.5 * (x[0] * x[0] + x[1] * x[1]))) - math.exp(
        0.5 * (math.cos(2 * math.pi * x[0]) + math.cos(2 * math.pi * x[1]))) + math.exp(1) + 20


def F_1_i(x):
    return -20 * imath.exp(-0.2 * imath.sqrt(0.5 * (x[0] * x[0] + x[1] * x[1]))) - imath.exp(
        0.5 * (imath.cos(2 * math.pi * x[0]) + imath.cos(2 * math.pi * x[1]))) + math.exp(1) + 20


# Функция Била
def F_2(x):
    return (1.5 - x[0] + x[0] * x[1]) ** 2 + (2.25 - x[0] + x[0] * x[1] ** 2) ** 2 + (2.625 - x[0] + x[0] * x[1] ** 3) ** 2


def F_2_i(x):
    return (1.5 - x[0] + x[0] * x[1]) ** 2 + (2.25 - x[0] + x[0] * x[1] ** 2) ** 2 + (2.625 - x[0] + x[0] * x[1] ** 3) ** 2


# Функция Бута
def F_3(x):
    return (x[0] + 2 * x[1] - 7) ** 2 + (2 * x[0] + x[1] - 5) ** 2


def F_3_i(x):
    return (x[0] + 2 * x[1] - 7) ** 2 + (2 * x[0] + x[1] - 5) ** 2


# Функция Матьяса
def F_4(x):
    return 0.26 * (x[0] ** 2 + x[1] ** 2) - 0.48 * x[0] * x[1]


def F_4_i(x):
    return 0.26 * (x[0] ** 2 + x[1] ** 2) - 0.48 * x[0] * x[1]


# Функция Растригина  p32
def F_5(x):
    n = len(x)
    val = 10 * n
    for i in range(n):
        val += x[i] ** 2 - 10 * math.cos(2 * math.pi * x[i])
    return val


def F_5_i(x):
    n = len(x)
    val = 10 * n
    for i in range(n):
        val += x[i] ** 2 - 10 * imath.cos(2 * math.pi * x[i])
    return val


# Функция Сферы
def F_6(x):
    val = 0
    n = len(x)
    for i in range(n):
        val += x[i] ** 2
    return val


def F_6_i(x):
    val = 0
    n = len(x)
    for i in range(n):
        val += x[i] ** 2
    return val


# Функция Розенброка  p38
def F_7(x):
    val = 0
    n = len(x)
    for i in range(n - 1):
        val += 100 * (x[i + 1] - x[i] ** 2) ** 2 + (x[i] - 1) ** 2
    return val


def F_7_i(x):
    val = 0
    n = len(x)
    for i in range(n - 1):
        val += 100 * (x[i + 1] - x[i] ** 2) ** 2 + (x[i] - 1) ** 2
    return val


# Функция Леви
def F_8(x):
    return math.sin(3 * math.pi * x[0]) ** 2 + (x[0] - 1) ** 2 * (1 + math.sin(3 * math.pi * x[1]) ** 2) + (x[1] - 1) ** 2 * (1 + math.sin(
        2 * math.pi * x[1]) ** 2)


def F_8_i(x):
    return imath.sin(3 * math.pi * x[0]) ** 2 + (x[0] - 1) ** 2 * (1 + imath.sin(3 * math.pi * x[1]) ** 2) + (x[1] - 1) ** 2 * (1 + imath.sin(
        2 * math.pi * x[1]) ** 2)


# Функция Химмельблау   p61
def F_9(x):
    return (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2


def F_9_i(x):
    return (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2


# Функция Изома
def F_10(x):
    return -math.cos(x[0]) * math.cos(x[1]) * math.exp(-((x[0] - math.pi) ** 2 + (x[1] - math.pi) ** 2))


def F_10_i(x):
    return -imath.cos(x[0]) * imath.cos(x[1]) * imath.exp(-((x[0] - math.pi) ** 2 + (x[1] - math.pi) ** 2))


# Функция Шафера
def F_11(x):
    return 0.5 + (math.sin(x[0] ** 2 - x[1] ** 2) ** 2 - 0.5) / (1 + 0.001 * (x[0] ** 2 + x[1] ** 2)) ** 2


def F_11_i(x):
    return 0.5 + (imath.sin(x[0] ** 2 - x[1] ** 2) ** 2 - 0.5) / (1 + 0.001 * (x[0] ** 2 + x[1] ** 2)) ** 2


# Функция Стыбинского-Танга
def F_12(x):
    n = len(x)
    val = 0
    for i in range(n):
        val += x[i] ** 4 - 16 * x[i] ** 2 + 5 * x[i]
    return val / 2


def F_12_i(x):
    n = len(x)
    val = 0
    for i in range(n):
        val += x[i] ** 4 - 16 * x[i] ** 2 + 5 * x[i]
    return val / 2


# # Функция "крест на подносе"
# def F_13(x):
#     return -0.0001 * ((abs(math.sin(x[0]) * math.sin(x[1]) * math.exp(abs(100 - (x[0] ** 2 + x[1] ** 2) ** 0.5 / math.pi)))) + 1) ** 0.1
#
#
# def F_13_i(x):
#     return -0.0001 * ((abs(imath.sin(x[0]) * imath.sin(x[1]) * imath.exp(abs(100 - (x[0] ** 2 + x[1] ** 2) ** 0.5 / math.pi)))) + 1) ** 0.1

# Функция "подставка для яиц"  p58
def F_13(x):
    return -(x[1] + 47) * math.sin(math.sqrt(abs(x[0] / 2 + x[1] + 47))) - x[0] * math.sin(math.sqrt(abs(x[0] - x[1] - 47)))


def F_13_i(x):
    return -(x[1] + 47) * imath.sin(imath.sqrt(abs(x[0] / 2 + x[1] + 47))) - x[0] * imath.sin(imath.sqrt(abs(x[0] - x[1] - 47)))


# Табличная функция Хольдера
def F_14(x):
    return -abs(math.sin(x[0]) * math.cos(x[1]) * math.exp(abs(1 - math.sqrt(x[0] ** 2 + x[1] ** 2) / math.pi)))


def F_14_i(x):
    return -abs(imath.sin(x[0]) * imath.cos(x[1]) * imath.exp(abs(1 - imath.sqrt(x[0] ** 2 + x[1] ** 2) / math.pi)))


# Функция Ackley  p16
def F_15(x):
    n = len(x)
    val_1 = 0
    val_2 = 0
    for i in range(n):
        val_1 += x[i] ** 2
        val_2 += math.cos(2 * math.pi * x[i])

    return 20 + math.e - 20 * math.exp(-0.2 * math.sqrt(val_1 / n)) - math.exp(val_2 / n)


def F_15_i(x):
    n = len(x)
    val_1 = 0
    val_2 = 0
    for i in range(n):
        val_1 += x[i] ** 2
        val_2 += imath.cos(2 * math.pi * x[i])

    return 20 + math.e - 20 * imath.exp(-0.2 * imath.sqrt(val_1 / n)) - imath.exp(val_2 / n)


# Функция Гриванка  p23
def F_16(x):
    n = len(x)
    val_1 = 0
    val_2 = 1
    for i in range(n):
        val_1 += x[i] ** 2
        val_2 *= math.cos(x[i] / math.sqrt(i + 1))

    return val_1 / 4000 - val_2 + 1


def F_16_i(x):
    n = len(x)
    val_1 = 0
    val_2 = 1
    for i in range(n):
        val_1 += x[i] ** 2
        val_2 *= imath.cos(x[i] / math.sqrt(i + 1))

    return val_1 / 4000 - val_2 + 1


# Функция Растригина новгородская p32
def F_17(x):
    n = len(x)
    val = n
    for i in range(n):
        val += x[i] ** 2 - math.cos(18 * math.pi * x[i])
    return val


def F_17_i(x):
    n = len(x)
    val = n
    for i in range(n):
        val += x[i] ** 2 - imath.cos(18 * math.pi * x[i])
    return val


# Функция Швефеля p44

def F_18(x):
    n = len(x)
    val = n * 418.9829
    for i in range(n):
        val += x[i] * math.sin(math.sqrt(abs(x[i])))
    return val


def F_18_i(x):
    n = len(x)
    val = n * 418.9829
    for i in range(n):
        val += x[i] * imath.sin(imath.sqrt(abs(x[i])))
    return val


# Аддитивная потенциальная функция   p52

def FF_19(x):
    val_1 = -1 / ((x - 1) ** 2 + 0.2)
    val_2 = -1 / (2 * (x - 2) ** 2 + 0.15)
    val_3 = -1 / (3 * (x - 3) ** 2 + 0.3)

    return val_1 + val_2 + val_3


def F_19(x):
    return FF_19(x[0]) + FF_19(x[1])


def F_19_i(x):
    return FF_19(x[0]) + FF_19(x[1])


# мультипликативная потенциальная функция   p76

def FF_20(x):
    val_1 = -1 / ((x - 1) ** 2 + 0.2)
    val_2 = -1 / (2 * (x - 2) ** 2 + 0.15)
    val_3 = -1 / (3 * (x - 3) ** 2 + 0.3)

    return val_1 + val_2 + val_3


def F_20(x):
    return -FF_19(x[0]) * FF_19(x[1])


def F_20_i(x):
    return -FF_19(x[0]) * FF_19(x[1])


# Levy function
def F_21(x):
    n = len(x)
    for i in range(n):
        x[i] = 3/4 + x[i]/4

    val = math.sin(math.pi*x[0])**2 + ((x[n-1]-1)**2)*(1+math.sin(2*math.pi*x[n-1])**2)
    for i in range(1,n-1):
        val += ((x[i]-1)**2)*(1+10*math.sin(math.pi*x[i]+1)**2)
    return val


def F_21_i(x):
    n = len(x)
    for i in range(n):
        x[i] = 3/4 + x[i]/4

    val = imath.sin(math.pi*x[0])**2 + ((x[n-1]-1)**2)*(1+imath.sin(2*math.pi*x[n-1])**2)
    for i in range(1,n-1):
        val += ((x[i]-1)**2)*(1+10*imath.sin(math.pi*x[i]+1)**2)
    return val


# Alpine function
def F_22(x):
    n = len(x)
    val = 0
    for i in range(n):
        val += abs(x[i]*math.sin(x[i])+0.1*x[i])
    return val


def F_22_i(x):
    n = len(x)
    val = 0
    for i in range(n):
        val += abs(x[i]*imath.sin(x[i])+0.1*x[i])
    return val

# Wave function
def F_23(x):
    n = len(x)
    val = 0
    for i in range(n):
        val += x[i]**2
    val = 1 - (1+math.cos(12*math.sqrt(val)))/(2+0.5*val)
    return val

# Wave function
def F_23_i(x):
    n = len(x)
    val = 0
    for i in range(n):
        val += x[i]**2
    val = 1 - (1+imath.cos(12*imath.sqrt(val)))/(2+0.5*val)
    return val

Functions = [F_0, F_0_i,
             F_1, F_1_i,
             F_2, F_2_i,
             F_3, F_3_i,
             F_4, F_4_i,
             F_5, F_5_i,
             F_6, F_6_i,
             F_7, F_7_i,
             F_8, F_8_i,
             F_9, F_9_i,
             F_10, F_10_i,
             F_11, F_11_i,
             F_12, F_12_i,
             F_13, F_13_i,
             F_14, F_14_i,
             F_15, F_15_i,
             F_16, F_16_i,
             F_17, F_17_i,
             F_18, F_18_i,
             F_19, F_19_i,
             F_20, F_20_i,
             F_21, F_21_i,
             F_22, F_22_i,
             F_23, F_23_i]
