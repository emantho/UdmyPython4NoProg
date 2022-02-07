# Make an ATM with $1000 of initial funds and four options, ingress, withdraw, show funds, exit

from ast import Break


initialFunds = 1000
option = int(input('''Welcome to you ATM
1. Deposit funds
2. Extract funds
3. See funds
4. Exit
\nPlease choose an option:'''))

if option == 1: #deposit 
    depo = float(input("Write amount to deposit: $"))
    print(f"Your new funds are ${initialFunds + depo}")

elif option == 2: # Extraction
    extr = float(input("Write amount to extract: $"))
    if extr >= initialFunds:
        print("You don't have the quantity solicited")
    else: print(f"Your new funds are ${initialFunds - extr}")

elif option == 3: # See funds
    print(f"Your funds are ${initialFunds}")

elif option == 4: # Exits
    print("Good Bye!!")
    Break



