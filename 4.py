while True:
    pin = int(input("Enter account pin : "))
    if pin == 2345:
        while True:
            print("1- View Balance   2- Withdraw   3- Deposite   4- Exit" )
            selection = int(input("Enter your selection : "))
            if selection == 1:
                print("0")
            elif selection == 2:
                amounttowithdraw = float(input("Enter amount to withdraw : "))
                print("Is this the correct amount, Yes or No ?",amounttowithdraw)
                if input() == 'Yes':
                    print("Verify withdraw")
            elif selection == 3:
                amounttodeposit = float(input("Enter amount to deposit : "))
                print("Is this the correct amount, Yes or No ?",amounttodeposit)
                if input() == 'Yes':
                    print("Update Balance : ",amounttodeposit)
            elif selection == 4:
                print("Transaction is now complete.")
                print("Transaction number: 870108")
                print("Current Interest rate: 3.4")
                print("Monthly Interest rate: 0.2833333333")
                print("Thanks for choosing us as your bank")
                break
