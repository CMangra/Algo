from itertools import permutations
 

myString = ['c','a','t','d','o','g']

perm = permutations(myString)
 
for element in list(perm):
    print (element)