
print("hello")

def sumOfOddPositiveInteger(n):
    return sum(i*i for i in range(1, n, 2))

print(sumOfOddPositiveInteger(6))
