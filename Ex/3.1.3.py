StopIteration
ZeroDivisionError
AssertionError
ImportError
KeyError
SyntaxError
IndentationError
TypeError


def threw_ZeroDivisionError():
    a = 5 / 0
def threw_StopIteration():
    iterator = iter([])
    next(iterator)
def threw_AssertionError():
    assert False, "This is an assertion error"
def threw_ImportError():
    import blablablabla
def threw_KeyError():
    my_dict = {"a": 1, "b": 2}
    value = my_dict["c"] 
def threw_SyntaxError():
    ghgfjhcxh
def threw_IndentationError():
#def my_function():
    print("Hello")
def threw_TypeError():
    a = "string"
    b = 5
    c = a + b

def main():

    threw_TypeError()

if __name__ == "__main__":
    main()