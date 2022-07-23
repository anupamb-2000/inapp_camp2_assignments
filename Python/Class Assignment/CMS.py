#Write a program to build a simple Clinic Management System using Python
#which can perform following operations inside class CMS

#Admit : takes patient details frommthe user like name, gender, age, dob
#blood group. A patient_id should be automatically generated

#listPatients : displays the details of every patient

#search : search using patient_id

#Delete : delete using patient_id

#Update : will ask for patient_id and other details. It will replace the other details with new details.

#Create inherited classes "OP" and "NonOP". "OP" should have the additional Admit function and NonOP a function to generate an OP Ticket
#with incrementing no. for every patient.

import random


class CMS:
    patientID = 0
    patients = {}
    admittedPatients = {}

    def __init__(self):
        CMS.patientID += 1
        self.ID = CMS.patientID

    def register(self, name, gender, age, dob, bloodGroup):
        CMS.patients.update({self.ID : [name, gender, age, dob, bloodGroup]})

    def listPatients(self):
        for patient in CMS.patients:
            print(f"ID : {patient}")
            print(f"Name : {CMS.patients[patient][0]}")
            print(f"Gender : {CMS.patients[patient][1]}")
            print(f"Age : {CMS.patients[patient][2]}")
            print(f"DOB : {CMS.patients[patient][3]}")
            print(f"Blood Group : {CMS.patients[patient][4]}")

    def search(self):
        searchID = int(input("Enter ID to search : "))
        if(searchID in CMS.patients.keys()):
            print(f"ID : {searchID}")
            print(f"Name : {CMS.patients[searchID][0]}")
            print(f"Gender : {CMS.patients[searchID][1]}")
            print(f"Age : {CMS.patients[searchID][2]}")
            print(f"DOB : {CMS.patients[searchID][3]}")
            print(f"Blood Group : {CMS.patients[searchID][4]}")
        else:
            print("No record found!")

    def delete(self):
        deleteID = int(input("Enter ID to delete : "))
        if(deleteID in CMS.patients.keys()):
            del CMS.patients[deleteID]
            print("Record deleted!")
        else:
            print("No record found!")

    def update(self,updateID, name, gender, age, dob, bloodGroup):
        if(updateID in CMS.patients.keys()):
            CMS.patients[updateID] = [name,gender,age,dob,bloodGroup]
            print("Record updated successfully!")
        else:
            print("No record found!")
        


class OP(CMS):
    def admit(self, id, department, days):
        self.ID = id
        self.department = department
        self.days = days
        super().admittedPatients[self.ID] = super().patients[self.ID]
        super().admittedPatients[self.ID].extend([self.department, self.days])
        print(super().admittedPatients)


class NonOP(CMS):
    def generateOP(self):
        self.OPToken = random.randint(1000, 9999)
        print(f"OP Token : {self.OPToken}")

patient1 = OP()
patient2 = CMS()
patient3 = NonOP()
patient1.register("Tom", "Male", 15, "03-07-2007", "A+")
patient2.register("Jane", "Female", 18, "04-07-2004", "A+")
patient1.admit(patient1.ID, "Dermatology", 5)
patient1.listPatients()
patient2.search()
patient2.delete()
patient1.update(1, "Tom", "Male", 16, "03-07-2007", "A+ve")
patient3.generateOP()