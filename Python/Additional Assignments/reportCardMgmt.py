class Student:
    records = {}
    
    def create(self, rno, name, maths, phy, chem, eng, prgm):
        self.rno = rno
        self.name = name        
        self.maths  = maths
        self.phy = phy
        self.chem = chem
        self.eng = eng
        self.prgm = prgm
        Student.records[self.rno] = [self.name, self.maths, self.phy, self.chem, self.eng, self.prgm]

    def delete(self, rno):
        del Student.records[rno]
    
    def modify(self, rno, maths, phy, chem, eng, prgm):
        Student.records[rno] = [Student.records[rno][0], self.maths, self.phy, self.chem, self.eng, self.prgm]

    def displayAll(self):
        for rno in Student.records.keys():
            self.displayOne(rno)
            print("\t------------------------------")

    
    def displayOne(self, rno):
        print(f"\t\tRoll no. : {rno}")
        print(f"\t\tName : {Student.records[rno][0]}")
        print(f"\t\tMaths : {Student.records[rno][1]}")
        print(f"\t\tPhysics : {Student.records[rno][2]}")
        print(f"\t\tChemistry : {Student.records[rno][3]}")
        print(f"\t\tEnglish : {Student.records[rno][4]}")
        print(f"\t\tProgramming : {Student.records[rno][5]}")

student = Student()
while(True):
    print("1. Create a record")
    print("2. Delete a record")
    print("3. Modify marks")
    print("4. Display all records")
    print("5. Display one record")
    print("6. Exit")
    userInput = int(input("Enter your choice : "))
    match userInput:
        case 1:
            rno = int(input("Enter roll no : "))
            name = input("Enter name : ")
            maths = int(input("Enter marks in maths : "))
            phy = int(input("Enter marks in physics : "))
            chem = int(input("Enter marks in chemistry : "))
            eng = int(input("Enter marks in english : "))
            prgm = int(input("Enter marks in programming : "))
            student.create(rno, name, maths, phy, chem, eng, prgm)
        case 2:
            rno = int(input("Enter roll no of record to delete : "))
            student.delete(rno)
        case 3:
            rno = int(input("Enter roll no of student to modify: "))
            maths = int(input("Enter marks in maths : "))
            phy = int(input("Enter marks in physics : "))
            chem = int(input("Enter marks in chemistry : "))
            eng = int(input("Enter marks in english : "))
            prgm = int(input("Enter marks in programming : "))
            student.modify(rno, maths, phy, chem, eng, prgm)
        case 4:
            print("\t\tStudent Records")
            print("\t------------------------------")
            student.displayAll()
        case 5:
            rno = int(input("Enter roll no of student to search: "))
            print("\t------------------------------")
            student.displayOne(rno)
        case 6:
            exit()
        case _:
            print("Invalid choice!")


