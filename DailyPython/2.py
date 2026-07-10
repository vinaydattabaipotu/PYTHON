#simple calculator
Operator = input("enter an operator (+  -  *  /) :")
num1 = float(input("enter the 1st number : "))
num2 = float(input("enter the 2nd number : "))
if Operator == "+" :
    result = num1 + num2
    print(round(result, 3))
elif Operator == "-" :
    result = num1 - num2
    print(round(result, 3))
elif Operator == "*" :
    result = num1 * num2 
    print(round(result, 3))
elif Operator == "/" :
    result = num1 / num2 
    print(round(result, 3))
else :
    print(f"{Operator} is not valid")


#Logical Operators
temp = 20
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")


num = 7
print ("positive" if num > 0 else "negative") 
num3 = 6 
result = "Even" if num3 % 2 == 0 else "Odd"
print(result)

num4 = 5
num5 = 6
max_num = num4 if num4 > num5 else num5
min_num = num4 if num4 < num5 else num5
print (max_num)
print (min_num)
name = input("Enter ur name :")
result = len(name)
print (result)
result1 = name.find(" ")
result2 = name.rfind(" ")
print(result1)
print(result2)
result3 = name.capitalize()
print(result3)
result4 = name.upper()
print(result4)
result5 = name.lower()
print(result5)
result6 = name.isdigit()
print(result6)
result7 = name.isalpha()
print(result7)
phone_number = input("Enter ur phn number :")
result8 = phone_number.count("9") 
print(result8)
result9 = phone_number.replace("9","8")
print(result9)
# print(help(str))
#indexing [start : end : step]
Credit_Number = "1234-5678-9012-3456"
print(Credit_Number[0])
print(Credit_Number[:4])
print(Credit_Number[5:9])
print(Credit_Number[5:])
print(Credit_Number[-1])
print(Credit_Number[ : :3])
revCreditNumber = Credit_Number[::-1]
print(revCreditNumber)
price1 = 3.14159
price2 = -987.874
price3 = 12.34
price4 = 32654.56567
print(f"Price 1 is {price1:.2f}") 
print(f"Price 2 is {price2:.2f}")
print(f"Price 3 is {price3:.2f}")
print(f"price 1 is {price1:10}")
print(f"price 2 is {price2:10}")
print(f"price 3 is {price3:10}")
print(f"price 1 is {price1:010}")
print(f"price 2 is {price2:010}")
print(f"price 3 is {price3:010}")
print(f"price 1 is {price1:<10}")
print(f"price 2 is {price2:<10}")
print(f"price 3 is {price3:<10}")
print(f"price 1 is {price1:>10}")
print(f"price 2 is {price2:>10}")
print(f"price 3 is {price3:>10}")
print(f"price 1 is {price1:^10}") 
print(f"price 2 is {price2:^10}")
print(f"price 3 is {price3:^10}")
print(f"price 1 is {price1:+10}")
print(f"price 2 is {price2:+10}")
print(f"price 3 is {price3:+10}")
print(f"price 1 is {price1: 10}")
print(f"price 2 is {price2: 10}")
print(f"price 3 is {price3: 10}")
print(f"price 4 is {price4:,}")
print(f"price 4 is {price4:,.2f}")
print(f"price 4 is {price4:+,.2f}")
