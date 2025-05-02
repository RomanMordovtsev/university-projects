'''
Данное решение хранит информацию о ходах
В отличии от очевидного перебора (который выполняется за O(n^2)),
данный алгоритм работает за O(1), однако требует дополнительные затраты по памяти
'''
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

Xrow = [0, 0, 0]
Xcolumn = [0, 0, 0]
Xdiag = [0]
Xanti_diag = [0]

Orow = [0, 0, 0]
Ocolumn = [0, 0, 0]
Odiag = [0]
Oanti_diag = [0]

curr_player = 0


def tablePrinter():
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
        print('\n')
    print('\n')


tablePrinter()


def winCheck(r, c):
    '''
    #Крестики - четные числа
    #Нолики - нечетный
    '''
    if curr_player % 2 == 0:
        Xrow[r] += 1
        Xcolumn[c] += 1
        if (r == c):
            Xdiag[0] += 1
        if (r + c) == 2:
            Xanti_diag[0] += 1
        print(Xdiag)

        if (Xrow[r] == 3 or Xcolumn[c] == 3 or Xdiag[0] == 3 or Xanti_diag[0] == 3):
            print("Крестики победили")
            return True

    if curr_player % 2 == 1:
        Orow[r] += 1
        Ocolumn[c] += 1
        if (r == c): Odiag[0] += 1
        if (r + c) == 2: Oanti_diag[0] += 1

        if (Orow[r] == 3 or Ocolumn[c] == 3 or Odiag[0] == 3 or Oanti_diag[0] == 3):
            print("Нолики победили")
            return True

        return False


def placer(r, c):
    if curr_player % 2 == 0:
        board[r][c] = 'X'
    else:
        board[r][c] = 'O'


r = int(input("Введите ряд: "))
c = int(input("Введите колонку: "))
placer(r - 1, c - 1)
tablePrinter()

while not winCheck(r - 1, c - 1):
    curr_player += 1
    r = int(input("Введите ряд: "))
    c = int(input("Введите колонку: "))
    placer(r - 1, c - 1)
    tablePrinter()
