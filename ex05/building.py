import sys

def errorParsing() -> bool:
    """
    Check if a parsing is good and return a correct error message.

    Return true if yes.

    Return false if no
    """
    length = len(sys.argv)

    if (length != 2):
        print("Error: The program must have 1 argument to work")
        return (False)

    return (True)


def getWithFuncion(str: str, func) -> int:
    """
    Itter on str with a function

    Return the number or the function is true
    """
    count = 0

    for c in str:
        if (func(c)):
            count += 1

    return (count)


def isPunctuation(char: str) -> bool:
    """
    Return true if the char is a punctuation and false is not
    """
    punctuation = "!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~"

    for c in punctuation:
        if (c == char): return (True)

    return (False)


def isSpace(c: str) -> bool:
    """
    Return true if the char is a space and false is not
    """
    if (c == " "): return(True)

    return (False)


def main():
    """
    Prints messages and check for errors
    """
    if (errorParsing() == False): return

    arg = sys.argv[1]
    print(f"The text contains {len(arg)} characters:")
    print(f"{getWithFuncion(arg, str.isupper)} upper letters")
    print(f"{getWithFuncion(arg, str.islower)} lower letters")

    print(f"{getWithFuncion(arg, isPunctuation)} punctuation marks")
    print(f"{getWithFuncion(arg, isSpace)} spaces")
    print(f"{getWithFuncion(arg, str.isdigit)} digits")


if (__name__ == "__main__"):
    main()
