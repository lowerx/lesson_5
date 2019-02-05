#!/usr/bin/env python3
#coding=utf-8

# print array like snake from [3][0]


def snake_array(array):
    print("Snake array")

    result = ""

    for i in range(len(array)):
        if i % 2 == 0:
            for a in range(len(array)):
                x = len(array) - 1 - i
                y = a

                result += str(array[x][y]) + " "

        else:
            for b in range(len(array)):
                x = len(array) - 1 - i
                y = len(array) - 1 - b

                result += str(array[x][y]) + " "

    result = result[:-1]
    print(result)

def snake_array_vertical(array):
    print("Vertical snake array")

    result = ""

    for d in range(len(array)):
        if d % 2 == 0:
            for a in range(len(array)):
                x = len(array) - 1 - a
                y = d

                result += str(array[x][y]) + " "

        else:
            for b in range(len(array)):
                x = b
                y = d

                result += str(array[x][y]) + " "

    result = result[:-1]
    print(result)

