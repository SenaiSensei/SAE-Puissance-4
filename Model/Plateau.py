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
    if not type_pion(pion):
        raise TypeError("placerPionPlateau : Le second paramètre n’est pas un pion.")
    if type(numCol) != int:
        raise TypeError("placerPionPlateau : Le troisième paramètre n’est pas un entier.")
    if numCol > 6 or numCol < 0:
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

def detecter4horizontalPlateau(plateau: list, couleur: int) -> list:
    """
    Retourne une liste de liste de 4 pions aligné horizontalement de la couleur choisie
    :param plateau: Paramètre lu pour connaître la position des pions
    :param couleur: Paramètre de la couleur choisie
    :return: tableau 2D des pions alignés horizontalements
    """
    if not(type_plateau(plateau)):
        raise TypeError("detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau.")
    if type(couleur) != int:
        raise TypeError("detecter4horizontalPlateau : le second paramètre n’est pas un entier.")
    if couleur > 1 or couleur < 0:
        raise ValueError("detecter4horizontalPlateau : La valeur de la couleur (valeur_du_paramètre) n’est pas correcte.")

    listeSerie4 = []
    for i in range(const.NB_LINES):
        serie4 = []
        pos = []
        j = 0
        fin = False
        while j < const.NB_COLUMNS and not fin:
            if type_pion(plateau[i][j]):
                if plateau[i][j][const.COULEUR] == couleur:
                    serie4.append(plateau[i][j])
                    pos.append(j)

                if len(serie4) >=2:
                    f = len(serie4)-1
                    if pos[f] > pos[f-1]+1:
                        for h in range(f):
                            del pos[0]
                            del serie4[0]

            if len(serie4) >= 4:
                listeSerie4.extend(serie4)
                fin = True

            j += 1
    return listeSerie4

def detecter4verticalPlateau(plateau: list, couleur: int) -> list:
    """
        Retourne une liste de liste de 4 pions aligné verticalment de la couleur choisie
        :param plateau: Paramètre lu pour connaître la position des pions
        :param couleur: Paramètre de la couleur choisie
        :return: tableau 2D des pions alignés verticalement
        """
    if not (type_plateau(plateau)):
        raise TypeError("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau.")
    if type(couleur) != int:
        raise TypeError("detecter4verticalPlateau : le second paramètre n’est pas un entier.")
    if couleur > 1 or couleur < 0:
        raise ValueError("detecter4verticalPlateau : La valeur de la couleur (valeur_du_paramètre) n’est pas correcte.")

    listeSerie4 = []
    for j in range(const.NB_COLUMNS):
        serie4 = []
        pos = []
        i = 0
        fin = False
        while i < const.NB_LINES and not fin:
            if type_pion(plateau[i][j]):
                if plateau[i][j][const.COULEUR] == couleur:
                    serie4.append(plateau[i][j])
                    pos.append(i)

                if len(serie4) >= 2:
                    f = len(serie4) - 1
                    if pos[f] > pos[f - 1] + 1:
                        for h in range(f):
                            del pos[0]
                            del serie4[0]

            if len(serie4) >= 4:
                listeSerie4.extend(serie4)
                fin = True

            i += 1
    return listeSerie4

def detecter4diagonaleDirectePlateau(plateau: list, couleur: int) -> list:
    """
    Retourne une liste de liste de 4 pions aligné en diagonale directe de la couleur choisie
        :param plateau: Paramètre lu pour connaître la position des pions
        :param couleur: Paramètre de la couleur choisie
        :return: tableau 2D des pions alignés en diagonale directe
    """

    if not (type_plateau(plateau)):
        raise TypeError("detecter4diagonaleDirectePlateau : Le premier paramètre ne correspond pas à un plateau.")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleDirectePlateau : le second paramètre n’est pas un entier.")
    if couleur > 1 or couleur < 0:
        raise ValueError("detecter4diagonaleDirectePlateau : La valeur de la couleur (valeur_du_paramètre) n’est pas correcte.")


    listeSerie4 = []
    i = 0
    rep = 0
    j = 0
    ni = False
    while rep < const.NB_LINES:
        line = i
        col = j
        serie4 = []
        pos = []
        fin = False

        while col < const.NB_COLUMNS and line < const.NB_LINES and not fin:
            if type_pion(plateau[line][col]):
                if plateau[line][col][const.COULEUR] == couleur:
                    serie4.append(plateau[line][col])
                    pos.append((line, col))

                if len(serie4) >= 2:
                    f = len(serie4) - 1
                    if not pos[f][0] == pos[f - 1][0] + 1 or not pos[f][1] == pos[f - 1][1] + 1:
                        for r in range(f):
                            del pos[0]
                            del serie4[0]

            if len(serie4) >= 4:
                listeSerie4.extend(serie4)
                fin = True

            col += 1
            line += 1

        if j >= 3:
            ni = True
        else:
            j += 1

        if ni:
            i += 1
            j = 0

        rep += 1
    return listeSerie4

