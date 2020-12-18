'''
todo:
    1->some editing required
    2->need GUI
'''
phone=(input("Enter your phone number: "))
digits={
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output=""
for ch in phone:
    output+=digits.get(ch,"!it's not a digit!")+" "
print(output)