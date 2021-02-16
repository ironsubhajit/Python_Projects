
# This function adds two number
def addition(fst_num, snd_num):
    resu = fst_num + snd_num
    return resu


# This function subtracts two number
def subtraction(fst_num, snd_num):
    resu = fst_num - snd_num
    return resu


# This function multiply two number
def multiplication(fst_num, snd_num):
    resu = fst_num * snd_num
    return resu


# This function divides two number
def division(fst_num, snd_num):
    resu = fst_num / snd_num
    return resu


# checks for operator and invokes function accordingly
def operator_check(op, first_num, second_num):
    if op == '+':
        res = addition(first_num, second_num)
        return res
    elif op == '-':
        res = subtraction(first_num, second_num)
        return res
    elif op == '*':
        res = multiplication(first_num, second_num)
        return res
    elif op == '/':
        res = division(first_num, second_num)
        return res
    else:
        print("Invalid Input!!!")
        return 0


def user_menu():
    menu = """
    #########################################
    #       Code by @ironsubhajit           #
    #########################################
    -------------Calculator app--------------
    """
    print(menu)
    try:
        # asking user to number input
        number_1 = int(input("\tEnter 1st number: "))
        number_2 = int(input("\tEnter 2nd number: "))

        operator_menu = """
                    Please type in the math operation you would like to complete:

                    + for addition
                    - for subtraction
                    * for multiplication
                    / for division
                """
        # asking user for operator input
        user_input_op = input(f"{operator_menu}\n>> ")

        # get result
        result = operator_check(user_input_op, number_1, number_2)

        if result:
            print(f"Result is : {result}")
    except (ValueError, UnboundLocalError):
        print("Invalid input!!!\nExpect Integer\nPlease Try Again!!!")
    except ZeroDivisionError:
        print("Division By Zero is not allowed!!!")


if __name__ == '__main__':
    user_menu()

    thank_you_msg = """
                Thanks For Visiting :D
            """

    choice = input("Do you want to continue?(Y/N): ")
    if choice.upper() != 'Y' and choice.upper() != 'N':
        print("Invalid Input!!!")
    elif choice.upper() == 'N':
        print(thank_you_msg)
        exit(0)

    while choice.upper() == 'Y' or True:
        user_menu()
        choice = input("Do you want to continue?(Y/N): ")
        if choice.upper() != 'Y' and choice.upper() != 'N':
            print("Invalid Input!!!")
            continue
        if choice.upper() == 'N':
            print(thank_you_msg)
            exit(0)