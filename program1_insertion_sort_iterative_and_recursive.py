"""
Experiment 1: Basic Sorting and Array Problems
Program 1: Insertion Sort (Iterative and Recursive)
Aim: Implement insertion sort using iterative and recursive approaches.
"""

def insertion_iterative(a):
    a = a[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def insertion_recursive(a, n=None):
    if n is None:
        a = a[:]
        n = len(a)
    if n <= 1:
        return a
    insertion_recursive(a, n - 1)
    key = a[n - 1]
    j = n - 2
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key
    return a

arr = [8, 4, 2, 9, 5]
print(insertion_iterative(arr))
print(insertion_recursive(arr))
