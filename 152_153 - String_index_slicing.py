# Strings with " " or ' '
string = "i'm studying" # "" or '' nested
string2 = " I am \"studying\" " # using scape character

# Scapes characters
"\n" # line brak
"\t" # Tab or 4 spaces
"\''" # Scape 

# Forcing string 
path1 = r"D:\name\terminal"
print(path1)

# using Index
string3 = "Manjarres"
print(string3[3])

# slicing
print(string3[1:5])

# modifing string
string3 = 'm' + string3[1:]
print(string3)

# Erasing blanks spaces
string = string.replace(" ","")
print(string)