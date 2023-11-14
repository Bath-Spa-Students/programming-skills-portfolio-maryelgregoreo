# Exercise 2: Glossary 

#storing the meanings and their values

glossary = {"print": "displays the output to the screen.",
            "string": "sequencce of characters that is used as data.",
            "variable": "represents a value stored in the computer memory.",
            "list": "an object that contains multiple data items.",
            "f-string": " a readable way to interpolate and format strings."}

#using 'words' as the variable for listing the words 

words = ("print", "string", "variable", "list", "f-string")

#displaying "print" and its meaning
print (f'\n {words [0]} - {glossary["print"]}')

#displaying "string" and its meaning
print (f'\n {words [1]} - {glossary["string"]}')

#displaying "variable" and its meaning
print (f'\n {words [2]} - {glossary["variable"]}')

#displaying "list" and its meaning
print (f'\n {words [3]} - {glossary["list"]}')

#displaying "f-string" and its meaning
print (f'\n {words [4]} - {glossary["f-string"]}')