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
