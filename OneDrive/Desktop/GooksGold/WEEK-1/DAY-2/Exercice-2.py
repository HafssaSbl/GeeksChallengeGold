birthdays = {
    "Alice": "1990/05/12",
    "Bob": "1985/11/23",
    "Charlie": "2000/07/09",
    "Diana": "1992/02/28",
    "Ethan": "1988/09/17"
}

print("Voici les personnes dont nous avons les anniversaires :")
for name in birthdays.keys():
    print("-", name)

user_input = input("Veuillez entrer un nom parmi ceux listés ci-dessus : ")

if user_input in birthdays:
    print(f"L'anniversaire de {user_input} est le {birthdays[user_input]}.")
else:
    print(f"Désolé, nous n'avons pas l'information d'anniversaire pour {user_input}.")
