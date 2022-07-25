from abc import ABC, abstractmethod
#Defining the class
class Calculator(ABC):

    @abstractmethod
    def calculator(self):
        pass

    @property
    def operandA(self): 
        return self.__num1

    @operandA.setter
    def operandA(self, num):
        if(num.isdigit()):
            self.__num1 = int(num)
        else:
            raise ValueError(f"Invalid operand(A)!")

    @property
    def operandB(self): 
        return self.__num2

    @operandB.setter
    def operandB(self, num):
        if(num.isdigit()):
            self.__num2 = int(num)
        else:
            raise ValueError(f"Invalid operand(B)!")

class CalcSum(Calculator):
    def calculator(self):
        print(f"Addition result : {self.operandA + self.operandB}")

class CalcDiff(Calculator):
    def calculator(self):
        print(f"Subtraction result : {self.operandA - self.operandB}")

class CalcProd(Calculator):
    def calculator(self):
        print(f"Multiplication result : {self.operandA * self.operandB}")

class CalcQuo(Calculator):
    def calculator(self):
        print(f"Division result : {self.operandA + self.operandB}")

#creating the object
add = CalcSum()
sub = CalcDiff()
mul = CalcProd()
div = CalcQuo()
#calling the methods
for operation in [add, sub, mul, div]:
    operation.operandA = "10"
    operation.operandB = "5"
    operation.calculator()