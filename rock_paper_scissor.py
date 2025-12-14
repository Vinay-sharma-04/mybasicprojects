'''
rock = 1
paper = -1
Scissors = 0

'''

my_choice = int(input("Enter the number :"))

import random
options = [1,-1,0]

computer_choice = random.choice(options)

my_dict = {
    1:"r",
    -1:"p",
    0:"s"
}

print("i chose ",my_choice)
print("computer chose",computer_choice)

if (computer_choice == my_choice):
    print("its a draw😒!")

else:
    if(computer_choice == 1 and my_choice  == -1):
        print("i win 😁")

    elif(computer_choice == 1 and my_choice == 0):
        print("i lose 😢")

    elif(computer_choice == -1 and my_choice == 1):
        print("i lose 😢")
    
    elif(computer_choice == -1 and my_choice == 0):
        print("i win 😁")

    elif(computer_choice == 0 and my_choice == 1):
        print("i win 😁")

    elif(computer_choice == 0 and my_choice == -1):
         print("i lose 😢")   

