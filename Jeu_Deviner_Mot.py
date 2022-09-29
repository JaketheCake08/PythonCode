#importation de random pour éviter que l'utilisateur entre un nombre au lancement du programme
import random

#Liste de mots à découvrir
epee = {"Mot secret": "Épée","indice": ["Moyen-Âge","Arme blanche","Excalibur"]}
tomate = {"Mot secret": "Tomate","indice": ["Légume","Rouge","Sauce"]}
auto = {"Mot secret": "Auto","indice":["Transport","Métal","4 roues"]}
#print(epee["indice"][0])

#Le tout dans une liste pour les repérer facilement, .append pour ajouter des mots secrects
list = [epee,tomate,auto]

#Fonction pour le jeu, limite de 4 essais
def Trouver_le_mot(x):
    essai_count = 0
    essai = ""
    essai_limit = 4
    essai_fin = False
    mot_secret = list[essai_count]["Mot secret"]
    print('Jouons au jeu de deviner le mot!')
    while essai != mot_secret and not (essai_fin):
        indice1 = list[x]["indice"][0]
        indice2 = list[x]["indice"][1]
        indice3 = list[x]["indice"][2]
        if essai_count < essai_limit:
            essai = input("Entrez votre essai:")
            essai_count += 1
            print(essai_count, "essai sur 4")
            if essai_count == 1:
                print("Premier indice: " + indice1)
            if essai_count == 2:
                print("Deuxième indice: " + indice2)
            if essai_count == 3:
                print("Troisième indice:" + indice3)
        else:
            essai_fin = True

    if essai_fin:
        print("Dommage!")
    else:
        print("Bravo!")

mot = random.randint(0,(len(list)-1))
Trouver_le_mot(mot)
