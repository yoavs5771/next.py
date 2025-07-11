def is_funny_in_one_line(string):
    return True if [char for char in string if char != 'h' and char != 'a'] == [] else False

def is_funny(string):
    for char in string:
        if char != 'h' and char != 'a':
            return False
    return True

main_string = "hahahahahahahahahahahahahahahahahahahahahahahahahahahahaha"
print(is_funny_in_one_line(main_string))
print(is_funny(main_string))
# Output:
# True
# True
main_string_2 = "hahahahahahahahjhdhfgjgahahahahahahahahahahb"
print(is_funny_in_one_line(main_string_2))
print(is_funny(main_string_2))
# Output:
# False
# False