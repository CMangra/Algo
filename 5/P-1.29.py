import random
import string


def find_brute(t, p):
    n, m = len(t), len(p)
    for i in range(n-m+1):
        k = 0
        while k < m and t[i + k] == p[k]:
            k += 1
        if k == m:
            return i
    return -1

def find_boyer_moore(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    last = { }
    for k in range(m):
        last[pattern[k]] = k
    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i 
            else:
                i -= 1 
                k -= 1 
        else:
            j = last.get(text[i], -1) 
            i += m - min(k, j + 1)
            k = m - 1 
    return -1


Text = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for i in range(1000000))

Pattern = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for i in range(3))

i = find_brute(Text, Pattern)

print("Brute Force:")
print(i)

if i>=0:
    print(Text[i: i + len(Pattern)])
else:
    print("nicht gefunden")




i = find_boyer_moore(Text, Pattern)
print("boyer-moore:")
if i >= 0:
    print("pattern found in: ")
    print(i)
else:
    print("pattern not found by the boyer-moore-algorithm")


print("searched pattern:\n" + Pattern)