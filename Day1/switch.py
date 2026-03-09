print("Select option :")
print("1.Addition of two number\n 2.Multiplication of two number \n 3.Division of two number ")
ch=int(input("\nEnter your choice :"))
match ch:
    case 1:
        num1=int(input("Enter  First Number : "))
        num2=int(input("Enter second number : "))
        num3=num1+num2
        print("The Sum of",num1 ,"and ",num2, "is",num3)
        
    case 2:
        num1=int(input("Enter  First Number : "))
        num2=int(input("Enter second number : "))
        num3=num1*num2
        print("The multiplication of",num1 ,"and ",num2, "is",num3)
       
    case 3:
        num1=int(input("Enter  First Number : "))
        num2=int(input("Enter second number : "))
        num3=num1/num2
        print("The multiplication of",num1 ,"and ",num2, "is",num3)
       
    case _ :
        print("Invalid input")
        
        
        