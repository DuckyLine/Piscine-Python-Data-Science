import sys


def parsingError() -> bool:
    """
    This function can parse errors.

    Return true if there is an any error.

    Return false if there are no error.
    """
    if (len(sys.argv) != 2):
        print("AssertionError: the arguments are bad")
        return (True)
    
    arg = sys.argv[1]

    for elem in arg:
        if (elem != ' ' and not elem.isalnum()):
            print("AssertionError: the arguments are bad")
            return (True)

    return (False)


def main():
    """
    Create a correct dictionaries for morse translation and print the message.
    """
    if (parsingError()):
        return
    
    morse_dict = {"a" : ".-",
                  "b" : "-...",
                  "c" : "-.-.",
                  "d" : "-..",
                  "e" : ".",
                  "f" : "..-.",
                  "g" : "--.",
                  "h" : "....",
                  "i" : "..",
                  "j" : ".---",
                  "k" : "-.-",
                  "l" : ".-..",
                  "m" : "--",
                  "n" : "-.",
                  "o" : "---",
                  "p" : ".--.",
                  "q" : "--.-",
                  "r" : ".-.",
                  "s" : "...",
                  "t" : "-",
                  "u" : "..-",
                  "v" : "...-",
                  "w" : ".--",
                  "x" : "-..-",
                  "y" : "-.--",
                  "z" : "--..",
                  "z" : "--..",
                  "0" : "-----",
                  "1" : ".----",
                  "2" : "..---",
                  "3" : "...--",
                  "4" : "....-",
                  "5" : ".....",
                  "6" : "-....",
                  "7" : "--...",
                  "8" : "---..",
                  "9" : "----."
                  }
    
    arg = sys.argv[1]
    len = arg.__len__()
    output = ""
    i = 0

    for c in arg:
        i += 1
        
        if (c.isalnum()):
            output += morse_dict[c.lower()]
        
        if (i < len and arg[i] != ' '):
            output += " "
        elif (i < len and arg[i] == ' '):
            output += " /"
    
    print(output)


if (__name__ == "__main__"):
    main()