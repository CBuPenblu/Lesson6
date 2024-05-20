class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color
    def fly(self):
        print(f"{self.name} flying")

    def eat(self):
        print(f"{self.name} eating")

    def sing(self):
        print(f"{self.name} singing - {self.voice}")

    def info(self):
        print(f"{self.name} - name")
        print(f"{self.voice} - voice")
        print(f"{self.color} - bird color")

class Pidgeon(Bird):
    pass

bird1 = Pidgeon("CBuPenblu", "cooing", "grey")

bird1.sing()
bird1.info()