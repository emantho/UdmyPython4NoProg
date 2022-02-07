# Detect if phrase entered by user ends with (.); yes-> print "Ends with period" no-> "Does not ends with period"

phrase1 = input("\nEnter a Phrase: ")
if phrase1.endswith(".") == True:
    print("This phrase ends with period.")
else:
    print("This phrase does not ends with period.")
