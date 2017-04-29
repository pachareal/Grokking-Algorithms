#!/usr/bin/python3


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        index = (low + high) // 2
        num = list[index]

        if num < item:
            low = index + 1
        elif num > item:
            high = index - 1
        elif num == item:
            return index

    return None


test = [1, 3, 5, 7, 9]

print(test)
print(binary_search(test, 1))
print(binary_search(test, 5))
print(binary_search(test, 9))
print(binary_search(test, -25))