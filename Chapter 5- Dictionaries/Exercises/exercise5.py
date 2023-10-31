## Exercise 5: Pets 

# inputting pet information for three pets

pets = [{"Type": "Dog",
        "Breed": "Golden Retriever",
        "Name": "Brownie",
        "Owner": "Jennifer"},

       {"Type": "Cat",
        "Breed": "White Ragdoll",
        "Name": "Maru",
        "Owner": "Sakura"},

       {"Type": "Puppy",
        "Breed": "Samoyed",
        "Name": "Zuzu",
        "Owner": "Kazuha"}]


# looping the pet informations for all pets

for pet in pets:
    print("Pets Data:")
    for key, value in pet.items():
        print(f"{key}: {value}")
    print()