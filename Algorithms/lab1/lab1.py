import numpy as NP



#collumns = int(input())
#matrix = []
#for c in range(collumns):
    #row = [int(x) for x in input().split()]
    #matrix.append(row)


def trans(matrix):
    matrix_1 = []
    rows = len(matrix)
    columns = len(matrix[0])
    for c in range(columns):
        matrix_1.append([])
        for r in range(rows):
            matrix_1[c].append(matrix[r][c])
    return matrix_1

def mult(matrix_1, matrix_2):
    rows_1 = len(matrix_1)
    columns_1 = len(matrix_1[0])
    rows_2 = len(matrix_2)
    columns_2 = len(matrix_2[0])

    if columns_1 != rows_2:
      return
    
    matrix_3 = [[0 for rows in range(columns_2)] for columns in range(rows_1)]

    for i in range(rows_1):
        for j in range(columns_2):
            for k in range(rows_2):
                matrix_3[i][j] += matrix_1[i][k] * matrix_2[k][j]
    return matrix_3

def opredelitel(m):
    opred = m[0][0]*m[1][1]*m[2][2]+m[1][0]*m[0][2]*m[2][1]+m[2][0]*m[0][1]*m[1][2]-m[2][0]*m[1][1]*m[0][2]-m[1][0]*m[0][1]*m[2][2]-m[0][0]*m[2][1]*m[1][2]
    return opred


def det_2(m):
    opred = m[0][0]*m[1][1] - m[0][1]*m[1][0]
    return opred

def dop_matrix(matrix, i, j):
    k = 0
    minor = [[0,0],[0,0]]
    for i1 in range(0,3):
        for j1 in range(0,3):
            if i1 != i and j1 != j:
                i2 = k//2
                j2 = k%2
                minor[i2][j2] += matrix[i1][j1]
                k += 1
    det = det_2(minor)
    return det
 

def reverse():
    matrix = []
    for i in range(3):
        row = [int(x) for x in input().split()]
        if len(row) != 3:
            print("Задан неверный размер матрицы")
            return 0
        else:
            matrix.append(row)
    reverse_matrix = [[0,0,0] for i in range(3)]
    det = opredelitel(matrix)
    if det == 0:
        return "Определитель равен нулю"
    reverse_det = 1/det
    alg_matrix = [[0,0,0],[0,0,0],[0,0,0]]
    k = 1
    for i in range(0,3):
        for j in range(0,3):
            add = dop_matrix(matrix, i, j)
            if k % 2 == 0:
                add = -1*add
            alg_matrix[i][j] += add
            k += 1

    for i in range(0,3):
        for j in range(0,3):
            alg_matrix[i][j] = alg_matrix[i][j] * reverse_det
    return trans(alg_matrix)

#rev_matrix = reverse()

x = NP.arange(1, 101)

cnd_list = [ (x%3==0) & (x%5==0), x%3==0, x%5==0, True ]
choice_list = ["fizzbuzz", "fizz", "buzz", x]

res = NP.select(cnd_list, choice_list)
print(res)



matrix = []

while True:
    mat = input('Введите строку (через пробел) ')
    if mat != '':
        mat = list(map(int, mat.split()))
        matrix.append(mat)
    else:
        break
print(matrix)

import numpy as NP
x = NP.arange(1, 101)

cnd_list = [ (x%3==0) & (x%5==0), x%3==0, x%5==0, True ]
choice_list = ["fizzbuzz", "fizz", "buzz", x]

res = NP.select(cnd_list, choice_list)
print(*res)

print(NP.linalg.inv(matrix))import numpy as NP


