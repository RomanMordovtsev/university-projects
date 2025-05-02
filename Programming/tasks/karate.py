from thread import FighterThread
from exc import Exceptiki

class Karateboy(FighterThread, Exceptiki): # Реализация вторичного потока
    def __init__(self):
        super(Karateboy, self).__init__()
        self.defendername = Exceptiki.nam(self)
        self.defendercoming = "Alalalalallallalalalalalalalalllalala"
        self.specific = 'Karate'

    def getName(self):
        return self.defendername

    def getSpec(self):
        return self.specific



