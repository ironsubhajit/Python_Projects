'''
to_do:
    1->define function :decimal_to_hexa(),decimal_to_octa() & vise-versa
    2->check all errors and list them
    3->change the upper() method to something else
    4->examine time & space complexity
advanced:
    1->use Tkinter for GUI
    2->use CSS
done:
    1->check box,decimal_to_binary()
'''
import sys

def main_menu():
    while(1):
        print("\npress 1: decimal to binary\npress 2: decimal to hexadecimal\npress 3: decimal to octadecimal\npress 0: Quit".upper())
        button = int(input("\nenter your choice: ".upper()))
        if button == 1:
            print(decimal_to_binary())
            check()
        elif button == 2:
            print(decimal_to_hexa())
            check()
        elif button == 3:
            print(decimal_to_octa())
            check()
        elif button == 0:
            print("\n!exit sucessfully!".upper())
            exit(0)
        else:
            print("\nwrong choice!\ntry again!".upper())
    else:
        print("\n!exi:wq
        t sucessfully!".upper())
        exit(0)


def decimal_to_binary():
    number = int(input("enter the number: ".upper()))
    binary = format(number, 'b')
    return("Decimal to Binary Conversion is: {}".format(binary))

def decimal_to_hexa():
    pass


def decimal_to_octa():
    pass


def check():
    while(1):
        ck = input("\ndo you want to continue?(y/n)\n".upper())
        if ck == 'y':
            return 1
        elif ck == 'n':
            return 2
        else:
            print("\nwrong choice!\ntry again!".upper())


print("\n😁😁!welcome to number conversion app!😁😁".upper())
while(1):
    try:
        main_menu()
    except(ValueError):
        print("\nsomething went wrong!!\nenter input correctly!".upper())
    continue
