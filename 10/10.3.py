"""
Aufgabe:

Implement a randomized quicksort, which randomly picks the pivot element. This algorithm has a
worst-case expected running time complexity of O(n log n). Compare its execution time to the quicksort
algorithm shown in class. Use various data sets of 10 000 or more elements, including a data set that is
already sorted. What do you observe?
Note on randomized quicksort: Its absolute worst-case is still O(n^2), yet it is very unlikely: “The
probability that quicksort will use a quadratic number of compares when sorting a large array on your
computer is much less than the probability that your computer will be struck by lightning.”.

@Chaitanya
Kommentar: funktioniert
"""

import random


def return_list_except_pivot(S, p):
    return_list = []
    flag = False
    for element in S:
        if element == p and not flag:
            flag = True
        else:
            return_list.append(element)
    return return_list


def quick_sort(S):
    if len(S) <= 1:
        return S
    left = []
    right = []
    pivot = S[random.randint(0, len(S) - 1)]
    for element in S:
        if element >= pivot:
            right.append(element)
        else:
            left.append(element)
    left = quick_sort(left)
    right = quick_sort(return_list_except_pivot(right, pivot))
    return left + [pivot] + right


if __name__ == '__main__':
    S = [1, 3, 69, -1, 600, -69, 30, 92, -600]
    print(quick_sort(S))

    L = []
    for i in range(10000):
        S.append(i)

    print(quick_sort(S))
