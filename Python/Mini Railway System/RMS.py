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
import pyodbc

#create a connection string
myConString = 'Driver={SQL Server};Server=DESKTOP-517KMB6\SQLEXPRESS;Database=railways_db;Trusted_Connection=yes;'
#create a connection with the connection string
myconn = pyodbc.connect(myConString)


class Booking:
    def __init__(self, name, start, end, seats):
        self.name = name
        self.start = start
        self.end = end
        self.seats = seats
    
    def bookTicket(self, end):
        pass

