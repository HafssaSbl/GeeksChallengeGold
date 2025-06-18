from datetime import datetime

def afficher_gateau(nb_bougies):
    bougies = 'i' * nb_bougies
    print(f"       ___{bougies}___")
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")

def est_bissextile(annee):
    return (annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0))

def main():
    date_str = input("Entre ta date de naissance (format DD/MM/YYYY) : ")
    
    try:
        naissance = datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError:
        print("Format invalide. Utilise DD/MM/YYYY.")
        return
    
    aujourd_hui = datetime.today()
    age = aujourd_hui.year - naissance.year
    
    if (aujourd_hui.month, aujourd_hui.day) < (naissance.month, naissance.day):
        age -= 1
    
    derniere_chiffre = age % 10
    if derniere_chiffre == 0:
        derniere_chiffre = 10  
        
    nb_gateaux = 2 if est_bissextile(naissance.year) else 1
    
    for _ in range(nb_gateaux):
        afficher_gateau(derniere_chiffre)
        print() 
    
    print(f"Tu as {age} ans. Joyeux anniversaire !")

if __name__ == "__main__":
    main()
