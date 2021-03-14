print("Welcome to python Bank ATM")
restart=('y')
chances=3
Balance=999.12
while chances>=0:
    pin=int(input('Please enter your 4 Digit Pin '))
    if pin==(1234):

        while restart not in ('n','NO','no','N'):
            print('please press 1 for your balance')
            print('please press 2 to make a transaction')
            print('please press 3 to pay in')
            print('please press 4 to return card\n')
            option=int(input('What would you like to choose?:'))
            if option==1:
                print('Your Balance is $',Balance)
                restart=input('Would you like to go back?')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option==2:
                option2=('y')
                withdrawl=float(input('How much would you like to withdraw? 10, 20, 30, 40, 50, 60, 70,80,90,100 for other enter 1:'))
                if withdrawl in [10,20,30,40,50,60,70,80,90,100]:
                    Balance=Balance-withdrawl
                    print('\nyour balance is now $',Balance)
                    restart = input('Would you like to go back?')
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('Thank You')
                        break

                elif withdrawl!=[10,20,30,40,50,60,70,80,90,100]:
                    print('Invalid Amount,please Re-try\n')
                    restart=('y')
                elif withdrawl==1:
                    withdrawl=float(input('Please enter desired amount:'))

            elif option==3:
                pay_in=float(input('How much would you like to pay in?:'))
                Balance=Balance+pay_in
                print('\nyour balance is now $',Balance)
                restart = input('Would you like to go back?')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                    break

            elif option==4:
                print('Please wait while your card is returned......\n')
                print('Thank you for you service')
                break

            else:
                print('please enter a correct number,..\n')
                restart=('y')

    elif pin !=('1234'):
        print('Incorrect password')
        chances=chances-1
        if chances==0:
            print('\n Sorry No more tries')
            print('Thank you')
            break