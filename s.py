#calculator
#addition
#subtraction
#multiplication
#division
print("select one operation")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLICATION")
print("4.DIVISION")
operation = input()
#choosing
if operation == "1":
     n1=(input("enter a value:"))
     n2=(input("enter b value:"))
     print("the addition is : "+str(int(n1)+int(n2)))
elif operation == "2":
    n1=(input("enter a number"))
    n2=(input("enter b value:"))
    print("the subtraction is : "+str(int(n1)-int(n2)))
elif operation == "3":
    n1=int(input("enter a number"))
    n2=int(input("enter b value:"))
    print("the multiplication is : "+str(int(n1)*int(n2)))
elif operation == "4":
    n1=int(input("enter a number"))
    n2=int(input("enter b value:"))
    print("the division is : "+str(int(n1)/int(n2)))
else:
    print("invalid enter")    
    
          