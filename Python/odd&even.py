#Python program to print odd and even nos. seperately in a list
myList = [1,2,3,4,5,6,7,8,9,10]
print("List: ",myList)

#seperating the list
oddList = myList[::2]
evenList = myList[1::2]

#print the lists
print("Odd List: ", oddList)
print("Even List: ", evenList)