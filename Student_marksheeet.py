print("Student marksheet")

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
