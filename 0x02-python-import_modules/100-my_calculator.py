#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if op == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == "-":
        print("{} - {} = {}".format(a, b, add(a, b)))
    elif op == "/":
        print("{} / {} = {}".format(a, b, add(a, b)))
    elif op == "*":
        print("{} * {} = {}".format(a, b, add(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
