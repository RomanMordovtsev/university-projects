import random

class SpeechMixin:
    def hairstyle(self):
        self.variants = ['"My hairstyle is perfect" - says the Winner', '"My hairstyle is amazing" - says the Winner', '"My hairstyle is brilliant" - says the Winner']
        return random.choice(self.variants)

    def naming(self):
        return input("Fighter's name is ")



