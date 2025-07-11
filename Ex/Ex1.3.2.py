def is_prime(number):
    return True if [num for num in range(2, number) if (number % num) == 0] == [] else False
