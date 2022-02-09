# ''' Make a program with a Customer list, each one has Name, lastName and DNI.
# Menu
# 1. Add new Customer
# 2. Show all Customers
# 3. Show Customer by DNI
# 4. Erase Customer
# 5. Exit
# '''


customers = []
customers = [
{'name': 'Eder', 'last': 'Manjarres', 'dni': 95246796},
{'name': 'Diana', 'last': 'Pinzon', 'dni': 95246797},
{'name': 'Emilia', 'last': 'Manjarres', 'dni': 95246798},
{'name': 'Elmira', 'last': 'Moreno', 'dni': 95246799},
{'name': 'Aquileo', 'last': 'Pinzon', 'dni': 95246800},
{'name': 'Nelsy', 'last': 'Thomas', 'dni': 95246801},
{'name': 'Alex', 'last': 'Manjarres', 'dni': 95246802},
{'name': 'Jissel', 'last': 'Manjarres', 'dni': 95246803},
{'name': 'Angela', 'last': 'Pinzon', 'dni': 95246804}]

# --------------------------------------------- Functions start -----------------------------
# Adding Customers
def newCustomers(uName,uLastName,uDNI):
    newCustomer = {"name":uName,"last":uLastName,"dni":uDNI}
    customers.append(newCustomer)
    return newCustomer

# Showing customer
def showCustomers():
    for i in range(len(customers)):
        print(f"\nDNI : {customers[i]['dni']} \nName: {customers[i]['name']} {customers[i]['last']}")
        
# Showing customers by DNI
def showDni(uDNI):
    out = 0
    for i in range(len(customers)):
        out += 1 
        if uDNI == (customers[i]["dni"]):
            print(f"\nCustomer found: \nDNI:{customers[i]['dni']} \nName: {customers[i]['name']} {customers[i]['last']}")
            break
        else:
            if out == len(customers):
                print(f"Customer with DNI {uDNI} does not exist.")
            else:
                pass

# Deleting users
def deleteCustomers(customerToDelete):
    out = 0
    for i in range(len(customers)):
        if customerToDelete == (customers[i]["dni"]):
            print(f"The Customer with DNI {(customers[i]['dni'])} is {customers[i]['name']} {customers[i]['last']}")
            isDelete = input("Do you want to delete it, Y/n: ").lower()
            if isDelete == "y":
                customers.pop(i)
                print("Customer has been deleted succesfully")
                break
            else:
                break
        else:
            if out == len(customers):
                print(f"Customer with DNI {customerToDelete} does not exist.")
            else:
                pass

# --------------------------------------------- Functions end -----------------------------

# ________ Programm body start ____________
while True:
    option = int(input('''
_.Menu._
1. Add new customer
2. Show all customers
3. Show customer by DNI
4. Erase Customer
5. Exit
\nEnter you option: '''))
    
    if option == 1:
        name = input("\nEnter Name: ")
        last = input("Enter LastName: ")
        dni = int(input("Enter DNI: "))
        newCustomer = newCustomers(name,last,dni)
        print(f"\nNew Customer \n{newCustomer['name']} {newCustomer['last']} - with DNI {newCustomer['dni']} added succesfully")
    
    # Show Customers
    elif option == 2:
        print("\nCustomer(s) found: ")
        showCustomers()
    
    # show Customers by DNI
    elif option == 3:
        search = int(input("\nEnter Customer DNI to search: "))
        showDni(search)
                
    # Erase Customers
    elif option == 4:
        toDelete = int(input("\nEnter Customer DNI to delete: "))
        deleteCustomers(toDelete)

    # Exit
    elif option == 5:
        break
    else:
        print(f"\n{option} is not an option")

    # ________ Programm body end ____________

