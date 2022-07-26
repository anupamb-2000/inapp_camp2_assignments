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

import pyodbc

def display(phoneBook):
    #Displaying the results
    for record in phoneBook:
        print(f"\tName : {record['Name']}, Number : {record['Number']} ")

def sort():
    #create a connection with the connection string
    myconn = pyodbc.connect(myConString)
    try: 
        #get the cursor object
        mycursor = myconn.cursor()
        #get the contents 
        mycursor.execute("SELECT * FROM phonebook ORDER BY name")
    except Exception as e:
        print(f"{type(e).__name__}")
    else:
        #saving the result into a dictionary
        phoneBook = [{'Name': row[0], 'Number': row[1]} for row in mycursor.fetchall()]
        display(phoneBook)
    myconn.commit()
    myconn.close()

def add():
    #create a connection with the connection string
    myconn = pyodbc.connect(myConString)
    try: 
        #get the cursor object
        mycursor = myconn.cursor()
        name = input("Enter the name : ")
        number = int(input("Enter number : "))
        #insert into the table
        mycursor.execute("INSERT INTO phonebook VALUES (?, ?)", (name, number))
    except Exception as e:
        print(f"{type(e).__name__}")
    else:
        print("Record added to phonebook")

    myconn.commit()
    myconn.close()

def delete():
    #create a connection with the connection string
    myconn = pyodbc.connect(myConString)
    try: 
        #get the cursor object
        mycursor = myconn.cursor()
        name = input("Enter name of contact to delete : ")
        #check if present in the table
        mycursor.execute(f"SELECT COUNT(*) FROM phonebook WHERE name = '{name}'")
        if mycursor.fetchall()[0][0] > 0:
            try:
                mycursor.execute(f"DELETE FROM phonebook WHERE name = '{name}'")
            except Exception as e:
                print(f"{type(e).__name__}")
            else:
                print("Record deleted from phonebook")
        else:
            print("No such record found!")
    except Exception as e:
        print(f"{type(e).__name__}")

    myconn.commit()
    myconn.close()

def searchname():
    #create a connection with the connection string
    myconn = pyodbc.connect(myConString)
    try: 
        #get the cursor object
        mycursor = myconn.cursor()
        name = input("Enter name of contact to search : ")
        #check if present in the table
        mycursor.execute(f"SELECT COUNT(*) FROM phonebook WHERE name = '{name}'")
        if mycursor.fetchall()[0][0] > 0:
            try:
                mycursor.execute(f"SELECT * FROM phonebook WHERE name = '{name}'")
            except Exception as e:
                print(f"{type(e).__name__}")
            else:
                #saving the result into a dictionary
                phoneBook = [{'Name': row[0], 'Number': row[1]} for row in mycursor.fetchall()]
                display(phoneBook)
        else:
            print("No such record found!")
    except Exception as e:
        print(f"{type(e).__name__}")

    myconn.commit()
    myconn.close()

def searchno():
    #create a connection with the connection string
    myconn = pyodbc.connect(myConString)
    try: 
        #get the cursor object
        mycursor = myconn.cursor()
        number = int(input("Enter number of contact to search : "))
        #check if present in the table
        mycursor.execute(f"SELECT COUNT(*) FROM phonebook WHERE number = '{number}'")
        if mycursor.fetchall()[0][0] > 0:
            try:
                mycursor.execute(f"SELECT * FROM phonebook WHERE number = '{number}'")
            except Exception as e:
                print(f"{type(e).__name__}")
            else:
                #saving the result into a dictionary
                phoneBook = [{'Name': row[0], 'Number': row[1]} for row in mycursor.fetchall()]
                display(phoneBook)
        else:
            print("No such record found!")
    except Exception as e:
        print(f"{type(e).__name__}")

    myconn.commit()
    myconn.close()



#create a connection string
myConString = 'Driver={SQL Server};Server=DESKTOP-517KMB6\SQLEXPRESS;Database=phonebook_db;Trusted_Connection=yes;'

#create a connection with the connection string
myconn = pyodbc.connect(myConString)
try: 
    #get the cursor object
    mycursor = myconn.cursor()
    #create a new table for storing the records
    mycursor.execute('''CREATE TABLE phonebook(
	  name varchar(50),
	  number int
  );''')
except:
    try:    
        mycursor.execute("SELECT * FROM phonebook")
    except:
        print("Failed to create table")
        exit()

myconn.commit()
myconn.close()

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
    




