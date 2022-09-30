#Traducteur
# voyelle -> b

def traducteur(phrase):
    traduction = ""
    for lettre in phrase:
        if lettre.lower() in "aeiou":
            if lettre.isupper():
                traduction = traduction + "B"
            else:
                traduction = traduction + "b"
        else:
            traduction = traduction + lettre
    return traduction

x = input("Entrez votre phrase: ")
print(traducteur(x))