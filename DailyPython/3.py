name = input ("Enter ur name : ")
if name == "":
    print("You did'n entered ur name 😾")
else :
    print(f"hello {name} 😊 ")

name1 = input ("Enter ur name : ")
while name1 == "" :
    print("Enter ur name 😾")
    name1 = input("Enter ur name ☮︎ : ")
print(f"hello {name1} 😛")

age = int(input("Enter ur age :"))

while age < 0 :
    print ("Age can't be negative ");
    age = int(input("Enter ur age :"))
print (f"u are {age} years old ")

food = input("enter the food u like (q to Quit):")
while not food == "q" :
    print(f"ohhhh u like {food} 😋😋")
    food = input("enter the another food u like (q to Quit): ")
print ("Thanxxxxx byeeee 🙈")

num = int(input("Enter a number between 1 - 10 :"))
while num < 1 or num > 10 :
    print ("please enter a valid number ")
    num = int(input("Enter a number between 1 - 10 :"))
 
