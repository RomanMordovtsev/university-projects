'''
Данный код начинает поиск с правого верхнего
'''

matrix = [
    [1, 4, 7, 14, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

def Finder(num):
    i = 0
    j = len(matrix[0]) - 1

    while (i < len(matrix) or j >= 0):
        if matrix[i][j] == num:
            return [i, j]
        if i == len(matrix) and j == len(matrix[0]):
            return 'не найден '
        if matrix[i][j] > num:
            j -= 1
        elif matrix[i][j] < num:
            i += 1
        else:
            return 'такого элемента нет '

print(Finder(26))