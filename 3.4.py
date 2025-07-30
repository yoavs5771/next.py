import string
class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username, char):
        super().__init__()
        self.char = char
        self.index = username.index(char)

    def __str__(self):
        return (f"The username contains an illegal character \"{self.char}\" "
                f"at index {self.index}. Only letters, digits, and underscores are allowed.")
     
class UsernameTooShort(Exception):
    def __init__(self):
        super()
    def __str__(self):
        return "The username is too short."
class UsernameTooLong(Exception):
    def __init__(self):
        super()
    def __str__(self):
        return "The username is too long."
class PasswordTooShort(Exception):
    def __init__(self):
        super()
    def __str__(self):
        return "The password is too short."
class PasswordTooLong(Exception):
    def __init__(self):
        super()
    def __str__(self):
        return "The password is too long."
class PasswordMissingCharacter(Exception):
    def __init__(self, missing_type):
        super().__init__()
        self.missing_type = missing_type

    def __str__(self):
        return f"The password is missing a required character: {self.missing_type}."

class PasswordMissingUppercase(PasswordMissingCharacter):
    def __init__(self):
        super().__init__("an uppercase letter")

    def __str__(self):
        return super().__str__() + " (Uppercase)"

class PasswordMissingLowercase(PasswordMissingCharacter):
    def __init__(self):
        super().__init__("a lowercase letter")

    def __str__(self):
        return super().__str__() + " (Lowercase)"

class PasswordMissingDigit(PasswordMissingCharacter):
    def __init__(self):
        super().__init__("a digit")

    def __str__(self):
        return super().__str__() + " (Digit)"

class PasswordMissingSpecial(PasswordMissingCharacter):
    def __init__(self):
        super().__init__("a special character")

    def __str__(self):
        return super().__str__() + " (Special)"

def check_input(username, password):
    if not username or not password:
        raise ValueError("Username and password cannot be empty.")
    if not isinstance(username, str) or not isinstance(password, str):
        raise TypeError("Username and password must be strings.")
    if len(password) < 8:
        raise PasswordTooShort()
    if len(password) > 40:
        raise PasswordTooLong()
    if len(username) < 3:
        raise UsernameTooShort()
    if len(username) > 16:
        raise UsernameTooLong()
    if not any(char.isdigit() for char in password):
        raise PasswordMissingDigit()
    if not any(char.isupper() for char in password):
        raise PasswordMissingUppercase()
    if not any(char.islower() for char in password):
        raise PasswordMissingLowercase()
    if not any(char in string.punctuation for char in password):
        raise PasswordMissingSpecial()
    for char in username:
        if char not in string.ascii_letters + string.digits + "_":
            raise UsernameContainsIllegalCharacter(username, char)

    print("OK")
def main():
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        check_input(username, password)
    except (UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong,
            PasswordTooShort, PasswordTooLong, PasswordMissingCharacter, ValueError, TypeError) as e:
        print(e)
if __name__ == "__main__":
    main()