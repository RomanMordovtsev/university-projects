# Task 1

class Student:
    def __init__(self):
        self.name = 'Radomir'
        self.age = 18
        self.groupNumber = 1213

    def set_name(self):
        name = input('Введите имя ')
        if name == '':
            self.name = 'Radomir'
        else:
            self.name = name

    def set_age(self):
        age = input('Введите возраст ')
        if age == '' or int(age) < 0:
            self.age = 18
        else:
            self.age = int(age)

    def set_groupNumber(self):
        groupNumber = input('Введите группу ')
        if groupNumber == '':
            self.groupNumber = 1213
        else:
            self.groupNumber = int(groupNumber)

    def get_name(self):
        self.set_name(self)
        return self.name

    def get_age(self):
        self.set_age(self)
        return self.age

    def get_groupNumver(self):
        self.set_groupNumber(self)
        return self.groupNumber

names = []
ages = []
groupNumbers = []

for i in range(5):
    hum = Student
    names.append(hum.get_name(hum))
    ages.append(hum.get_age(hum))
    groupNumbers.append(hum.get_groupNumver(hum))

for j in range(5):
    print('Имя студента -', names[j])
    print('Возраст студента -', ages[j])
    print('Номер группы студента -', groupNumbers[j])

# Task 2

class Country:
    pass

class Russia(Country):
    def __init__(self):
        self.capital = 'Moscow'
        self.population = 143.4

    def setPopulation(self):
        population = input('Население страны = ')
        if population == '' or float(population) < 0:
            pass
        else:
            self.population = float(population)

    def getPopulation(self):
        self.setPopulation()
        return self.population

class Canada:
    def __init__(self):
        self.capital = 'Ottava'
        self.population = 38.25

    def setPopulation(self):
        population = input('Население страны = ')
        if population == '' or float(population) < 0:
            pass
        else:
            self.population = float(population)

    def getPopulation(self):
        self.setPopulation()
        return self.population

class Germany:
    def __init__(self):
        self.capital = 'Berlin'
        self.population = 83.2

    def setPopulation(self):
        population = input('Население страны = ')
        if population == '' or float(population) < 0:
            pass
        else:
            self.population = float(population)

    def getPopulation(self):
        self.setPopulation()
        return self.population

Rus = Russia()
print(Rus.getPopulation())
Can = Canada()
print(Can.getPopulation())
Ger = Germany()
print(Ger.getPopulation())

# Task 3

class Games:
    def __init__(self):
        self.Year = input('Введите год выхода игры ')

    def getName(self):
        return 'Skyrim'

class PCGames(Games):
    def __init__(self):
        self.platform = 'PC'

    def getName(self):
        return 'Hitman'

class PS4Games(Games):
    def __init__(self):
        self.platform = 'PS4'

    def getName(self):
        return 'The Last of Us'


class XboxGames(Games):
    def __init__(self):
        self.platform = 'XBox'

    def getName(self):
        return 'Forza Horizon'


class MobileGames(Games):
    def __init__(self):
        self.platform = 'Phone'

    def getName(self):
        return 'Subway Surfers'

sirius = PCGames()
print(sirius.getName())
rigel = PS4Games()
print(rigel.getName())
arcturus = XboxGames()
print(arcturus.getName())
centaura = MobileGames()
print(centaura.getName())

# Task 4

class Dog:
    def __init__(self):
        self.nickname = input('Кличка питомца ')
        age = int(input('Возраст питомца = '))
        if 0 < age < 20:
            self.age = age
        else:
            age = int(input('Врушки, настоящий возраст = '))


class ToyTerrier(Dog):
    def __init__(self):
        super(ToyTerrier, self).__init__()
        self.barking = input('Введите лай ')
        self.destination = input('Введите предназачение ')

    def Info(self):
        print('Кличка -', self.nickname)
        print('Возраст =', self.age)
        print('Звук голоса -', self.barking)
        print('Предназначение -', self.destination)

class Spaniel(Dog):
    def __init__(self):
        super(Spaniel, self).__init__()
        self.barking = input('Введите лай ')
        self.destination = input('Введите предназачение ')

    def Info(self):
        print('Кличка -', self.nickname)
        print('Возраст =', self.age)
        print('Звук голоса -', self.barking)
        print('Предназначение -', self.destination)

class GermanShepherd(Dog):
    def __init__(self):
        super(GermanShepherd, self).__init__()
        self.barking = input('Введите лай ')
        self.destination = input('Введите предназачение ')

    def Info(self):
        print('Кличка -', self.nickname)
        print('Возраст =', self.age)
        print('Звук голоса -', self.barking)
        print('Предназначение -', self.destination)

Hunter = ToyTerrier()
Hunter.Info()
Guard = GermanShepherd()
Guard.Info()
Homey = ToyTerrier()
Homey.Info()