def detecter4diagonaleIndirectePlateau(plateau: list, couleur: int) -> list:
    """
        Retourne une liste de liste de 4 pions aligné en diagonale indirecte de la couleur choisie
            :param plateau: Paramètre lu pour connaître la position des pions
            :param couleur: Paramètre de la couleur choisie
            :return: tableau 2D des pions alignés en diagonale indirecte
        """

    if not (type_plateau(plateau)):
        raise TypeError("detecter4diagonaleIndirectePlateau : Le premier paramètre ne correspond pas à un plateau.")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleIndirectePlateau : le second paramètre n’est pas un entier.")
    if couleur > 1 or couleur < 0:
        raise ValueError("detecter4diagonaleIndirectePlateau : La valeur de la couleur (valeur_du_paramètre) n’est pas correcte.")

    listeSerie4 = []
    i = const.NB_LINES-1
    rep = 0
    j = 0
    ni = False
    while rep < const.NB_LINES:
        line = i
        col = j
        serie4 = []
        pos = []
        fin = False

        while col < const.NB_COLUMNS and line < const.NB_LINES and not fin:
            if type_pion(plateau[line][col]):
                if plateau[line][col][const.COULEUR] == couleur:
                    serie4.append(plateau[line][col])
                    pos.append((line, col))

                if len(serie4) >= 2:
                    f = len(serie4) - 1
                    if not pos[f][0] == pos[f - 1][0] - 1 or not pos[f][1] == pos[f - 1][1] + 1:
                        for r in range(f):
                            del pos[0]
                            del serie4[0]

            if len(serie4) >= 4:
                listeSerie4.extend(serie4)
                fin = True

            col += 1
            line -= 1

        if j >= 3:
            ni = True
        else:
            j += 1

        if ni:
            i -= 1
            j = 0

        rep += 1
    return listeSerie4

def getPionsGagnantsPlateau(plateau: list) -> list:
    """
    Fonction qui retourne les pions gagnants de chaque couleurs
    :param plateau: Liste des positions des pions sur le plateau
    :return: liste des pions de chaque couleurs aligné par 4 en ligne, en colonne et en digonale directe et indirecte
    """
    if not (type_plateau(plateau)):
        raise TypeError("getPionsGagnantsPlateau : Le paramètre n'est pas à un plateau.")

    listePionsGagnants = []
    listePionsRouge = []
    listePionsRouge.extend(detecter4verticalPlateau(plateau,const.ROUGE))
    listePionsRouge.extend(detecter4horizontalPlateau(plateau,const.ROUGE))
    listePionsRouge.extend(detecter4diagonaleDirectePlateau(plateau,const.ROUGE))
    listePionsRouge.extend(detecter4diagonaleIndirectePlateau(plateau,const.ROUGE))
    listePionsGagnants.extend(listePionsRouge)
    listePionsJaune = []
    listePionsJaune.extend(detecter4verticalPlateau(plateau,const.JAUNE))
    listePionsJaune.extend(detecter4horizontalPlateau(plateau,const.JAUNE))
    listePionsJaune.extend(detecter4diagonaleDirectePlateau(plateau,const.JAUNE))
    listePionsJaune.extend(detecter4diagonaleIndirectePlateau(plateau,const.JAUNE))
    listePionsGagnants.extend(listePionsJaune)
    return listePionsGagnants

def isRempliPlateau(plateau: list) -> bool:
    """
    Verifie si le plateau est rempli
    :param plateau: Liste des positions des pions sur le plateau
    :return: True si le plateau est rempli, False sinon
    """

    if not (type_plateau(plateau)):
        raise TypeError("isRempliPlateau : Le paramètre n'est pas à un plateau.")

    rempli = True
    i = 0
    while i < const.NB_LINES and rempli:
        j = 0
        while j < const.NB_COLUMNS and rempli:
            if plateau[i][j] == None:
                rempli = False
            j += 1
        i += 1
    return rempli


