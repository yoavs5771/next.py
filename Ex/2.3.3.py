class animal:
    instance_count = 0
    def __init__(self, name="Jack"):
        self._name = name
        self._age = 5
        animal.instance_count += 1
    def birthday(self):
        self._age += 1
    def get_age(self):
        return self._age
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name
    
    
def main():
    A = animal("Octavio")
    B = animal()
    print(A.get_name())
    print(B.get_name())
    set_name = input("Enter a name for B: ")
    B.set_name(set_name)
    print(B.get_name())
    print(animal.instance_count, "animals created.")


if __name__ == "__main__":
    main()

