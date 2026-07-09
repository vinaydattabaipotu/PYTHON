#Day1 of python 
#Basic print statements and Variables
print ("My name is Vinay")
print ("Today date is july 6 2026")
first_name = "Vinay"
Fruit = "Water Melon 🍉"
print(f"my name is {first_name}")
print(f"{Fruit} tastes superrrr🥰")
Age = 19
print(f"i am {Age} years old today")
sgpa = 8.03
print(f"my sgpa in 1st year is : {sgpa}")
is_student = True
if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

    #Typecasting 
sgpa = int(sgpa)
print(type(sgpa))
    #INPUT
Ironman = input("who is Ironman ?")
print(f"Ironman is {Ironman}")

#Exercise 1 
#Area Calculation of rectangle
length = input("Enter the length of Rectangle :")
breadth = input("enter the breadth of Reatangle :")
length = int(length)
breadth = int(breadth)
Area = length*breadth
print (f"Area of Reactangle is : {Area}cm²")
#Exercise 2
#Shopping Cart
Item = input ("what item do u like to buy :")
price = float(input("What is the price of ur item :"))
Quantity = int(input("How many pieces do u want to buy :"))
Total = price * Quantity
print (f"ur bill is {Total}")



animals = 10 
#animals = animals + 1
#animlas += 1
#animals = animals - 1
#animals -= 1
#animals = animals * 1
#animals *= 1
#animals = animals / 1
#animals /= 1
#animals = animals ** 2
#animals **= 2
#animals = animals % 3


X = 3.14
Y = -4
Z = 5

result1 = round(X)
print(result1)
result2 = abs(Y)
print(result2)
result3 = pow(4,3)
print(result3)
result4 = max(X,Y,Z)
print(result4)
result5 = min(X,Y,Z)
print(result5)

import math

V = 16
W = 9.1
print(math.pi)
print(math.e)
result6 = math.sqrt(V)
print(result6)
print(math.ceil(W))
print(math.floor(W))


#if,elif,else
age = int(input("enter ur age : "))
if age >= 18:
    print("sigguledhu ra neeku")
elif age < 0 :
    print("puttu ra mundhu")
else :
    print ("bagupadu ra ayya ")


response = input("would you like to eat something (Y/N) : ")
if response.lower() == "y" :
    print("veldham padha ayithe")
elif response.lower() == "n" :
    print ("Endhuku ra nuvvu puttavu")
else :
    print ("thinnaga chusi Y gani N gani response ivvu ra ")
