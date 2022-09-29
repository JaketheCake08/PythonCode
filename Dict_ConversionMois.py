ConversionMois = {
    "Jan": "Janvier",
    "Fev": "Fevrier",
    "Mar": "Mars",
    "Avr": "Avril",
    "Mai": "Mai",
    "Jun": "Juin",
    "Jui": "Juillet",
    "Aou": "Aout",
    "Sep": "Septembre",
    "Oct": "Octobre",
    "Nov": "Novembre",
    "Dec": "Decembre",
}
#Une clé est unique
#Retourne la valeur lié à la clé
print(ConversionMois["Nov"])
#Même chose mais on retourne un message comme 2e argument si la clé
#n'existe pas
print(ConversionMois.get("Nov",'Invalide clé'))

#Retourne 'Invalide clé'
print(ConversionMois.get("Bob",'Invalide clé'))
