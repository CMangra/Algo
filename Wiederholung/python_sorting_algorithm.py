data1 = [3, 2, 1, 20, 15, 12]

print(sorted(data1))

print(sorted(data1, reverse = True))

data2 = [('red',1), ('blue',1), ('red',2), ('blue',2)]

from operator import itemgetter

#at each element from the list the sorter is looking at, i'm looking at the subelement at index 1
print(sorted(data2, key=itemgetter(1)) )

print(sorted(data2, key=itemgetter(1),reverse=True) )