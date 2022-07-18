#Python program to find the second largest number in a list
myList = [20, 10, 30, 60, 8, 50]
print("List: ",myList)

#Sorting
myList.sort()
print("Sorted List: ", myList)

#print the second largest element(second last in sorted list)
print("Second Largest Element: ",myList[-2])