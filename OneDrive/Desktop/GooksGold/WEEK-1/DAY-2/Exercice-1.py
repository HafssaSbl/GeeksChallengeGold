birthdays = {
    "Alice": "1990/05/12",
    "Bob": "1985/11/23",
    "Charlie": "2000/07/09",
    "Diana": "1992/02/28",
    "Ethan": "1988/09/17"
}

print("Bienvenue !")
print("You can look up the birthdays of the people in the list!")

name = input("Please enter a person's name: ")

birthday = birthdays.get(name)

if birthday:
    print(f"{name}'s birthday is on {birthday}.")
else:
    print(f"Sorry, I don't have the birthday information for {name}.")
