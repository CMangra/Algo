"""
Aufgabe:

Write a short recursive Python function that determines if a string s is a
palindrome, that is, it is equal to its reverse. For example, 'racecar' and
'gohangasalamiimalasagnahog' are palindromes.

@Chaitanya
Kommentar: Seite 203 im Buch

"""


def is_palindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


if __name__ == "__main__":
    print(is_palindrome("gohangasalamiimalasagnahog"))
    print(is_palindrome("racecar"))
