#Program to find Factorial of a Number

number = int(input("Enter the number"))
fact = 1
if number == 0 or number == 1:
    print("Factorial is 1")
else:
    for i in range(number,1,-1):   #here we are going backwards from the number to 1 and we are
        fact *=i                   #not including 1 because anynumber multiplied by that number is the original number.

    print("The factorial of ",number," is ",fact)