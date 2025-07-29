class Animal:
    zoo_name = "Hayaton"
    def __init__(self, name,hunger_ = 0):
        self.name = name
        self.hunger_ = hunger_
    def get_name(self):
        return self.name
    def is_hungry(self):
        return self.hunger_ > 0
    def feed(self):
        if self.is_hungry():
            self.hunger_ -= 1
    
class Dog(Animal):
    def __init__(self, name, hunger_):
        super().__init__(name, hunger_)
        self.hunger_ = hunger_
    def talk(self):
        return "Woof Woof"
    def fetch_stick(self):
        return "There you go, sir!"
class Cat(Animal):
    def __init__(self, name, hunger_):
        super().__init__(name, hunger_)
        self.hunger_ = hunger_
    def talk(self):
        return "Meow"
    def chase_laser(self):
        return "Meeeeow"
class Skunk(Animal):
    def __init__(self, name, hunger_, _stink_count = 6):
        super().__init__(name, hunger_)
        self.hunger_ = hunger_
        self._stink_count = _stink_count
    def talk(self):
        return "tsssss"
    def stink(self):
        return "Dear lord!"
class Unicorn(Animal):
    def __init__(self, name, hunger_):
        super().__init__(name, hunger_)
        self.hunger_ = hunger_
    def talk(self):
        return "Good day, darling"
    def sing(self):
        return "I’m not your toy..."
class Dragon(Animal):
    def __init__(self, name, hunger_, _color = "Green"):
        super().__init__(name, hunger_)
        self.hunger_ = hunger_
        self._color = _color
    def talk(self):
        return "Raaaawr"
    def breath_fire(self):
        return "$@#$#@$"

def main():
    zoo_lst = [
        Dog("Brownie", 10), 
        Cat("Zelda", 3), 
        Skunk("Stinky", 0), 
        Unicorn("Keith", 7), 
        Dragon("Lizzy", 1450),
        Dog("Doggo", 80), 
        Cat("Kitty", 80), 
        Skunk("Stinky Jr.", 80), 
        Unicorn("Clair", 80), 
        Dragon("McFly", 80)
    ]
    for animal in zoo_lst:
        while animal.is_hungry():
            animal.feed()
        print(type(animal).__name__, animal.get_name())
        print(animal.talk())
        
        if isinstance(animal, Dog):
            print(animal.fetch_stick())
        if isinstance(animal, Cat):
            print(animal.chase_laser())
        if isinstance(animal, Skunk):
            print(animal.stink())
        if isinstance(animal, Unicorn):
            print(animal.sing())
        if isinstance(animal, Dragon):
            print(animal.breath_fire())
    print("Zoo name:", Animal.zoo_name)
if __name__ == "__main__":
    main()
