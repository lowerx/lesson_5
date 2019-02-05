#!/usr/bin/env python3
#coding=utf-8

# transposition around main diagonal

def main_transposition(array):
    print("Main transposition:")

    result = ""
    x = 0
    y = 0

    for i in range(len(array)):
        for a in range(len(array)):
            x = a
            y = i

            result += str(array[x][y]) + " "

        result = result[:-1]
        result += "\n"

    print(result)

# transposition around incidental diagonal

def incidental_transposition(array):
    print("Incidental transposition:")

    result = ""
    x = 0
    y = 0

    for i in range(len(array)):
        for b in range(len(array)):
            x = len(array) - 1 - b
            y = len(array) - 1 - i
            result += str(array[x][y]) + " "

        result = result[:-1]
        result += "\n"

    print(result)






