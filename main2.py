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
        print(f"{self.name} singing - coo")

    def info(self):
        print(f"{self.name} - name")
        print(f"{self.voice} - voice")
        print(f"{self.color} - bird color")

class Pidgeon(Bird):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def sing(self):
        print(f"{self.name} sing - cooing cooing")

    def walk(self):
        print(f"{self.name} walking")

bird1 = Pidgeon("CBuPenblu", "cooing", "grey", "seeds")

bird2 = Bird("MAKAPOHbl", "coo", "brown")

bird1.sing()
bird1.info()
bird1.walk()
