from Model.Constantes import *
from Model.Pion import *


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not(c is None) and not type_pion(c)), True) == wrong:
        return False
    return True

def construirePlateau() -> list:
    """
    Construit un plateau vide
    :return: un plateau vide sous forme de double liste/Tableau 2D
    """
    plateau = []
    for i in range(const.NB_LINES):
        ligne =[]
        for j in range(const.NB_COLUMNS):
            ligne.append(None)
        plateau.append(ligne)
    return plateau

def placerPionPlateau(plateau: list, pion: dict, numCol: int) -> int:
    """
    Place un pion sur un plateau dans la colonne indiquée
    :param plateau: Paramètre liste où sera mis le pion
    :param pion: Paramètre dictionnaire désignant le pion mis sur le plateau
    :param numCol: entier représentant la colonne où se situe le pion
    :return: un entier correspondant à la ligne où est mis le pion sur le plateau
    """

    if not type_plateau(plateau):
        raise TypeError("placerPionPlateau : Le premier paramètre ne correspond pas à un plateau.")
    elif not type_pion(pion):
        raise TypeError("placerPionPlateau : Le second paramètre n’est pas un pion.")
    elif type(numCol) != int:
        raise TypeError("placerPionPlateau : Le troisième paramètre n’est pas un entier.")
    elif numCol > 6 or numCol < 0:
        raise ValueError("placerPionPlateau : La valeur de la colonne (valeur_du_paramètre) n’est pas correcte .")

    pos = False
    i = const.NB_LINES-1
    while not pos and i >= 0:
        if plateau[i][numCol] == None:
            plateau[i][numCol] = pion
            pos = True
            i += 1
        i -= 1
    return i
