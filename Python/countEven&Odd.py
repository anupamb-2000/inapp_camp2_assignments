#Program to count even and odd numbers in a list
myList = [20, 10, 30, 60, 8, 1, 7, 11, 50]
print("List: ",myList)

oddCount = 0
evenCount = 0

for i in myList:
    if i % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1

#print the counts
print("Odd Count: ", oddCount)
print("Even Count: ", evenCount)