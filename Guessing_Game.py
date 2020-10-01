'''
Author: @ironsubhajit
Project Name: Simple_Number_guessing_Game

'''
import random as rand


def game_level(level=4):
    print(f"You are Now in level: {level}")
    if level == 4:
        val=int(input("\nHow many time you want to Guess(max is 2 times): "))
    elif level == 3:
        val = int(input("\nHow many time you want to Guess(max is 3 times): "))
    elif level == 2:
        val = int(input("\nHow many time you want to Guess(max is 4 times): "))
    elif level == 1:
        val = int(input("\nHow many time you want to Guess(max is 5 times): "))

    return val


def start_game(val, guess):
    if val <= 4:
        print("\nOK all set,Lets start :D\n")
        i = 1
        while i <= val:
            g = int(input("guess plz: "))
            if g==guess:
                print("\ncongrates! you win! :D\n")
                print("\nSir,You have really a good guessing skill.\n")
                l = end_game()
                if l == 1:
                    break
                elif l == 0:
                    exit(1)
            else:
                t=val-i
                if t>=1:
                    print(f"\nOnly {t} Chance are left.\n")
                else:
                    print("\nGame over\n")
                i+=1
        else:
            print("sorry,you are failed!\n")
            print(f"The answer is {guess}\n\nBetter luck next time.\n")
            l = end_game()
    else :
        print("\nYou can't guess more than 4 times\n")
        l = end_game()
    return l


def end_game():
    l = int(input("press 1. New 1Game 0. exit\n"))
    if l == 1:
        return 1
    else:
        return 0


l = end_game()
while l == 1:
    print("\nHello Sir,Welcome to guessing a Number."
          "\n\nLets see how strong your guessing skills are :D"
          "\nRules are so simple:"
          "\nyou have max of 4 chances to guess a no. which is between 0 to 9\n")
    guess = rand.randint(0,9)
    level = int(input("Enter Game Level(max is 4): "))
    val = game_level(level)
    l = start_game(val, guess)
if l == 0:
    print("Thank You!")
    exit(0)
