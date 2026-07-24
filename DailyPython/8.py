#we can make with set & tuple also in the same way
#2 Dimensional
Fruits =     ["appple","orange","banana","water melon"]
vegetables = ["carrot","potato","beetroot"]
Dry_Fruits = ["pista","almonds","cashew"]
groceries = [Fruits,vegetables,Dry_Fruits]
#groceries[row][coloumn]
print(groceries[0])
print(groceries[0][2])
#OR
groceries = [["appple","orange","banana","water melon"],
             ["carrot","potato","beetroot"],
             ["pista","almonds","cashew"]]
for collection in groceries :
    print(groceries)
    break
for collection in groceries :
    for food in collection :
        print(food, end=" ")
    print()

#NUMPAD 
num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))
for row in num_pad :
    for number in row:
        print(number , end=" ")
    print()

#Simple Quiz
Questions = (("What is the rarest element element ?"),
             ("what is the odd number from below?"),
             ("what is the even number from below?"),
             ("what is the prime number from below?"),
             ("what is the gas we inhale ?"))

Options = (("A.Astatine ","B.Gold ","C.Silver ","D.Platinum "),
           ("A.2 ","B.4 ","C.5 ","D.6 "),
           ("A.2 ","B.5 ","C.7 ","D.9 "),
           ("A.2 ","B.4 ","C.6 ","D.8 "),
           ("A.carbon-di-oxide ","B.Oxygen ","C.Nitrogen ","D.Helium "))

Answers = ("A","C","A","A","B")
Guesses = []
Score = 0
Question_num = 0 
for question in Questions :
    print("------------------------")
    print(question)
    for option in Options[Question_num]:
        print(option)
    guess = input("Enter ur guess (A,B,C,D): ").upper()
    Guesses.append(guess)
    if guess == Answers[Question_num] :
        print ("CORRECT!")
        Score += 1
    else :
        print("INCORRECT!")


    Question_num += 1
print(f"ur total score is {Score}")











