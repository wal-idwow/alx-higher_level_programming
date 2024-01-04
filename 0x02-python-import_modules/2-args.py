#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    list = len(sys.argv) - 1
    if list == 0:
        print("0 arguments.")
    elif list == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(list))
    for i in range(list):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
