# Calculatrice NPI

Calculatrice en **Notation Polonaise Inversée** (NPI) écrite en Python, disponible en **mode console** et avec une **interface graphique PyQt5**.

## Qu'est-ce que la NPI ?

La notation polonaise inversée (ou notation postfixée) place les opérateurs **après** leurs opérandes, ce qui supprime le besoin de parenthèses. Le calcul repose sur une **pile** :

- un nombre est **empilé** ;
- un opérateur **dépile** les deux derniers nombres, applique l'opération et **empile** le résultat.

| Notation classique | Notation NPI |
|--------------------|--------------|
| `3 + 4`            | `3 4 +`      |
| `(5 + 2) * 3`      | `5 2 + 3 *`  |
| `8 / (4 - 2)`      | `8 4 2 - /`  |

## Fonctionnalités

- Opérations : addition, soustraction, multiplication et division
- Pile affichée en temps réel dans l'interface graphique
- Affichage de la dernière opération effectuée (ex. : `3 + 4 = 7`)
- Gestion des erreurs : division par zéro, pile contenant moins de deux valeurs, saisie invalide
- Deux modes d'utilisation : console et interface graphique
- Interface personnalisable via une feuille de style `style.css`

## Structure du projet

| Fichier         | Rôle                                                                 |
|-----------------|----------------------------------------------------------------------|
| `main.py`       | Point d'entrée de l'application graphique (relie boutons et logique) |
| `interface.py`  | Fenêtre PyQt5 : boutons, labels, mise en page                        |
| `logic.py`      | Logique de la calculatrice (traitement des saisies, pile, erreurs)   |
| `npi.py`        | Version console de la calculatrice                                   |
| `stack.py`      | Implémentation de la structure de pile                               |
| `operators.py`  | Définition des opérateurs disponibles                                |
| `is_correct.py` | Vérification de la validité d'une saisie                             |
| `style.css`     | Style de l'interface graphique                                       |

## Installation

**Prérequis :** Python 3 et pip.

```bash
# Cloner le dépôt
git clone https://github.com/Thib00w/Calculatrice-NPI.git
cd Calculatrice-NPI

# Installer la dépendance de l'interface graphique
pip install PyQt5
```

## Utilisation

### Interface graphique

```bash
python main.py
```

> Lance la commande depuis le dossier du projet : `style.css` est chargé depuis le répertoire courant.

La fenêtre contient un pavé numérique (0 à 9) et les quatre opérateurs. Chaque chiffre est empilé, et un opérateur s'applique aux deux dernières valeurs de la pile.

**Exemple :** pour calculer `3 + 4`, appuie sur `3`, `4`, puis `+`.

### Mode console

```bash
python npi.py
```

Saisis un nombre ou un opérateur à chaque invite, et `q` pour quitter.

```text
--------------Calculatrice NPI--------------
Calcul NPI:
-> 3
-> 4
-> +
3 + 4 = 7
-> q
```

## 🛠️ Technologies

- **Python 3**
- **PyQt5** pour l'interface graphique

## Pistes d'amélioration

- Gérer les nombres à plusieurs chiffres dans l'interface graphique
- Ajouter des boutons *Entrée*, *Effacer* et *Annuler*
- Prendre en charge les nombres décimaux
- Ajouter des tests unitaires

## Auteur

**Thibaut Commeau** — [@Thib00w](https://github.com/Thib00w)
