#Mini Railway Reservation System

# three trains running: first one from Trivandrum to Alleppy designated as TVM_ALP,
# second one from Trivandrum to Ernakulam designated as TVM_ERN, and 
# third one from Trivandrum to Kozhikode designated as TVM_KZK
# 5 berths in each train
# TVM_ALP has only one stop at destination Alleppy.
# TVM_ERN has two stops: at Alleppy and Ernakulam.
# TVM_KZK has three stops: at Alleppy, Ernakulam, and Kozhokode.
# to travel to Kozhikode, then TVM_KZK is the only option.
# to Ernakulam, then there are two options:TVM_ERN and TVM_KZK. 
# But priority must be given to TVM_ERN. If it is full then TVM_KZK can be tried.
# to travel to Alleppy, then there are three options: TVM_ALP, TVM_ERN, and TVM_KZK.
# If the first train is full, then the second train may be tried. If that is also 
# full, then the third train may be tried.
# If a passenger is unable to get a ticket, then he may be wait listed in
# the train travelling to his destination provided he wants it. Only two
# wait listed tickets are allowed per train.


from calendar import c
import pyodbc

#create a connection string
myConString = 'Driver={SQL Server};Server=DESKTOP-517KMB6\SQLEXPRESS;Database=railways_db;Trusted_Connection=yes;'

def menu():    
    print("\t\t\t\t\t\t\t\t\t\tRAILWAYS MANAGEMENT SYSTEM")
    print("Menu : ")
    print("1. View your ticket status")
    print("2. List all trains")
    print("3. Show all bookings")
    print("4. Book ticket")
    print("5. Exit")

def display(mycursor, obj):
    if obj == "trains":
        trains = [{"Train No." : row[0], "Train Name" : row[1], "Start Station" : row[2], "End Station" : row[3], "Seats Available" : row[4], "Waiting List Available" : row[5]} for row in mycursor.fetchall()]
        for train in trains:
                    print("--------------------------------------------------")
                    print(f"\tTrain No : {train['Train No.']}")
                    print(f"\tTrain Name : {train['Train Name']}")
                    print(f"\tStart Station : {train['Start Station']}")
                    print(f"\tEnd Station : {train['End Station']}")
                    print(f"\tSeats Available : {train['Seats Available']}")
                    print(f"\tWaiting List Available : {train['Waiting List Available']}")
        print("--------------------------------------------------")
    elif obj == "passengers":
        passengers = [{"Name" : row[1], "Age" : row[2], "Gender" : row[3], "Start Station" : row[4], "End Station" : row[5], "Seats" : row[6], "Train No." : row[7], "Ticket Status" : row[8]} for row in mycursor.fetchall()]
        for passenger in passengers:
                    print("--------------------------------------------------")
                    print(f"\tName : {passenger['Name']}")
                    print(f"\tAge : {passenger['Age']}")
                    print(f"\tGender: {passenger['Gender']}")
                    print(f"\tStart Station : {passenger['Start Station']}")
                    print(f"\tEnd Station : {passenger['End Station']}")
                    print(f"\tSeats : {passenger['Seats']}")
                    print(f"\tTrain No. : {passenger['Train No.']}")
                    print(f"\tTicket Status : {passenger['Ticket Status']}")
        print("--------------------------------------------------")

def listDestinations():
    #create a connection with the connection string
    myconn = pyodbc.connect(myConString)
    #get the cursor object
    mycursor = myconn.cursor()
    query = f"""SELECT * FROM destinations"""
    mycursor.execute(query)
    no = 1
    print("Destinations : ")
    for row in mycursor.fetchall():
        print(f"\t{no}. {row[0]}")
        no += 1
    myconn.commit()
    myconn.close()

class Booking:
    def __init__(self, name, age, gender, start = "TVM"):
        self.name = name
        self.age= age
        self.gender = gender
        self.start = start
    
    def bookTicket(self, end, seats):
        try:
            #create a connection with the connection string
            myconn = pyodbc.connect(myConString)
            #get the cursor object
            mycursor = myconn.cursor()
            query = f"""SELECT trains.train_no 
                        FROM trains 
                        JOIN stops ON trains.train_no = stops.train_no
                        JOIN stations ON stops.station_id = stations.station_id
                        WHERE stations.station_name = '{end}'"""
            mycursor.execute(query)
            trains = [row[0] for row in mycursor.fetchall()]
            for train in trains:
                try: 
                    query = f"""SELECT available_seats, waiting_list FROM trains WHERE train_no = {train}"""
                    mycursor.execute(query)
                    curr = mycursor.fetchall()
                    available = [row[0] for row in curr]
                    waiting = [row[1] for row in curr]
                    if available[0] >= seats:
                        query = f"""UPDATE trains SET available_seats = {available[0] - seats} WHERE train_no = {train}"""
                        mycursor.execute(query)
                        print(f"Booking confirmed in Train - {train}")
                        query = f"""INSERT INTO passengers VALUES (?,?,?,?,?,?,?,?)"""
                        mycursor.execute(query,(self.name, self.age, self.gender, self.start, end, seats, train, "Booked"))                             
                        query = f"""SELECT id 
                                    FROM passengers 
                                    WHERE name = '{self.name}' AND train_no = {train} """
                        mycursor.execute(query)
                        for row in mycursor.fetchall():
                            print(f"Ticket Id : {row[0]}")
                        break
                    elif waiting[0] >= seats:
                        query = f"""UPDATE trains SET waiting_list = {waiting[0] - seats} WHERE train_no = {train}"""
                        mycursor.execute(query)
                        print(f"You are in the waiting list in Train - {train}")
                        query = f"""INSERT INTO passengers VALUES (?,?,?,?,?,?,?,?)"""
                        mycursor.execute(query,(self.name, self.age, self.gender, self.start, end, seats, train, "Waiting List"))

                        break
                    else:
                        print(f"No seats in Train - {train}")
                        break
                except Exception as e:
                    print(e)
                
        except Exception as e:
            print(type(e).__name__)
            print(e)
        myconn.commit()
        myconn.close()

while(True):
    menu()
    ch = int(input("\nEnter option : "))
    match ch:
        case 1:
            id = int(input("Enter ticket id : "))
            #create a connection with the connection string
            myconn = pyodbc.connect(myConString)
            #get the cursor object
            mycursor = myconn.cursor()
            query = f"""SELECT * 
                        FROM passengers
                        WHERE id = '{id}'"""
            mycursor.execute(query)
            display(mycursor, "passengers")
            myconn.commit()
            myconn.close()
        case 2:
            #create a connection with the connection string
            myconn = pyodbc.connect(myConString)
            #get the cursor object
            mycursor = myconn.cursor()
            query = f"""SELECT * 
                        FROM trains"""
            trains = mycursor.execute(query)
            display(mycursor, "trains")
            myconn.commit()
            myconn.close()
        case 3:
            #create a connection with the connection string
            myconn = pyodbc.connect(myConString)
            #get the cursor object
            mycursor = myconn.cursor()
            query = f"""SELECT * 
                        FROM passengers"""
            passengers = mycursor.execute(query)
            display(mycursor, "passengers")
            myconn.commit()
            myconn.close()
        case 4:
            name = input("Enter name : ")
            age = int(input("Enter age : "))
            gender = input("Enter gender : ")
            listDestinations()
            end = input("Enter destination : ")
            seats = int(input("Enter number of seats : "))
            booking = Booking(name= name, age= age, gender= gender)
            booking.bookTicket(end= end, seats= seats)
        case 5:
            exit()
        case _:
            print("Invalid Input!")

    
