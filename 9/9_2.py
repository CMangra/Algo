"""
Aufgabe:

A trivial recursive definition of the power function follows from the fact that x^n = x × x^n−1 for n > 0:

power(x, n) = 1 when n = 0
otherwise power(x, n) = x × power(x, n − 1)

Implement this function and determine its running time complexity.

@Chaitanya
Time complexity: O(n)
"""


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


if __name__ == "__main__":
    print(power(2, 5))
