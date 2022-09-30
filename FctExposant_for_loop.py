#Fonction Exposant

def exposant(base_num,exp_num):
    result = 1
    for i in range(exp_num):
        result = result * base_num
    return result
x = int(input('Entrez un nombre: '))
y = int(input('Entrez un exposant: '))
print(exposant(x,y))

