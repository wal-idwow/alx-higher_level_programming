#!/usr/bin/python3
def pascal_triangle(n):
    """ Pascals triangle of n"""
    lists = []
    if n <= 0:
        return lists
    for x in range(n):
        for i in range(x + 1):
            if i == 0:
                lists.append([1])
            elif i == x:
                lists[x].append(1)
            else:
                lists[x].append(lists[x - 1][i] + lists[x -1][i - 1])
        return lists
