#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    total_sum = sum(int(arg) for arg in arguments)
    print(total_sum)
