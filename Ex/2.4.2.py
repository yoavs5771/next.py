class BigThing:
    def __init__(self, name):
        self.name = name
    def size(self , _size):
        if type(_size) is int:
            self.size = _size
        else:
            return len(_size)
class BigCat(BigThing):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight
        if self.weight > 15:
            return "Fat"
        elif self.weight > 20:
            return "very fat"
