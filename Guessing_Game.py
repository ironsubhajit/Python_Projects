'''
Author: @ironsubhajit
Project Name: Simple_Number_guessing_Game

'''
import random as rand
l=int(input("\n1.New Game\n0.Quit\n"))
while l==1:
    print("\nHello Sir,Wellcome to guessing a Number.\n\nLets see how strong your gussing skills are :D\nRules are so simple:\nyou have max of 4 chances to guess a no. which is between 0 to 9\n")
    guess = rand.randint(0,9)
    val=int(input("\nHow many time you want to Guess(max is 4 times): "))
    if val<=4:
        print("\nOK all set,Lets start :D\n")
        i=1
        while i<=val:
            g=int(input("guess plz: "))
            if g==guess:
                print("\ncongrates! you win! :D\n")
                print("\nSir,You have really a good guessing skill.\n")
                l=int(input("\npress 1. New Game 0. exit\n"))
                if l==1:
                    break
                elif l==0:
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
            l=int(input("press 1. New 1Game 0. exit\n"))
    else :
        print("\nYou can't guess more than 4 times\n")
        l=int(input("\npress 1. continue 0. exit\n"))
if l==0:
    exit(1)
