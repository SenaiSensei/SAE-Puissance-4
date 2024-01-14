# Essais sur les couleurs
print("\x1B[43m \x1B[0m : carré jaune ")
print("\x1B[41m \x1B[0m : carré rouge ")
print("\x1B[41mA\x1B[0m : A sur fond rouge")




def toStringPlateau(plateau: list) -> str:
    """
    Affiche un plateau de jeu sur la console
    :param plateau: liste représentant le plateau
    :return: un str représentant le plateau de jeu
    """
    p = ""
    for i in range(const.NB_LINES):
        ligne = "|"
        for j in range(const.NB_COLUMNS):
            if type_pion(plateau[i][j]) and plateau[i][j][const.COULEUR] == 0:
                ligne = ligne + "\x1B[43m \x1B[0m" + "|"
            elif type_pion(plateau[i][j]) and plateau[i][j][const.COULEUR] == 1:
                ligne = ligne + "\x1B[41m \x1B[0m" + "|"
            else:
                ligne = ligne + " |"
        p = p + ligne + "\n"
    p = p + "---------------" + "\n"
    for i in range(const.NB_COLUMNS):
        p = p + f"{i:>2}" + ""
    return p

from Model.Constantes import *
from Model.Plateau import *
from Model.Pion import *
from random import randint, choice
"""p = construirePlateau()
for _ in range(20):
    placerPionPlateau(p, construirePion(choice(const.COULEURS)),randint(0, const.NB_COLUMNS - 1))
print(toStringPlateau(p))"""

p2 = construirePlateau()
print(p2)
for _ in range(30):
    placerPionPlateau(p2, construirePion(choice(const.COULEURS)),randint(0, const.NB_COLUMNS - 1))
    print(toStringPlateau(p2))
print(getPionsGagnantsPlateau(p2))

print(isRempliPlateau(p2))