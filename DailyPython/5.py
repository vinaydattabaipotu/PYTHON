#nested loops
#1st model
for x in range (3) :
    for y in range (1, 10):
        print (y , end = " ") 
#seperation
print()
#2nd model
for x in range (3) :
    for y in range (1, 10):
        print(y , end = "")   

#seperation
print()
#3rd model
for x in range (3) :
    for y in range (1, 10):
        print(y , end = "")   
    print()

#nested loop examples 
#printing rectangle 
rows = int(input("Enter no.of rows : "))
columns = int(input("Enter no.of columns :"))
symbol = input("Enter the symbol u want :")
for x in range (rows) :
    for y in range (columns):
        print(symbol ,end = "")
    print()
