class Eleve:
    def __init__(self, prenom, voisin_gauche=None, voisin_droite=None):
        self.prenom = prenom
        self.voisin_gauche = voisin_gauche
        self.voisin_droite = voisin_droite
    
    def __repr__(self):
        chaine_res = "prénom : " + self.prenom + "\n"
        if self.voisin_gauche != None :
            chaine_res += "\tvoisin de gauche : " + self.voisin_gauche.prenom + "\n"
        else :
            chaine_res += "\tvoisin de gauche : inexistant\n"
        if self.voisin_droite != None :
            chaine_res += "\tvoisin de droite : " + self.voisin_droite.prenom + "\n"
        else :
            chaine_res += "\tvoisin de droite : inexistant\n"
        return chaine_res
            
    def ajout_voisin_gauche(self, voisin):
        self.voisin_gauche = voisin

    def ajout_voisin_droite(self, voisin):
        self.voisin_droite = voisin

    def add_students(self, l_student, r_student):
        self.ajout_voisin_droite(r_student)
        self.ajout_voisin_gauche(l_student)
        l_student.ajout_voisin_droite(self)
        r_student.ajout_voisin_gauche(self)


def afficher_eleves(eleves):
    """ Amine : "cette fonction est très importante, vous devez absolument la comprendre" """
    nom_le_plus_long = 0
    for eleve in eleves:
        if len(eleve.prenom) > nom_le_plus_long:
            nom_le_plus_long = len(eleve.prenom)
    for eleve in eleves:
        espace_gauche = ' '* (nom_le_plus_long-len(eleve.voisin_gauche.prenom))
        cellule_gauche = f"{eleve.voisin_gauche.prenom}{espace_gauche}"
        espace_milieu = ' '*(nom_le_plus_long-len(eleve.prenom))
        cellule_milieu = f"{eleve.prenom}{espace_milieu}"
        espace_droite = ' '* (nom_le_plus_long-len(eleve.voisin_droite.prenom))
        cellule_droite = f"{eleve.voisin_droite.prenom}{espace_droite}"
        print(f"{cellule_gauche} ===   {cellule_milieu} ===   {cellule_droite}")

def elv_dans_lst(prenom: str, lst_elv):
    for elv in lst_elv:
        if elv.prenom == prenom:
            return elv
    return None

def add_elv(elv: Eleve, prenom_voisin_gauche: str, lst_elv):
    voisin_gauche = elv_dans_lst(prenom_voisin_gauche, lst_elv)
    if voisin_gauche != None:
        elv.add_students(voisin_gauche, voisin_gauche.voisin_droite)
        voisin_gauche.voisin_droite = elv
        elv.voisin_gauche.voisin_droite = elv
    for i in range(len(lst_elv)):
        if lst_elv[i].prenom == prenom_voisin_gauche:
            index_elv = i
    lst_elv.insert(index_elv+1, elv)

#TODO: creer une fonction qui peux suppr un eleve de la lst

def remove_student(elv: str, lst_elv):
    # Vérifie si l'élève existe
    remove_elv = elv_dans_lst(elv, lst_elv)
    if remove_elv is None:
        print(f"Élève '{elv}' introuvable.")
    else:
        # attribution nouveaux voisins gauche et droite
        g_elv = remove_elv.voisin_gauche
        d_elv = remove_elv.voisin_droite
        g_elv.ajout_voisin_droite(d_elv)
        d_elv.ajout_voisin_gauche(g_elv)
        # suppr elv
        lst_elv.remove(remove_elv)
        print(f"L'élève: {elv} a bien été suprimé !")

# def change_place_elv(elv, prenom_voisin_gauche, lst_elv):
#     change_elv = elv_dans_lst(elv, lst_elv)
#     if change_elv is None:
#         print(f"Élève '{elv}' introuvable.")
#     else:
#         g_elv = change_elv.voisin_gauche
#         d_elv = change_elv.voisin_droite
#         g_elv.ajout_voisin_droite(d_elv)
#         d_elv.ajout_voisin_gauche(g_elv)
#         lst_elv.remove(change_elv)
#         add_elv(elv, prenom_voisin_gauche, lst_elv)
#         print(f"L'élève {elv} a changé de place")


if __name__ == "__main__":
    noms_eleves = ["Thylio", "Mehmet", "Yann M", "Thomas", "Thibaut", "Mathis", "Noah", "Yann K", "Quentin", "Xavier", "Amine", "Laurent", "Noah L"]
    eleves_dans_lordre = [Eleve(nom) for nom in noms_eleves]

    #! Important: comprendre la boucle for
    for idx in range(len(eleves_dans_lordre)):
        eleve = eleves_dans_lordre[idx]
        voisin_gauche = None
        voisin_droite = None
        if idx == 0:
            voisin_gauche = eleves_dans_lordre[-1]
            voisin_droite = eleves_dans_lordre[idx+1]
        elif idx == len(eleves_dans_lordre)-1:
            voisin_gauche = eleves_dans_lordre[idx-1]
            voisin_droite = eleves_dans_lordre[0]
        else:
            voisin_gauche = eleves_dans_lordre[idx-1]
            voisin_droite = eleves_dans_lordre[idx+1]
        eleve.ajout_voisin_gauche(voisin_gauche)
        eleve.ajout_voisin_droite(voisin_droite)

    # affichage de la lst chainé
    afficher_eleves(eleves_dans_lordre)
    print("------------------------------------------")
    # ajout d'un éleve à droite de Quentin
    add_elv(Eleve("Lionel"), "Quentin", eleves_dans_lordre)
    afficher_eleves(eleves_dans_lordre)
    print("------------------------------------------")
    # Suppression d'un elève
    remove_student("Lionel", eleves_dans_lordre)
    afficher_eleves(eleves_dans_lordre)
    print("------------------------------------------")
    # Changer de place un élève
    # change_place_elv("Thylio", "Mathis", eleves_dans_lordre)
    # afficher_eleves(eleves_dans_lordre)
