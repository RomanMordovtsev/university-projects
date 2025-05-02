import random

class Fighter:
    def __init__(self, name):
        self.health = 100

    def __add__(self, other):
        return self.health & other.health

    def __eq__(self, other):
        return self.health == other.health

class Ninja(Fighter):
    def __init__(self, name):
        super(Ninja, self).__init__('Alisher Morgenshtern')
        self.attackername = name

    def _hairstyle(self):
        print("My hairstyle is perfect")

    def coming(self):
        print("I'm as free as the dust in the solar wind")

class Karateboy(Fighter):
    def __init__(self, name):
        super(Karateboy, self).__init__('')
        self.defendername = name

    def _hairstyle(self):
        print("My hairstyle is perfect")

    def coming(self):
        print("Alalalalallallalalalalalalalalllalala")

class Fight(Ninja, Karateboy):
    def __init__(self):
        super(Fight, self).__init__('Slava Marlow')
        self.health = [self.health, self.health]
        Shaolin = Karateboy('Slava')
        Shaolin.coming()
        Ice = Ninja('Alisher')
        Ice.coming()
        self.h = Shaolin + Ice
        self.e = Shaolin == Ice


    def fight(self):
        while not 0 in self.health:
            i = random.randint(0, 1)
            self.health[i] -= 20
            if i == 0:
                j = 2
            else:
                j = 1

            if i + 1 == 1:
                fighter1 = self.attackername
                fighter2 = self.defendername
            else:
                fighter1 = self.defendername
                fighter2 = self.attackername
            if 0 not in self.health:
                print(fighter1, 'hits', fighter2)
                print(self.health[i], "Loser's HP left")
            else:
                print(fighter1, 'kills', fighter2)
                print(self.health[i], "Loser's HP left")

        print(self.h)
        print(self.e)

Attraction = Fight()
Attraction.fight()
