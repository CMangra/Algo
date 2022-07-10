"""
Aufgabe:
Write a short recursive Python function that finds the minimum and maximum values in a sequence without using any loops.

Kommentar: Seite 202 im Buch

"""


def max_and_min(S, n):
    def max_elements(S, n):
        if n == 1:
            return S[0]
        return max(S[n - 1], max_elements(S, n - 1))

    def min_elements(S, n):
        if n == 1:
            return S[0]
        return min(S[n - 1], min_elements(S, n - 1))

    return max_elements(S, n), min_elements(S, n)


if __name__ == "__main__":
    S = [1, 2, 3, 69, 4, -5]
    max_and_min = max_and_min(S, len(S))
    maximum = max_and_min[0]
    minimum = max_and_min[1]
    print("Maximum : " + str(maximum) + "\nMinimum : " + str(minimum))
