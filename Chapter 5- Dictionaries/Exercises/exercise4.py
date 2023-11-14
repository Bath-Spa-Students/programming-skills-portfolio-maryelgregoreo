## Exercise 4: Rivers 

# inputting rivers and their countries as values

rivers = {'Nile River': 'Egypt',
          'Amazon River': 'Brazil',
          'Rio Grande River': 'Mexico'}


# looping river and countries in a sentence

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")


# looping the names of rivers

print ('\nRivers:')
for river in rivers.keys():
    print(river)


# looping the countries that the rivers are located at

print("\nCountries:")
for country in rivers.values():
    print(country)
