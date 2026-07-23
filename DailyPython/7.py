#SET {} = ordered,immutable,add&remove ok ,no duplicates  
Fruits = {"apple","banana","water melon","musk melon"}
print(Fruits)
print(dir(Fruits))
print(help(Fruits))
print(len(Fruits))
print("banana" in Fruits)
Fruits.add("Avacado")
print(Fruits)
Fruits.remove("apple")
print(Fruits)
Fruits.pop()
print(Fruits)
Fruits.clear()
print(Fruits)

#Tuples{} = ordered , unchangeable ,duplicates ok , FASTER
Fruits = ("apple","banana","water melon","musk melon","musk melon")
print(dir(Fruits))
print(help(Fruits))
print(len(Fruits))
print("banana" in Fruits)
print(Fruits.index("apple"))
print(Fruits.count("musk melon"))
#
for fruit in Fruits:
    print(fruit)


#Shopping cart program
Foods = []
Price = []
total = 0 
while True :
    food = input("enter the fod u like (q to quit) : ")
    if food.lower() == "q" :
        break
    else :
        price = float(input(f"Enter the price of {food} : ₹"))
        Foods.append(food)
        Price.append(price)
        
for food in Foods :
    print(food,end=(" "))
for price in Price :
    total += price
print(total)



