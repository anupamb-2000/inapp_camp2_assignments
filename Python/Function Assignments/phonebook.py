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
def sort():
    for item in sorted(phoneBook):
        print(f"Name : {item}, Phone Number : {phoneBook[item]}")
def add():
    name = input("Enter the name : ")
    number = int(input("Enter number : "))
    phoneBook[name] = number
    print("Record added to phonebook")

def delete():
    name = input("Enter name of contact to delete : ")
    del phoneBook[name]
    print("Record deleted from phonebook")

def searchname():
    name = input("Enter name of contact to search : ")
    if(name in phoneBook.keys()):
        print(f"Name : {name}, Number : {phoneBook[name]}")
    else:
        print("No such record found!")

def searchno():
    number = int(input("Enter number of contact to search : "))
    key_list = list(phoneBook.keys())
    val_list = list(phoneBook.values())
    if(number in val_list):
        print(f"Name : {key_list[val_list.index(number)]}, Number : {number}")
    else:
        print("No such record found!")



#Creating an empty dictionary
phoneBook = {}

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
    




