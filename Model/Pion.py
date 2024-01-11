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
    :return: Un dictionnaire représentant le pion avec la couleur choisie
    """
    if type(couleur) != int:
        raise TypeError("construirePion : Le paramètre n’est pas de type entier ")
    if couleur > 1 or couleur < 0:
        raise ValueError("construirePion : la couleur (valeur_du_paramètre) n’est pas correcte")

    pion = {const.COULEUR: couleur, const.ID : None}
    return pion

def getCouleurPion(pion: dict) -> int:
    """
    Retourne la couleur du pion passé en paramètre
    :param pion: Paramètre dont on veut savoir la couleur
    :return: Un entier représentant la couleur du pion
    """
    if not(type_pion(pion)):
        raise TypeError("getCouleurPion : Le paramètre n’est pas un pion. ")
    return pion[const.COULEUR]

def setCouleurPion(pion: dict, couleur: int) -> None:
    """
    Change la couleur du pion avec la couleur en second paramètre
    :param pion: Paramètre dont on veut changer la couleur
    :param couleur: Paramètre qui définit la nouvelle couleur du pion
    :return: Rien
    """
    if not(type_pion(pion)):
        raise TypeError("setCouleurPion : Le premier paramètre n’est pas un pion. ")
    if type(couleur) != int:
        raise TypeError("setCouleurPion : Le second paramètre n’est pas un entier.")
    if couleur > 1 or couleur < 0:
        raise ValueError("setCouleurPion : Le second paramètre (valeur_du_second_paramètre) n’est pas une couleur.")

    pion[const.COULEUR] = couleur
    return None

def getIdPion(pion: dict) -> int:
    """
    Retourne l'identifiant du pion passé en paramètre
    :param pion: Paramètre dont on veut connaître l'identifiant
    :return: Un entier représentant l'identifiant du pion
    """
    if not type_pion(pion):
        raise TypeError("getIdPion : Le paramètre n’est pas un pion. ")
    return pion[const.ID]

def setIdPion(pion: dict, id: int) -> None:
    """
    Modifie l'identifiant du pion passer en paramètre avec le second paramètre
    :param pion: Paramètre dont on veut modifier l'identifiant
    :param id: Paramètre entier qui définit le nouvel identifiant du pion
    :return:
    """
    if not(type_pion(pion)):
        raise TypeError("setIdPion : Le premier paramètre n’est pas un pion. ")
    if type(id) != int:
        raise TypeError("setIdPion : Le second paramètre n’est pas un entier. ")
    pion[const.ID] = id
    return None

