# Calculatrice améliorée - Dorade

def additionner(a, b):
    return a + b

def soustraire(a, b):
    return a - b

def multiplier(a, b):
    return a * b

def diviser(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    return a / b

def afficher_menu():
    print("\n=== Calculatrice de Dorade ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

def main():
    while True:
        afficher_menu()
        choix = input("Ton choix : ")

        if choix == "5":
            print("Au revoir Dorade !")
            break

        if choix in ["1", "2", "3", "4"]:
            a = float(input("Premier nombre : "))
            b = float(input("Deuxième nombre : "))

            if choix == "1":
                print(f"Résultat : {additionner(a, b)}")
            elif choix == "2":
                print(f"Résultat : {soustraire(a, b)}")
            elif choix == "3":
                print(f"Résultat : {multiplier(a, b)}")
            elif choix == "4":
                print(f"Résultat : {diviser(a, b)}")
        else:
            print("Choix invalide, réessaie !")

main()
