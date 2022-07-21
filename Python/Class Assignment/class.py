#Defining the class
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        print(f"Add result : {self.num1 + self.num2}")
    
    def multiply(self):
        print(f"Multiply result : {self.num1 * self.num2}")
    
    def divide(self):
        print(f"Divide result : {self.num1 / self.num2}")

#creating the object
calc = Calculator(10,5)
#calling the methods
calc.add()
calc.multiply()
calc.divide()