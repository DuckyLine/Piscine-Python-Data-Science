import sys

def main():
	if (len(sys.argv) == 1): return

	if (len(sys.argv) != 2):
		print("AssertionError: more than one argument is provided")
		return

	try:
		n = int(sys.argv[1])
		if (n % 2 == 0): print("I'm Even.")
		else: print("I'm Odd.")

	except:
		print("AssertionError: argument is not an integer")

if (__name__ == "__main__"): main()
