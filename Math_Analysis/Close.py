from math import *

def Euler(x0, y0, z0):
    h = 0.1
    x = round(x0 + h, 4)
    y = round(y0 + h*z0, 4)
    f = x0 ** 2 * e ** (-3 * x0)
    '''per = (-(1 * z0 + 2 * y))
    per += z0'''
    z = round(z0 + h * (-6 * z0 - 10 * y0 + f), 4)
    return [x, y, z]

i, x0, y0, z0 = 0, 0, 1, 2
print('Euler:')
print('i x y z')
print(i, x0, y0, z0 * 0.1)
for i in range(1, 6):
    strok = Euler(x0, y0, z0)
    print(i, *strok)
    x0, y0, z0 = strok[0], strok[1], strok[2]

def F(x0):
    return x0 ** 2 * e ** (-3 * x0)

def F2(x0, y0, z0):
    return -6 * z0 - 10 * y0 + F(x0)

def RungeKutta(x0, y0, z0):
    h = 0.1
    # f = x0 ** 2 * e ** (-3 * x0)
    k1, l1 = h * z0, h * F2(x0, y0, z0)
    k2, l2 = h * (z0 + 0.5 * l1), h * F2(x0 + 0.5 * h, y0 + 0.5 * k1, z0 + 0.5 * l1)
    k3, l3 = h * (z0 + 0.5 * l2), h * F2(x0 + 0.5 * h, y0 + 0.5 * k2, z0 + 0.5 * l2)
    k4, l4 = h * (z0 + l3), h * F2(x0 + h, y0 + k3, z0 + l3)
    dy, dz = (k1 + 2 * k2 + 2 * k3 + k4) / 6, (l1 + 2 * l2 + 2 * l3 + l4) / 6
    y, z = y0 + dy, z0 + dz
    return [round(y, 4), round(z, 4)]

i, x0, y0, z0 = 0, 0, 1, 2
print('Runge-Kutta:')
print('i x y z')
print(i, x0, y0, z0 * 0.1)
for i in range(1, 6):
    strok = RungeKutta(x0, y0, z0)
    x0, y0, z0 = x0 + 0.1, strok[0], strok[1]
    print(i, round(x0, 4), *strok)


