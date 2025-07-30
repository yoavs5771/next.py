class Under18(Exception):
    def __init__(self, age):
        self.age = age
    def __str__(self):
        return f"Age {self.age} is under 18, access denied. you can come back more {18 - int(self.age)} years."

def send_invitation(name, age):
    if int(age) < 18:
        raise Under18(age)
    else:
        print("You should send an invite to " + name)
def main():
    try:
        name = input("Enter the name of the person: ")
        age = input("Enter the age of the person: ")
        send_invitation(name, age)
    except Under18 as e:
        print(e)
if __name__ == "__main__":
    main()