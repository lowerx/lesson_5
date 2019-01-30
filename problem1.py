#!/usr/bin/env python3
#coding=utf-8

# print main diagonal from multi_dimensional array


def mainDiagonal(array):
    print("Main diagonal:")

    result = ""

    for i in range(len(array)):
        x = i
        y = i
        result += str(array[x][y]) + " "

    result = result[:-1]
    print(result)


def incidentalDiagonal(array):
    print("Incidental diagonal:")

    result = ""

    for i in range(len(array)):
        x = i
        y = len(array[i]) - 1 - i
        result += str(array[x][y]) + " "

    result = result[:-1]
    print(result)
