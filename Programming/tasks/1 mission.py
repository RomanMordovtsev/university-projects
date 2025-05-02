#Task 1

'''class Coffee:
    additive = input('Введите добавку ')
    def show_my_drink(self):
        if self.additive == '':
            return 'Черный кофе'
        else:
            return 'Кофе и ' + self.additive

human = Coffee()
print(human.show_my_drink())

#Task 2
from math import sqrt

class Triangle:
    def __init__(self, kind):
        if kind == 'Равносторонний':
            self.a = int(input('Введите сторону '))
            self.b, self.c = self.a, self.a
            self.p = self.a * 3 / 2
        elif kind == 'Обычный':
            self.a, self.b, self.c = int(input('1 сторона = ')), int(input('2 сторона = ')), int(input('3 сторона = '))
            self.p = (self.a + self.b + self.c) / 2
        elif kind == 'Не существующий':
            self.a, self.b, self.c = int(input('1 сторона = ')), int(input('2 сторона = ')), int(input('3 сторона = '))

    def Square(self):
        if self.a > self.b + self.c or self.b > self.a + self.c or self.c > self.a + self.b or self.a < 0 or self.b < 0 or self.c < 0:
            return 'У несуществующего треугольника и площадь считать не хочется'
        else:
            return sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))


figure = Triangle(input('Введите вид треугольника '))
print(figure.Square())

#Task 3

class Mathem:
    a, b = int(input('1 переменная = ')), int(input('2 переменная = '))
    def addition(self):
        return self.a + self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        if self.b == 0:
            return 'no way'
        else:
            return self.a / self.b
    def subtraction(self):
        return self.a - self.b

action = Mathem()
print('a + b = ', action.addition(), 'a * b = ', action.multiplication(), 'a : c = ', action.division(), 'a - c = ', action.subtraction())'''

#Task 4

class Tree:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        self.lc = 0
        self.gt = 0

    def Loc_Change(self):
        if self.lc == 0:
            print('Дерево пересадили')
            self.lc += 1
        else:
            print('Уже было пересажено')

    def Goodbye_Tree(self):
        if self.gt == 0:
            print('Дерево вырубили')
            self.gt += 1
        else:
            print('Уже было вырублено')

    def Tree_Name(self):
        self.name = input('Введите новое имя ')

    def Tree_Age(self):
        self.age = input('Введите возраст дерева ')

    def Tree_Height(self):
        self.height = input('Введите высоту дерева ')

    def Tree_Info(self):
        goda = ['2', '3', '4']
        let = ['5', '6', '7', '8', '9', '0']
        if self.age[-1] == 1:
            knc = 'год'
        elif self.age[-1] in goda:
            knc = 'года'
        elif self.age[-1] in let:
            knc = 'лет'
        else:
            knc = 'Ваш возраст меня не впечатляет'
        print("Название дерева -", self.name)
        print("Возраст дерева -", self.age, knc)
        print("Высота дерева -", self.height, 'метров')


Hogwarts = Tree(input('Введите имя дерева '), input('Введите возраст дерева '), input('Введите высоту дерева '))

while True:
    method = input('Введите метод ')
    if method == 'Пересадка':
        Hogwarts.Loc_Change()
    elif method == 'Вырубка':
        Hogwarts.Goodbye_Tree()
    elif method == 'Имя':
        Hogwarts.Tree_Name()
    elif method == 'Возраст':
        Hogwarts.Tree_Age()
    elif method == 'Высота':
        Hogwarts.Tree_Height()
    elif method == 'Информация':
        Hogwarts.Tree_Info()
    elif method == 'Шик':
        break
