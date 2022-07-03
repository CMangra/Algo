vowels = ["a","e","i","o","u","A","E","I","O","U"]

myString = "hello world"
count = 0

for element in myString:
    if element in vowels:
        count = count + 1

print("Total number of vowels is: " + str(count))