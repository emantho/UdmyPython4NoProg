
# Some type Errors

#### SYNTAXERROR
# print("Hello World" #-> SyntaxError; closing ) is missing
# if 10 > 50          #-> SyntaxError
#     print("Is mayor")

#### INDEXERROR
# list1 = [1,0]
# list1.pop() #-> IndexError; there's not more index to delete
# print(list1[1]) #-> IndexError; index out of range

# #### TYPEERROR
# number = input("Enter a number: ") #-> TypeError; int convertion is missing
# print(f"Addition is {number + 10}")

#### VALUEERROR
# number = int(input("Enter a number: ")) #-> ValueError; user enter a string instead of int/float
# print(f"Addition is {number + 10}")


## EXCEPTIONS

while True:
    try:
        number = int(input("Enter a number: ")) #-> ValueError; user enter a string instead of int/float
        print(f"Addition is {number + 10}")

    except:                                     # Exception has been captured and one message is displayed, so the program doesn't crash
        print("An error has ocurred")

    else:                                       # Only works when try is True, it means none exceptions is captured
        print("No news good news")
        break

    finally:                                    # It executes always, can be use when works with databases to close connection
        print("It works too")

print("Program Finished")