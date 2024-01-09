# Model/Pion.py

from Model.Constantes import *

#
# Ce fichier implémente les données/fonctions concernant le pion
# dans le jeu du Puissance 4
#
# Un pion est caractérisé par :
# - sa couleur (const.ROUGE ou const.JAUNE)
# - un identifiant de type int (pour l'interface graphique)
#
# L'identifiant sera initialisé par défaut à None
#

def type_pion(pion: dict) -> bool:
    """
    Détermine si le paramètre peut être ou non un Pion

    :param pion: Paramètre dont on veut savoir si c'est un Pion ou non
    :return: True si le paramètre correspond à un Pion, False sinon.
    """
    return type(pion) == dict and len(pion) == 2 and const.COULEUR in pion.keys() \
        and const.ID in pion.keys() \
        and pion[const.COULEUR] in const.COULEURS \
        and (pion[const.ID] is None or type(pion[const.ID]) == int)


def construirePion(couleur: int) -> dict:
    """
    Construit un Pion avec la couleur définie

    :param couleur: entier représentant la couleur choisie avec 1 : rouge et 0 : le jaune
    :return: Le pion avec la couleur choisie
    """
    if type(couleur) != int:
        raise TypeError("construirePion : Le paramètre n’est pas de type entier ")
    elif couleur > 1 or couleur < 0:
        raise ValueError("construirePion : la couleur (valeur_du_paramètre) n’est pas correcte")

    pion = {const.COULEUR: couleur, const.ID : None}
    return pion

def getCouleurPion(pion: dict) -> int:
    if type(pion) != dict or len(pion) != 2:
        raise TypeError("getCouleurPion : Le paramètre n’est pas un pion ")
    return pion[const.COULEUR]