from abc import ABC


class Fighter(ABC):
    def __init__(self):
        self.health = 100

    def __add__(self, other):
        return self.health & other.health

    def coming(self):
        pass



