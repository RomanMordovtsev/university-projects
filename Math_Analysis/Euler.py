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
print('i x y z')
print(i, x0, y0, z0 * 0.1)
for i in range(1, 6):
    strok = Euler(x0, y0, z0)
    print(i, *strok)
    x0, y0, z0 = strok[0], strok[1], strok[2]

