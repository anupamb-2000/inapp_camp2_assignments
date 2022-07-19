#Program to create the multiplication table(from 1 to 10) of a number getting input from the user

#get the number from the user
n = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")