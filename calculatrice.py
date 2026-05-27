# Calculatrice simple - Projet de Dorade

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

print("=== Calculatrice de Dorade ===")
print(additionner(10, 5))
print(soustraire(10, 5))
print(multiplier(10, 5))
print(diviser(10, 5))
