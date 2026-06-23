# Python code for ATM cash withdrawal Machine system

option = input("Select the option: ")
balance = int(input("Enter your account balance: "))

if option == "Cash Withdrawal":
    amount = int(input("Enter the amount you want to withdraw: "))
    if balance == 0:
        print("Low balance!!!")
    elif amount > balance:
        print("Insufficient balance!!!")
    else:
        pin = int(input("Enter your PIN: "))
        if len(str(pin)) < 4:
            print("Pin must be 4 digits long!!!")
        else:
            if(pin == 1234):
                print("Amount withdrawn successfully.")
                print("Remaining balance is: ", balance - amount)
            else:
                print("Invalid PIN!!!")
else:
    print("Invalid option selected.")

            