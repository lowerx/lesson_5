#!/usr/bin/env python3
#coding=utf-8

# print array like snake from [3][0]


def snake_array(array):
    print("Snake array")

    result = ""
    x = 0
    y = 0

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
        result += "\n"
    print(result)


