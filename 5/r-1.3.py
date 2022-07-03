
print("hello")

def squareSmallerNumbersThanMe(n):
    
    sum = 0
    
    for i in range(1, n):
        sum = sum + i*i
        
    return sum

print(squareSmallerNumbersThanMe(3000000))
