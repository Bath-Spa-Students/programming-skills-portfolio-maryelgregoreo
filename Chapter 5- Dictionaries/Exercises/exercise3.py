## Exercise 3: Glossary 2 :ballot_box_with_check:

# inputting previous glossary

glossary_1 = {"print": "displays the output to the screen.",
            "string": "sequencce of characters that is used as data.",
            "variable": "represents a value stored in the computer memory.",
            "list": "an object that contains multiple data items.",
            "f-string": " a readable way to interpolate and format strings."}

words_1 = ("print", "string", "variable", "list", "f-string")


# looping to clean up the previous code
for words_1, definition in glossary_1.items():
    print(f"\n{words_1} - {definition}")



# adding another set of 5 words to the glossary 
glossary_2 = {"sequence": "an object that contains multiple items of data.",
              "index": "a number specifying the position of an element in a list.",
              "concatenate": "join two things together.",
              "slice": "a span of items that are taken from a sequence.",
              "sort": "used to sort the elements of the list in ascending order." }

words_2 = ("sequence", "index", "concatenate", "slice", "sort")


# looping the new glossary
for words_2, definition in glossary_2.items():
    print(f"\n{words_2} - {definition}")