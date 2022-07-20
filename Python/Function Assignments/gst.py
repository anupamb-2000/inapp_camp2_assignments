#Create a function to calculate the price after imposing GST on an Item.
#The user will be giving the base price of the item and its GST rate as input
#The output should contain the following details:
#The actual price of the item
#Price after CGST
#Price after SGST
#Total price after GST

#Function definition
def calcGST(basePrice, rate):
    CGSTRate = rate / 2
    SGSTRate = rate / 2
    CGSTPrice = basePrice + basePrice*(CGSTRate/100)
    SGSTPrice = basePrice + basePrice*(SGSTRate/100)
    newPrice = basePrice + basePrice*(rate/100)
    return (CGSTPrice, SGSTPrice, newPrice)

basePrice = float(input("Enter the actual price of the item: "))
rate = float(input("Enter the GST rate: "))
#Calling the function
output = calcGST(basePrice, rate)

#Printing the output
print(f"The Actual Price of the Item : {basePrice}")
print(f"Price after CGST : {output[0]}")
print(f"Price after SGST : {output[1]}")
print(f"Total Price after GST : {output[2]}")

