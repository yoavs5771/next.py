def read_file(file_name):
    try:
        f = open(file_name)
    except FileNotFoundError:
        print("__CONTENT_START__")
        print("__NO_SUCH_FILE__")
        print("__CONTENT_END__")
    else:
        print("__CONTENT_START__")
        print(f.read(), end="")
        print("__CONTENT_END__")

def main():
    read_file("names.txt")
    print("\n==========================\n")
    read_file("not_real_file.txt")
if __name__ == "__main__":
    main()

