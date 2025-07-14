class animal:
    def __init__(self):
        self.name = "Jack"
        self.age = 5
    def birthday(self):
        self.age += 1
    def get_age(self):
        return self.age
def main():
    a = animal()
    print(a.name)
    print(a.get_age())
    a.birthday()
    print(a.get_age())
    b = animal()
    print(b.get_age())
if __name__ == "__main__":
    main()