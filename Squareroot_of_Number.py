
y="Y"
while(y=="y" or y=="Y"):
    number = int(input("Enter the number"))
    if number < 0:
        print("Please Enter a postive number")
    else:
        sqrt= number**(1/2)
        print("The squareroot of the numebr is ",sqrt)
        y=input("Do you want to continue Y/N?")

