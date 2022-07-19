#Get the month number from the user
dobMonth = int(input("Enter the dob month number : "))

#Using if-elif-else
print("\nUsing if-elif-else\n")
if(dobMonth == 1):
    print("People born in January are bold and alert")
    print("Stone: Garnet")
elif(dobMonth == 2):
    print("People born in February are lucky and loyal")
    print("Stone: Amethyst")
elif(dobMonth == 3):
    print("People born in March are naughty and genuine")
    print("Stone: Aquamarine")
elif(dobMonth == 4):
    print("People born in April are caring and strong")
    print("Stone: Diamond")
elif(dobMonth == 5):
    print("People born in May are loving and practical")
    print("Stone: Emerald")
elif(dobMonth == 6):
    print("People born in June are romantic and curious")
    print("Stone: Alexandrite")
elif(dobMonth == 7):
    print("People born in July are adventurous and honest")
    print("Stone: Ruby")
elif(dobMonth == 8):
    print("People born in August are ative and hardworking")
    print("Stone: Peridot")
elif(dobMonth == 9):
    print("People born in September are sensitive and pretty")
    print("Stone: Sapphire")
elif(dobMonth == 10):
    print("People born in October are stylish and friendly")
    print("Stone: Tourmaline")
elif(dobMonth == 11):
    print("People born in November are nice and creative")
    print("Stone: Citrine")
elif(dobMonth == 12):
    print("People born in December are confident and freedom loving")
    print("Stone: Zircon")
else:
    print("Invalid month!")

#Using match-case
print("\nUsing match-case\n")

match dobMonth:
    case 1:
        print("People born in January are bold and alert")
        print("Stone: Garnet")
    case 2:
        print("People born in February are lucky and loyal")
        print("Stone: Amethyst")
    case 3:
        print("People born in March are naughty and genuine")
        print("Stone: Aquamarine")
    case 4:
        print("People born in April are caring and strong")
        print("Stone: Diamond")
    case 5:
        print("People born in May are loving and practical")
        print("Stone: Emerald")
    case 6:
        print("People born in June are romantic and curious")
        print("Stone: Alexandrite")
    case 7:
        print("People born in July are adventurous and honest")
        print("Stone: Ruby")
    case 8:
        print("People born in August are ative and hardworking")
        print("Stone: Peridot")
    case 9:
        print("People born in September are sensitive and pretty")
        print("Stone: Sapphire")
    case 10:
        print("People born in October are stylish and friendly")
        print("Stone: Tourmaline")
    case 11:
        print("People born in November are nice and creative")
        print("Stone: Citrine")
    case 12:
        print("People born in December are confident and freedom loving")
        print("Stone: Zircon")
    case _:
        print("Invalid month!")