
print("hello")

def minmax(data):
    
    min = data[0]
    max = data[0]
    
    for element in data:
        if (element < min):
            min = element
        if (element > max):
            max = element
    
    return [min, max]





print(minmax([2]))
