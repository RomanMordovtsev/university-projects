import random
from abc import ABC


def Meta(type): # Создание мета-класса
    def __init__(self, name, bases):
        pass

class Fighter(ABC): # Наследование от абстрактного класса
    def __init__(self):
        self.health = 100

    def __add__(self, other):
        return self.health & other.health

    def coming(self):
        pass

class SpeechMixin: # Создание класса-миксина
    def hairstyle(self):
        self.variants = ['"My hairstyle is perfect" - says the Winner', '"My hairstyle is amazing" - says the Winner', '"My hairstyle is brilliant" - says the Winner']
        return random.choice(self.variants)

    def naming(self):
        return input("Fighter's name is ")

class Ninja(Fighter, SpeechMixin): # Наследование от класса-миксина
    def __init__(self):
        super(Ninja, self).__init__()
        self.attackername = SpeechMixin.naming(self)
        self.attackercoming = "I'm as free as the dust in the solar wind"

class Karateboy(Fighter, SpeechMixin): # Наследование от класса-миксина
    def __init__(self):
        super(Karateboy, self).__init__()
        self.defendername = SpeechMixin.naming(self)
        self.defendercoming = "Alalalalallallalalalalalalalalllalala"

class Fight(Ninja, Karateboy, SpeechMixin): # Наследование от класса-миксина, множественное наследование
    def __init__(self):
        super(Fight, self).__init__()
        self.health = [self.health, self.health]
        self.hairstyle = SpeechMixin.hairstyle(self)

    @property
    def check(self): # декоратор проверки преусловия функции
        if not 0 in self.health:
            return True
        else:
            return False

    @property
    def fight(self): # декоратор вызова важного сценария
        while self.check:
            global fighter1
            i = random.randint(0, 1)
            self.health[i] -= 20

            if i + 1 == 1:
                fighter1 = self.attackername
                print(self.attackercoming)
                fighter2 = self.defendername
            else:
                fighter1 = self.defendername
                print(self.defendercoming)
                fighter2 = self.attackername
            if 0 not in self.health:
                print(fighter1, 'hits', fighter2)
                print(self.health[i], "Loser's HP left")
            else:
                print(fighter1, 'kills', fighter2)

        return self.hairstyle

    @property # декоратор финала
    def dance(self):
        return fighter1 + ' Dances (Use Your Imagination)'

Attraction = Fight()
print(Attraction.fight)
print(Attraction.dance)

