# Make a program to convert currency from USD to ARS

# Convert USD to ARS
def usdToArs(usd):
    ars = usd / 215
    return ars

def arsToUsd(ars):
    usd = ars * 215
    return usd

while True:
    option = int(input('''
Press 1 to conver ARS to USD
Press 2 to convert USD to ARS
Press 3 to exit
Option: '''))
    
    if option == 1:
        amount = float(input("\nWrite the amount of ARS to convert $: "))
        print(f"\n${amount} ARS are equivalent to U${usdToArs(amount):.2f} USD")
    elif option == 2:
        amount = float(input("\nWrite the amount of USD to convert $: "))
        print(f"\n${amount} USD are equivalent to ${arsToUsd(amount):.2f} ARS")
    elif option == 3:
        break
    else:
        print("Wrong Choise")
        print("\nGoodBye!!")

