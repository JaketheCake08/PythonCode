#Test questions à choix multiples

#Importer la classe Question d'un autre fichier Question.py

#class Question:
#    def __init__(self,instruction,reponse):
#        self.instruction = instruction
#        self.reponse = reponse

from Question import Question

Q = [
    "Quel est la couleur d'une pomme\n(a) Rouge/Vert\n(b) Mauve\n(c) Orange\n\n",
    "Quel est la couleur d'une banane\n(a) Brun\n(b) Mangenta\n(c) Jaune\n\n",
    "Quel est la couleur d'une framboise\n(a) Jaune\n(b) Rouge\n(c) Bleu\n\n"
]


reponses = [
    Question(Q[0],"a"),
    Question(Q[1], "c"),
    Question(Q[2], "b")

]


def run_test(reponses):
    score = 0
    for question in reponses:
        rep = input(question.instruction)
        if rep == question.reponse:
            score +=1
    print("Vous avez %i sur %i bonnes réponses"%(score,len(reponses)))

run_test(reponses)
