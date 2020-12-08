import sys


# usage of functions
def test_function(s, b):
    r = s * 3
    if b:
        return r + '!!!'
    return r


def main():
    print(sys.argv)
    print(test_function("test", True))
    print(test_function("Blah", False))


if __name__ == '__main__':
    main()
