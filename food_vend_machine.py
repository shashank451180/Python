#vending machine

print('***Welcome to food courte***')

drinks=['cola','pepsi','water','juice']
chips=['lays','balaji','daimond']
chocolate=['kitkat','5*','silk','munch']

cont="yes"
while cont=="yes":
    food=int(input('\n1.drinks\n2.chips\n3.chocolates\n'))

#if food==1:
   # a=0
    #for i in drinks:
    #    print(a+1,i)
     #   a+=1

    if food==1:
        choice=int(input("plese select your drink\n1.cola=Rs.10\n2.pepsi=Rs.12\n3.water=Rs.5\n4.cola=Rs.15\n"))

        if choice==1:
            pay=int(input('please pay Rs.10 for cola:'))
            if pay==10:
                print('collect your cola')
            else:
                print('please pay Rs.10')

        elif choice==2:
            pay=int(input('please pay Rs.12 for pepsi:'))
            if pay==12:
                print('collect your pepsi')
            else:
                print('please pay Rs.12')
            
        elif choice==3:
            pay=int(input('please pay Rs.5 for water:'))
            if pay==5:
                print('collect your water')
            else:
                print('please pay Rs.5')
            
        elif choice==4:
            pay=int(input('please pay Rs.15 for juice:'))
            if pay==15:
                print('collect your juice')
            else:
                print('please pay Rs.15')

    elif food==2:
        choice=int(input("plese select your chips\n1.lays=Rs.10\n2.balaji=Rs.10\n3.daimond=Rs.10\n"))

        if choice==1:
            pay=int(input('please pay Rs.10 for lays:'))
            if pay==10:
                print('collect your lays')
            else:
                print('please pay Rs.10')

        elif choice==2:
            pay=int(input('please pay Rs.10 for balaji:'))
            if pay==10:
                print('collect your balaji')
            else:
                print('please pay Rs.10')
            
        elif choice==3:
            pay=int(input('please pay Rs.10 for daimond:'))
            if pay==10:
                print('collect your daimond')
            else:
                print('please pay Rs.10')

    elif food==3:
        choice=int(input("plese select your chocolate\n1.kitkat=Rs.10\n2.5*=Rs.20\n3.silk=Rs.50\n4.munch=Rs.5\n"))

        if choice==1:
            pay=int(input('please pay Rs.10 for kitkat:'))
            if pay==10:
                print('collect your kitkat')
            else:
                print('please pay Rs.10')

        elif choice==2:
            pay=int(input('please pay Rs.20 for 5*:'))
            if pay==20:
                print('collect your 5*')
            else:
                print('please pay Rs.20')
            
        elif choice==3:
            pay=int(input('please pay Rs.50 for silk:'))
            if pay==50:
                print('collect your silk')
            else:
                print('please pay Rs.50')
                
        elif choice==4:
            pay=int(input('please pay Rs.5 for munch:'))
            if pay==5:
                print('collect your munch')
            else:
                print('please pay Rs.10')


    cont=input('do you want to continue??\nyes/no')



