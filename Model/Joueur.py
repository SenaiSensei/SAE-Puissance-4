from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *



#
# Ce fichier contient les fonctions gérant le joueur
#
# Un joueur sera un dictionnaire avec comme clé :
# - const.COULEUR : la couleur du joueur entre const.ROUGE et const.JAUNE
# - const.PLACER_PION : la fonction lui permettant de placer un pion, None par défaut,
#                       signifiant que le placement passe par l'interface graphique.
# - const.PLATEAU : référence sur le plateau de jeu, nécessaire pour l'IA, None par défaut
# - d'autres constantes nécessaires pour lui permettre de jouer à ajouter par la suite...
#

def type_joueur(joueur: dict) -> bool:
    """
    Détermine si le paramètre peut correspondre à un joueur.

    :param joueur: Paramètre à tester
    :return: True s'il peut correspondre à un joueur, False sinon.
    """
    if type(joueur) != dict:
        return False
    if const.COULEUR not in joueur or joueur[const.COULEUR] not in const.COULEURS:
        return False
    if const.PLACER_PION not in joueur or (joueur[const.PLACER_PION] is not None
            and not callable(joueur[const.PLACER_PION])):
        return False
    if const.PLATEAU not in joueur or (joueur[const.PLATEAU] is not None and
        not type_plateau(joueur[const.PLATEAU])):
        return False
    return True

def construireJoueur(couleur: int) -> dict:
    """
    Construire un joueur de la couleur passer en paramètre
    :param couleur: entier qui représente la couleur du joueur
    :return: dictionnaire avec la couleur, le plateau initialisé à None et les pions placer du joueur initialisé à None
    """

    if type(couleur) != int:
        raise TypeError('construireJoueur : Le paramètre n’est pas un entier.')
    if couleur > 1 or couleur < 0:
        raise ValueError('construireJoueur :  L’entier donné (valeur_du_paramètre) n’est pas une couleur.')
    joueur = {const.COULEUR: couleur, const.PLATEAU : None, const.PLACER_PION: None}
    return joueur

def getCouleurJoueur(joueur: dict) -> int:
    """
    Retourne la couleur du joueur passer en paramètre
    :param joueur: Paramètre dictionnaire représentant le joueur
    :return: couleur du joueur sous la forme d'un entier
    """

    if not type_joueur(joueur):
        raise TypeError('« getCouleurJoueur : Le paramètre ne correspond pas à un joueur.')

    return joueur[const.COULEUR]

def getPlateauJoueur(joueur: dict) -> list:
    """
    Retourne le plateau du joueur passer en paramètre
    :param joueur: Paramètre dictionnaire représentant le joueur
    :return: plateau du joueur sous la forme d'une liste
    """

    if not type_joueur(joueur):
        raise TypeError('« getPlateauJoueur : Le paramètre ne correspond pas à un joueur.')

    return joueur[const.PLATEAU]

def getPlacerPionJoueur(joueur: dict) -> dict:
    """
    Retourne le placerPion du joueur passer en paramètre
    :param joueur: Paramètre dictionnaire représentant le joueur
    :return: placerPion du joueur sous la forme d'un dictionnaire
    """

    if not type_joueur(joueur):
        raise TypeError('« getPlacerPionJoueur : Le paramètre ne correspond pas à un joueur.')

    return joueur[const.PLACER_PION]

def getPionJoueur(joueur: dict) -> dict:
    """
    Retourne le pion de la couleur du joueur passer en paramètre
    :param joueur: Paramètre dictionnaire représentant le joueur
    :return: Pion de la couleur du joueur sous forme de dictionnaire
    """

    if not type_joueur(joueur):
        raise TypeError('« getPionJoueur : Le paramètre ne correspond pas à un joueur.')

    pion = construirePion(joueur[const.COULEUR])
    return pion

def setPlateauJoueur(joueur: dict, plateau: list) -> None:
    """
    Modifie le plateau du joueur passer en paramètre
    :param joueur: Paramètre dictionnaire représentant le joueur
    :param plateau: Parmètre liste représentant le plateau
    :return: Rien
    """

    if not type_joueur(joueur):
        raise TypeError('setPlateauJoueur : Le premier paramètre ne correspond pas à un joueur.')
    if not type_plateau(plateau):
        raise TypeError('setPlateauJoueur :  Le second paramètre ne correspond pas à un plateau.')

    joueur[const.PLATEAU] = plateau
    return None

def setPlacerPionJoueur(joueur: dict, fn: callable) -> None:
    """
    Modifie le placerPion du joueur passer en paramètre
    :param joueur: Paramètre dictionnaire représentant le joueur
    :param plateau: Parmètre liste représentant le plateau
    :return: Rien
    """

    if not type_joueur(joueur):
        raise TypeError('setPlacerPionJoueur : Le premier paramètre ne correspond pas à un joueur.')
    if not callable(fn):
        raise TypeError('setPlacerPionJoueur :  Le second paramètre  n’est pas une fonction.')

    joueur[const.PLACER_PION] = fn
    return None

