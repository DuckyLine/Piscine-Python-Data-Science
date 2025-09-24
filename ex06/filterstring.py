import sys


def errorParsing() -> bool:
    """
    Check if a parsing is good and return a correct error message.

    Return true if yes.

    Return false if no.
    """
    length = len(sys.argv)

    if (length != 3):
        print("AssertionError: the arguments are bad")
        return (False)

    return (True)


def makeList(src: str, n: int):
    """
    Make a list and print this.
    """
    list_src = src.split(' ')
    list_result = []

    for elem in list_src:
        if (len(elem) > n):
            list_result.append(elem)

    print(list_result)


def main():
    """
    Execute and check for errors.
    """
    if (not errorParsing()):
        return

    try:
        src = str(sys.argv[1])

        try:
            n = int(sys.argv[2])
            makeList(src, n)

        except (ValueError):
            print("AssertionError: the arguments are bad")

    except (ValueError):
        print("AssertionError: the arguments are bad")


if (__name__ == "__main__"):
    main()
