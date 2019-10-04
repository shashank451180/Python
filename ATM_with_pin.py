
print('welcome to ATM')

balance=50000       #default balance

chance=1

def bal():
    print('Transaction Successful \nyour balance is',balance)


while chance<=3:    #only three times user can enter incorrect password
    
    pin=int(input('please enter your pin'))  #input pin

        
    if pin==1234:   #if pin is correct then only following code will execute
        print('correct pin')
        #options for user
        choose=int(input('press 1 to check the balance\npress 2 to withdraw cash\npress 3 to deposite\npress 4 to quit\n'))

        while choose==1:    #if user press 1 then following code will execute and will show remaining balance amount
            a="yes" 
            while a=="yes" or a=="Yes":
                bal()
                a=input("\ndo you want to continue transaction??\ntype yes to continue\ntype no to main menu\n")
            choose=int(input('press 1 to check the balance\npress 2 to withdraw cash\npress 3 to deposite\n'))

        while choose==2:    #if user press 2 then following code will execute
            a="yes"
            while a=="yes" or a=="Yes":
                withdraw=float(input('enter the amount you want to withdraw:'))
                balance-=withdraw
                bal()
                a=input("\ndo you want to continue transaction??\ntype yes to continue\ntype no to main menu\n")
            choose=int(input('press 1 to check the balance\npress 2 to withdraw cash\npress 3 to deposite\npress 4 to quit\n'))

        while choose==3:    #if user press 3 then following code will execute
            a="yes"
            while a=="yes" or a=="Yes":
                deposite=float(input('enter the amount to deposite:'))
                balance+=deposite
                bal()
                a=input("\ndo you want to continue transaction??\ntype yes to continue\ntype no to main menu\n")
            choose=int(input('press 1 to check the balance\npress 2 to withdraw cash\npress 3 to deposite\npress 4 to quit\n'))

        if choose==4:    #if user press 4 then following code will execute
            print("Thank you")
        else:
            print("wrong input")

    else:
        print('worng pin')
        chance+=1
        if chance==0:
            print('you are out of tries')
