"""
Aufgabe:

The bubble sort implementation we discussed in class has a best-case running time complexity of O(n^2).
Implement a better bubble sort that has a best-case running time complexity of O(n). Hint: stop as
early as possible, i.e. if the sequence was not altered at all in the previous iteration.

@Chaitanya
Best-case running time complexity: O(2n) = O(n)

"""


def bubble_sort(A):
    n = len(A)
    flag = True
    for i in range(n):
        if flag:
            flag = False
            for j in range(n - i - 1):
                if A[j] > A[j + 1]:
                    flag = True
                    tmp = A[j]
                    A[j] = A[j + 1]
                    A[j + 1] = tmp


if __name__ == '__main__':
    S = [-69, 1, 4, 10, 55, 69]
    bubble_sort(S)
    print(S)
