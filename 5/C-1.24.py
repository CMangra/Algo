myString = "....,,.,;sdfgdf.,.,.sdfg.,,,"
count = 0

newString = []

for element in myString:
    if element.isalpha():
        newString.append(element)

myString = ''.join(newString)
print(''.join(newString))