'''
Author: @ironsubhajit
Project Name: Converter_Weight_height_Currency

'''

print("\nHello,and Wellcome Sir.\nIt's a Converter for converting weight, height & currency\n")
ch=int(input("\n1.Start Converting.\n2.Quit\n"))
if ch==1 :
    while ch==1:
        choice=int(input("\nWhat you want to convert.\nPress 1 for Weight(lbs to kg)\nPress 2 for Height(cm to feet)\nPress 3 for Currency\n"))
        if choice==1 :
            weight=float(input("\nEnter Your Weight: "))
            unit=input("(L)bs or (K)g: ")
            if unit.upper()=="L":
                convert=weight*0.45
                print(f"\nYour Weight is {convert} kgs.")
                ch=int(input("\n1.Start\n2.Quit\n"))
            else:
                convert=weight/0.45
                print(f"\nYour Weight is {convert} lbs.")
                ch=int(input("\n1.Start\n2.Quit\n"))
        elif choice==2 :
            height=float(input("Enter Your Height: "))
            unit=input("(cm) or (Feet): ")
            if unit.upper()=="CM":
                convert=height/30.48
                print(f"\nYour Height is {covert} feet.")
                ch=int(input("\n1.Start\n2.Quit\n"))
            else:
                convert=height*30.48
                print(f"\nYour Height is {convert} cm.")
                ch=int(input("\n1.Start\n2.Quit\n"))
        elif choice==3:
            currency
elif ch==2:
    exit(0)
