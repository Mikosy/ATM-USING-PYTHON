
initial_balance = 100000
pin = "1234"
name = "MIKE"


print("WELCOME TO BANK OF THE SOFTWARE DEVELOPERS " + (name))

while True:
    user_pin = input("Please enter your pin: ")

    if pin == user_pin:

        option = input("Press 1 to withdraw \n"
                        "2 to Transfer \n"
                        "3 to Buy Airtime \n"
                        "4 to Check Balance \n"
                        "5 to Change Pin \n"
                        "6 to Logout \n")

        if option == "1" :  
            withdraw_amount = int(input("How much do you want to withdraw: "))

            if withdraw_amount <= initial_balance:
                new_balance = initial_balance - withdraw_amount
                print("Thank you for banking with Us")
                print("Your new balance is", new_balance)
        
        if option == "2":
            account_number = int(input("account number: "))
            amount = int(input("Input transfer amount: "))

            if amount <= initial_balance:
                new_balance = initial_balance - amount
                print("Transfer Successful")
                print("Your new balance is", new_balance)

        if option == "3":
            airtime_amount = int(input("Enter the amount you want: "))
            airtime_network = input("Choose your network \n" 
                                    "1 for MTN \n"
                                    "2 for GLO \n"
                                    "3 for Airtel \n"
                                    "4 for 9mobile \n")
            if airtime_amount <= initial_balance:
                new_balance = initial_balance - airtime_amount
                print("Recharge Successfull")
                print("Your new balance is", new_balance)


        if option == 4:
            print("Your new balance is", initial_balance)

        
        
        if option == "5":
            old_pin = input("Please enter your old pin: ")

            if old_pin == pin:
                new_pin = input("Please enter your new pin: ")
                if len(new_pin) > 4 or len(new_pin) < 4 :
                    print("Pin characters must be 4")
                else:
                    pin = new_pin
                    print("Pin changed successfully")
                
            else:
                print("Incorrect pin")
                while old_pin != pin:
                    old_pin = input("Please enter your old pin44: ")
                    if old_pin == pin:
                        new_pin = input("Please enter your new pin: ")
                        if len(new_pin) > 4 or len(new_pin) < 4 :
                            print("Pin characters must be 4")
                        else:
                            pin = new_pin
                            print("Pin changed successfully")


        if option == 6:

            print("Logout")


    else:
        print("Insufficient Funds")

            
    
    