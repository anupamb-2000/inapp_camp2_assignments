#Create a simple phone book app using dictionary in python
#On starting the program give choiceto the user, 
#1. List all contacts(sorted in alphabetical order)
#2. Add a new contact
#3. Search by name
#4. Search by number
#Create functions for :
#searchname()
#searchno()
#add()
#delete()
#sort()
from unicodedata import name


def sort():
    f = open("phonebook.txt", "r")
    phoneBook = f.readlines()
    names = []
    entries = []
    for record in phoneBook:
        entry = record.split("\n")[0].split(",")
        entries.append(entry)
        names.append(entry[0])
    # names = sorted(names)
    # print(list(zip(names, entries))) #zip the listes together
    # print(list(sorted(zip(names, entries)))) #sort the combined list based on the first list
    # print(list(zip(*sorted(zip(names, entries))))) #unzip the sorted list into two seperate lists
    names, entries = zip(*sorted(zip(names, entries)))
    for entry in entries:
        print(f" Name : {entry[0]}\n Number : {entry[1]}")
    f.close()
def add():
    f = open("phonebook.txt", "a")
    name = input("Enter the name : ")
    number = int(input("Enter number : "))
    f.write(f"{name},{number}\n")
    print("Record added to phonebook")
    f.close()

def delete():
    f = open("phonebook.txt", "r")
    phoneBook = f.readlines()
    f.close()
    f = open("phonebook.txt", "w")
    name = input("Enter name of contact to delete : ")
    for record in phoneBook:
        entry = record.split("\n")[0].split(",")
        if entry[0] != name:
            f.write(f"{record}")
    print("Record deleted from phonebook")
    f.close()

def searchname():
    f = open("phonebook.txt", "r")
    phoneBook = f.readlines()
    f.close()
    names = []
    print(names)
    for record in phoneBook:
        names.append(record.split("\n")[0].split(",")[0])
    name = input("Enter name of contact to search : ")
    if(name in names):
        for record in phoneBook:
            entry = record.split("\n")[0].split(",")
            if entry[0] == name:
                print(f" Name : {entry[0]}\n Number : {entry[1]}")
    else:
        print("No such record found!")

def searchno():
    f = open("phonebook.txt", "r")
    phoneBook = f.readlines()
    f.close()
    numbers = []
    for record in phoneBook:
        numbers.append(record.split("\n")[0].split(",")[1])
    number = input("Enter number of contact to search : ")
    for record in phoneBook:
        if(number in numbers):
            entry = record.split("\n")[0].split(",")
            print(f" Name : {entry[0]}\n Number : {entry[1]}")
        else:
            print("No such record found!")


#Displaying Menu for the user
while(True):
    print("Menu :")
    print("\t1. List all contacts")
    print("\t2. Add a new contact")
    print("\t3. Search by name")
    print("\t4. Search by number")
    print("\t5. Delete")
    print("\t6. Exit")
    choice = int(input("Enter your choice:"))
    match choice:
        case 1:
            sort()
        case 2:
            add()
        case 3:
            searchname()
        case 4:
            searchno()
        case 5: 
            delete()
        case 6:
            exit()
        case _:
            print("Invalid Input!")
    




