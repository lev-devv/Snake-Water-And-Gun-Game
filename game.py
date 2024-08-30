#  A SNAKE , WATER AND GUN GAME USING PYTHON PROGRAMMING :kissing_closed_eyes:
import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1]) # can be anyone from the three values
youStr = input("Enter your choice: ")
youDict = {"s": 1 , "w": -1 , "g": 0}
reverseDict = {1: "snake" , -1: "water" , 0 : "gun"}

you= youDict[youStr]

#By Now, you have two numbers . One from the computer and the other from or by you

print(f"You choose {reverseDict[you]} \nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw!")

else:
    if(computer == 1 and you == -1):
        print("You Lose!")

    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer ==-1 and you == 1):
        print("You Win!")

    elif(computer ==-1 and you == 0):
        print("You Lose!")

    elif(computer == 0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something Went wrong!")