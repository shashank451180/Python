print("calculator\n")
a=float(input("enter 1st number = "))
b=float(input("enter 2nd number = "))

print("\nselect operation you want to perform \n\nfor addition press + \nfor subtraction press -\nfor multiplication press *\nfor division press /\n")

choice=input("Enter Choice ")

if choice=="+":
    print("Addition : ", a, "+", b, "=", a+b)
elif choice=="-" :
    print("Subtraction : ", a, "-", b, "=", a-b)
elif choice=="*" :
    print("Multiplication is : ", a, "*", b, "=", a*b)
elif choice=="/" :
    print("Division is : ", a, "/", b, "=", a/b)
else:
    print("wrong Choice")
