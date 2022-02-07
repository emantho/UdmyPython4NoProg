'''
Make a contact book, Using dictionary name:telephone. Option Menu:
1. Add contact
2. Delete contact
3. Show contacts
4. Exit
'''
agenda = {}
contact = ""
number = 0
while True:
    option = int(input(
    '''
Option menu:
1. Add contact
2. Delete contact
3. Show contacts
4. Exit
Choose an option: '''))
    if option == 1:
        contact = input("\nPlease write the contact name: ")
        number = int(input("\nPlease write the contact number: "))
        agenda[contact] = number
        print("\nContact has been stored succesfully!!")
    
    elif option == 2:
        while True:
            option = 0
            option = int(input("1. Delete using name | 2. Delete using number | 3. Exit. Option: "))
            if option == 1:
                contact = input("\nPlease write the name of contact to delete: ")
                del agenda[contact]
                print("\nContact has been deleted succesfully")
            elif option == 2:
                number = input("\nPlease write the number of contact to delete: ")
                del agenda[number]
                print("\nContact has been deleted succesfully")
            elif option == 3:
                False
                option == 0

    elif option == 3:
        print(f"\nContact(s) in agenda: {agenda}")

    elif option == 4:
        False
        break

print("\n\t¡¡¡Goodbye!!!")
