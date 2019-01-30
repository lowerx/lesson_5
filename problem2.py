#!/usr/bin/env python3
#coding=utf-8

# print array like snake from [][]

def snake_array(inputArray):
    print("Problem 2")

    line = 3
    for i in range(len(inputArray)):
        if i / 2:
            for a in range(len(inputArray[line])):
                print(inputArray[line][a])
        else:
            for b in range(len(inputArray[line])):
                print(inputArray[line][len(inputArray) - 1 - b])

        line -= 1


