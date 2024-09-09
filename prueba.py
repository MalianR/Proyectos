class Animal(object):
    makes_noise: bool = False

    def make_noise(self):
        if self.makes_noise:
            print(self.sound())

    def sound(self) -> str:
        return "???"

class Cow(Animal):
    def __init__(self):
        self.makes_noise = True

    def sound(self) -> str:
        return "Moo"

c: Animal = None
c = Cow()
c.make_noise()  # Imprime "Moo"
