"""
Aufgabe:

Describe a recursive algorithm for finding the maximum element in a sequence, S, of n elements.
What is your running time and space usage

@Chaitanya
Time complexity: O(n)
Space complexity: O(n)
"""


def max_element(S, n):
    if n == 1:
        return S[0]
    return max(S[n - 1], max_element(S, n - 1))


if __name__ == "__main__":
    S = [1, 2, 3, 69, 4, -5]
    print(max_element(S, len(S)))
