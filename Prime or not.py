#Program that checks whether the entered number is a prime number or not

number = int(input("Enter the number you want to check:- "))

counter = 0

for i in range(2,number//2):
    if number%i == 0:
        counter+=1

if counter is 0:
    print("The given number is prime number")
else:
    print("The given number is not a prime number")
