from thread import FighterThread
from exc import Exceptiki

class Ninja(FighterThread, Exceptiki): # Реализация вторичного потока
    def __init__(self):
        super(Ninja, self).__init__()
        self.attackername = Exceptiki.nam(self)
        self.attackercoming = "I'm as free as the dust in the solar wind"
        self.specific = 'Ninja'

    def getName(self):
        return self.attackername

    def getSpec(self):
        return self.specific




