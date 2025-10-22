from stack import Stack
from operators import operateurs
from is_correct import is_correct

print("--------------Calculatrice NPI--------------")
print("Saisie : ")
print("\t Un nombre;")
print("\t ou un opérateur;")
print("\t ou 'q' pour quitter;")

stack = Stack()
saisie = ""
print("Calcul NPI:")
while(saisie !='q'):
    saisie = input("-> ")
    if is_correct(saisie):
        if saisie == 'q':
            print("C'est ciaoooooo !!!!")
        elif saisie not in operateurs:
            stack.push(int(saisie))
        else:
            if stack.size() >= 2:
                a, b = stack.pop(), stack.pop()
                if a != 0 or saisie != '/':
                    res = int(operateurs[saisie](b, a))
                    print(f"{b} {saisie} {a} = {res}")
                    stack.push(res)
                else:
                    print("Erreur : Division par zéro")
            else:
                print("Il y a pas assez de veleur dans la pile")
    else:
        print("ValueError")

#TODO: Gérer les erreurs de division par 0 (test fait sur fichier operators) + faire une interface graphique