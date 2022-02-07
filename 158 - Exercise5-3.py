# Verify is a phrase or word is palindrome. 

user1 = input("\nEnter a word or phrase: ") # user enter text
user1 = user1.replace(" ","") # eracing spaces

# l = len(user1) 
# print(user1[::-1]) 

compa1 = user1[::-1]

if user1 == compa1:

    print("is a palindrome")
else: print("Is not a palindrome")
   