def placerPionLignePlateau(plateau: list, pion: dict, nb_ligne: int, left: bool) -> tuple:
    """
    Creer un déplacement horizontal pour les pions
    :param plateau: liste représentant le plateau
    :param pion: dictionnaire représentant le pion
    :param nb_ligne: entier correspondant à la ligne où est placer le pion
    :param left: True si le pion est mis par la gauche, False par la droite
    :return: un tuple avec les pions déplacer et la ligne auquel est tombé le dernier pion
    """

    if not type_plateau(plateau):
        raise TypeError("placerPionLignePlateau : Le premier paramètre n’est pas un plateau.")
    if not type_pion(pion):
        raise TypeError("placerPionLignePlateau : Le second paramètre n’est pas un pion.")
    if type(nb_ligne) != int:
        raise TypeError("placerPionLignePlateau : le troisième paramètre n’est pas un entier.")
    if nb_ligne < 0 or nb_ligne > const.NB_LINES-1:
        raise ValueError("placerPionLignePlateau : Le troisième paramètre (valeur_du_paramètre) ne désigne pas une ligne .")
    if type(left) != bool:
        raise TypeError("« placerPionLignePlateau : le quatrième paramètre n’est pas un booléen.")

    tombe = None
    listePion = [pion]
    if left:
        j = 0
        while j < const.NB_COLUMNS-1 and tombe is None:
            if plateau[nb_ligne][j] != None:
                listePion.append(plateau[nb_ligne][j])
                plateau[nb_ligne][j] = listePion[j]
            else :
                line = nb_ligne
                while line < const.NB_LINES:
                    if plateau[line][j] == None:
                        tombe = line
                    elif line == const.NB_COLUMNS:
                        tombe = const.NB_LINES
                    line += 1
            val = tombe
            if val is None:
                val = nb_ligne
            plateau[val][j] = listePion[j]
            j += 1
    else:
        j = const.NB_LINES
        compteur = 0
        while j >= 0 and tombe is None:
            if plateau[nb_ligne][j] != None:
                listePion.append(plateau[nb_ligne][j])
            else:
                line = nb_ligne
                while line < const.NB_LINES:
                    if plateau[line][j] == None:
                        tombe = line
                    elif line == 0:
                        tombe = const.NB_LINES
                    line += 1
            val = tombe
            if val is None:
                val = nb_ligne
            plateau[val][j] = listePion[compteur]
            j -= 1
            compteur += 1
    return (listePion, tombe)

def encoderPlateau(plateau: list) -> str:
    """
    Renvoie sous forme de chaîne de caractère les pions sur le plateau. "_" si c'est None, "R" si c'est un pion rouge et "J" si c'est un pion jaune
    :param plateau: liste correspondant au plateau de jeu
    :return: plateau de jeu sous forme de chaîne de caractère
    """

    if not type_plateau(plateau):
        raise TypeError("encoderPlateau : le paramètre ne correspond pas à un plateau.")

    res = ""
    for i in range(const.NB_LINES):
        line = ""
        for j in range(const.NB_COLUMNS):
            if plateau[i][j] == None:
                line += "_"
            elif plateau[i][j][const.COULEUR] == const.ROUGE:
                line += "R"
            elif plateau[i][j][const.COULEUR] == const.JAUNE:
                line += "J"
        res += line
    return res

def isPatPlateau(plateau: list, histoPlateau: dict) -> bool:
    """
    Vérifie si le plateau est apparu 5 fois
    :param plateau: liste correspondant au plateau de jeu
    :param histoPlateau: dictionnaire correspondant à l'histograme des plateaux de jeux
    :return: True si le plateau est apparu 5 fois, False sinon
    """

    if not type_plateau(plateau):
        raise TypeError("isPatPlateau : Le premier paramètre n’est pas un plateau.")
    if type(histoPlateau) != dict:
        raise TypeError("« isPatPlateau : Le second paramètre n’est pas un dictionnaire.")

    res = False
    plat = encoderPlateau(plateau)
    if plat in histoPlateau:
        histoPlateau[plat] += 1
        if histoPlateau[plat] >= 5:
            res = True
    else:
        histoPlateau[plat] = 1

    return res