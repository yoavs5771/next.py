def is_div_four(num):
    return num % 4 == 0
def four_dividers(number):
    return list(filter(is_div_four ,list(range(1, number))))