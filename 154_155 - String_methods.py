from ntpath import join


string = "Hello world".upper(); print(string) # can be used in print
string = "Hello world".lower(); print(string)
string = "Hello World".capitalize(); print(string) # Upper only first word
string = "hello world".title() ; print(string) # Upper first letter in all words
string = "Hello World".count("o") ; print(string) # how many times appears "o"
string = "hello world".find("o") ; print(string) # index of where is "o" first appearance
string = "Hello World".rfind("o") ; print(string) # index of where is "0" last appearance
string = "Hello World".split() ; print(string) # split the string in list, by default use space as limit
string = ";".join("Manjarres") ; print(string) # insert ";" in between each letter