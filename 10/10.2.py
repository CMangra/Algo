"""
Aufgabe:

Implement merge(S1, S2, S) for merge sort.

@Chaitanya
Kommentar: funktioniert

"""


def merge(S1, S2, S):
    finished = False
    i = 0
    j = 0
    while not finished:
        if i != len(S1) and j != len(S2) and S1[i] < S2[j]:
            S[i + j] = S1[i]
            i += 1
        elif j != len(S2):
            S[i + j] = S2[j]
            j += 1
        elif i != len(S1):
            S[i + j] = S1[i]
            i += 1
        if i == len(S1) and j == len(S2):
            finished = True


def merge_sort(S):
    n = len(S)
    if n < 2:
        return
    mid = n // 2
    S1 = S[: mid]
    S2 = S[mid:]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)


if __name__ == '__main__':
    S = [1, 4, 69, 3, -69, 10]
    merge_sort(S)
    print(S)
