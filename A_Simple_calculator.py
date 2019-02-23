#A _Simple_Calculator_which works with integer values

y='Y'
while(y == 'Y' or y == 'y'):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    ch = input("""Enter the operation you want to perform
                   + for Addition
                   - for Subtraction
                   * for Multiplication
                   / for Division
                   % for Modulus(to find reminder):- """)

    if ch is '+':
        print("The sum of the given numbers is: ", num1 + num2)
    elif ch is '-':
        print("The difference between the given numbers is: ", num1 - num2)
    elif ch is '*':
        print("The product of the given numbers is: ", num1 * num2)
    elif ch is '/':
        print("The quotient(Division) of the numbers is: ", num1 / num2)
    elif ch is '%':
        print("The modulo(reminder) after the operation is: ", num1 % num2)
    else:
        print("Please enter the correct operation")


    print("Do you want to continue Y(Yes)/N(No)?")
    y=input()