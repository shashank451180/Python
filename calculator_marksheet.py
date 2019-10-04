option=int(input('choose your option \npress 1 for calculator \npress 2 for student marksheet\n'))

if option==1:
    print("calculator\n")
    d="yes"
    while d=="yes" or d=="Yes":

        
        
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

        d=input("\ndo you want to continue??\ntype Yes if you want to continue\ntype No to exit\n")
        
    if d=="no" or d=="No":
        print("Thank you")
    else:
        print("wrong input")    

elif option==2:
    print("Student marksheet")

    choice="Yes"


    while choice=="yes" or choice=="Yes":

        marks=float(input("enter your marks ="))

        if marks>=80 and marks<=100:
            print("Your Grade Is O")
        elif marks>=65 and marks<=79:
            print("Your Grade Is A")
        elif marks>=50 and marks<=64:
            print("Your Grade Is B")
        elif marks>=40 and marks<=49:
            print("Your Grade Is C")
        elif marks>=30 and marks<=39:
            print("Your Grade Is D")
        elif marks>=0 and marks<=29:
            print("You are FAIL")
        else:
            print("Wrong input")

        choice=input("\ndo you want to continue??\ntype Yes if you want to continue\ntype No to exit\n")

    if choice=="no" or choice=="No":
        print("Thank you")
    else:
        print("wrong input") 

else:
    print("wrong input")
