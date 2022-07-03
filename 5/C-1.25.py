v = [4,3]



def norm(v,p):
    sum = 0
    for element in v:
        sum = sum + element**p
    
    return sum**(1/p)

print(norm(v,2))