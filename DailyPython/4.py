#for loops 
for x in range (1, 11) :
    print (x)

for x in reversed(range(1,11)) :
    print (x)

print("HAPPY NEW YEAR 🥳🥳 !!")
credit_Number = "1234-5678-9012-3456"
for x in credit_Number :
   print (x)
for x in range (1 , 20) :
   if x == 7 :
      continue
   else :
      print (x)
for x in range (1 , 20) :
   if x == 7 :
      break
   else :
      print (x)


for x in range(1 , 10) :
    print(x,end = " ")

import time 

time.sleep(3)
print("⌛️ is  🆙 ")
my_time = int(input("Enter the time in sec :"))
for x in range (0,my_time) :
    print (x)
    time.sleep(1)


my_time = int(input("Enter the time in sec :"))
for x in reversed(range (0,my_time)) :
    print (x)
    time.sleep(1)

print("TIME IS UP!!")

my_time = int(input("Enter the time in sec :"))
for x in range (my_time ,0 , -1) :
    print (x)
    time.sleep(1)

print("TIME IS UP!!")

my_time = int(input("Enter the time in sec :"))
for x in range (my_time ,0 , -1) :
    seconds = x % 60
    minutes = int(x / 60 ) % 60
    hours = int((x / 3600))
    print (f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME IS UP!!")
