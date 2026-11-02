"""
Experiment 1: Basic Sorting and Array Problems
Program 2: Dutch National Flag
Aim: Sort an array containing only 0, 1 and 2 in one traversal.
"""

def dutch_flag(a):
    a = a[:]
    low = mid = 0
    high = len(a) - 1
    while mid <= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid], a[high] = a[high], a[mid]
            high -= 1
    return a

print(dutch_flag([2, 0, 1, 2, 1, 0, 0]))
