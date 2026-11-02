"""
Experiment 1: Basic Sorting and Array Problems
Program 3: Majority Element
Aim: Find an element occurring more than n/2 times using Moore's Voting Algorithm.
"""

def majority_element(a):
    candidate = None
    count = 0
    for x in a:
        if count == 0:
            candidate = x
        count += 1 if x == candidate else -1
    if candidate is not None and a.count(candidate) > len(a) // 2:
        return candidate
    return -1

print(majority_element([2, 2, 1, 2, 3, 2, 2]))
