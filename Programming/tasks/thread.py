from fighter import Fighter
import threading

class FighterThread(Fighter, threading.Thread): # Создание класса для вторичного потока
    def __init__(self):
        Fighter.__init__(self)
        threading.Thread.__init__(self) 