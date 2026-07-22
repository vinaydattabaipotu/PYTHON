#collections [list],{set},(tuple)
Fruits = ["apple","banana","water melon","orange"] 
print(Fruits)
print(Fruits[0])
print(Fruits[0:3])
print(Fruits[0:3:2]) 
print(Fruits[::-1])

#loops 
for x in Fruits :
    print(x)
####
print(dir(Fruits))
####
print(help(Fruits))
####    
print(len(Fruits))
####
print("apple" in Fruits)
####
print("vinay" in Fruits)
#[] lists = ordered and changeable . duplicates ok
Fruits[0] = "pine apple"
print(Fruits[0])
Fruits.append("Muskmelon")
print(Fruits)
Fruits.remove("apple")
print(Fruits)
Fruits.insert(3,"Avacado")
print(Fruits)
Fruits.sort()
print(Fruits)
Fruits.reverse()
print(Fruits)
Fruits.clear()
print(Fruits)
print(Fruits.index("apple"))
print(Fruits.count("apple"))

