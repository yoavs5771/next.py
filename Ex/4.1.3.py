import sys


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def first_prime_over(n):
    next_prime = (i for i in range(n + 1, sys.maxsize) if is_prime(i))
    print(next(next_prime))

if __name__ == "__main__":
    first_prime_over(10)
    first_prime_over(20)
    first_prime_over(30)
    first_prime_over(40)
    first_prime_over(50)
    first_prime_over(60)
    first_prime_over(70)
    first_prime_over(80)
    first_prime_over(90)
    first_prime_over(int(1e95))