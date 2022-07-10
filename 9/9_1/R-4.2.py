"""
Aufgabe:

Draw the recursion trace for the computation of power(2,5), using the
traditional function implemented in Code Fragment 4.11.

@Chaitanya
Kommentar: Seite 202 im Buch

Tracetable:

Method call     x       n       return value
power(2,5)      2       5       2 * [power(2, 4)] -> 16 = 32
power(2,4)      2       4       2 * [power(2, 3)] -> 8 = 16
power(2,3)      2       3       2 * [power(2, 2)] -> 4 = 8
power(2,2)      2       2       2 * [power(2, 1)] -> 2 = 4
power(2,1)      2       1       2 * [power(2, 0)] -> 1 = 2
power(2,0)      2       5       1

"""


# Code Fragment 4.11: Compute the value x**n for integer n.
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


if __name__ == "__main__":
    print(power(2, 5))

