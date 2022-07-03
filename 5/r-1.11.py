
print("hello")

myList = [1, 2, 3, 4, 5, 6, 7, 8]

count = len(myList) -1

for i in range(0, int(len(myList)/2)):
    
    temp = myList[i]
    myList[i] = myList[count]
    myList[count] = temp
    count = count - 1
    
        
    

print(myList)
    
