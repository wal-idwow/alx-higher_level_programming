#!/usr/bin/python3
"""
module containing a script that reads stdin line by line and computes metrics.
Every 10 lines and after a keyboard interruption (CTRL + C), it prints the statistics
since the beginning:
File size: File size: <total size> (the sum of all previous sizes)
Number of lines by status code:
Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500
If a status code doesnt appear, dont print anything for that status code.
Format: <status code>: <number>
Status codes should be printed in ascending order.
"""

import sys

SIZE = 0
status_code_count = {"200": 0, "301": 0, "400": 0, "401": 0,
                     "403": 0, "404": 0, "405": 0, "500": 0}

COUNT = 0

try:
    # iterate over each line in stdin
    for line in sys.stdin:
        tokens = line.split()

        if len(tokens) >= 2:
            current_line_count = COUNT
            status_code = tokens[-2]

            if status_code in status_code_count:
                status_code_count[status_code] += 1
                COUNT += 1

            try:
                file_size = int(tokens[-1])
                SIZE += file_size
                if current_line_count == COUNT:
                    COUNT += 1
            except ValueError:
                if current_line_count == COUNT:
                    continue

        # print statistics every 10 lines
        if COUNT % 10 == 0:
            print(f"File size: {SIZE}")
            for code in sorted(status_code_count):
                if status_code_count[code]:
                    print(f"{code}: {status_code_count[code]}")

    # print final statistics after processing all input lines
    print(f"File size: {SIZE}")
    for code in sorted(status_code_count):
        if status_code_count[code]:
            print(f"{code}: {status_code_count[code]}")

except KeyboardInterrupt:
    # print final statistics on keyboard interruption (Ctrl + C)
    print(f"File size: {SIZE}")
    for code in sorted(status_code_count):
        if status_code_count[code]:
            print(f"{code}: {status_code_count[code]}")
