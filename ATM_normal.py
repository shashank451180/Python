print('welcome to ATM')

balance=50000

def bal():
    print('Transaction Successful \nyour balance is',balance)
  
choose=int(input('press 1 to check the balance\npress 2 to withdraw cash\npress 3 to deposite\npress 4 to quit\n'))


while choose==1:
    a="yes" 
    while a=="yes" or a=="Yes":
        bal()
        a=input("\ndo you want to continue??\ntype yes to continue\ntype no to exit\n")
    choose=int(input('press 1 to check the balance\npress 2 to withdraw cash\npress 3 to deposite\n'))

while choose==2:
    a="yes"
    while a=="yes" or a=="Yes":
        withdraw=float(input('enter the amount you want to withdraw:'))
        balance-=withdraw
        bal()
        a=input("\ndo you want to continue??\ntype yes to continue\ntype no to exit\n")
    choose=int(input('press 1 to check the balance\npress 2 to withdraw cash\npress 3 to deposite\npress 4 to quit\n'))

while choose==3:
    a="yes"
    while a=="yes" or a=="Yes":
        deposite=float(input('enter the amount to deposite:'))
        balance+=deposite
        bal()
        a=input("\ndo you want to continue??\ntype yes to continue\ntype no to exit\n")
    choose=int(input('press 1 to check the balance\npress 2 to withdraw cash\npress 3 to deposite\npress 4 to quit\n'))

if choose==4:
    print("Thank you")
else:
    print("wrong input")
