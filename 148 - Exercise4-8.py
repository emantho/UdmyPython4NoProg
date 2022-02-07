'''Make an ATM with 1000 as initial funds, and with this options
1- Deposit funds
2- Extract funds
3- Show funds
4- Exit
'''
exit = 4
user = 0
funds = 1000
while user != exit:
    user = int(input('''
    1- Deposit funds
    2- Extract funds
    3- Show funds
    4- Exit
    \n Choose an option: '''))
    if user == 1:
        deposit = float(input("\nEnter the amount to deposit: $"))
        funds += deposit
        print("\nYour deposit was succesful")
    elif user == 2:
        while True:
            extract = float(input("\nEnter the amount to extract: $"))
            if extract > funds:
                print("\nYou don't have that amount in your account")
            else:
                print("\nYour extraction was succesful")
                funds -= extract
                break
    elif user == 3:
        print(f"\nYour funds availables are: ${funds}")

    
print("\nHave a good Day, GoodBye ")
