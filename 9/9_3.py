"""
Aufgabe:

There is a much faster way to compute the power function using an alternative definition that employs
a squaring technique:

power(x, n) =

1 when n = 0
power(x, n/2)^2 if n > 0 is even
x × power(x, [[n/2]])^2 if n > 0 is odd

Let [[n/2]] denote the floor of the division (expressed as n // 2 in Python).
Implement this function and determine its running time complexity.

@Chaitanya
Time complexity: O(n/2) = O(n)
"""


def power(x, n):
    if n == 0:
        return 1
    elif n % 2.0 == 0:
        return power(x, n / 2) * power(x, n / 2)
    else:
        return x * power(x, n // 2) * power(x, n // 2)


if __name__ == '__main__':
    print(power(2, 5))
