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
