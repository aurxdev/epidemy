from random import randint
import numpy as np

ETAT_SAIN = 0
ETAT_INFECTE = 1
ETAT_GUERI = 2
ETAT_MORT = 3

class Modele:
    def __init__(self, nbColonnes, nbLignes, a, b, c, pourcentage=20):
        self.nbColonnes = nbColonnes
        self.nbLignes = nbLignes
        self.total = self.nbColonnes * self.nbLignes

        # parametres du modèle
        self.a = a # taux d'infection
        self.b = b # taux de guérison
        self.c = c # taux de mortalité

        # nombre de cases 
        self.nbCasesInfectes = 0
        self.nbCasesGueries = 0
        self.nbCasesMortes = 0
        # tableau de cases
        self.historiqueCasesInfectes = []
        self.historiqueCasesGueries = []
        self.historiqueCasesMortes = []

        # on initialise la grille
        self.pourcentage = pourcentage
        self.grille=self.initGrille()

    ## GETTERS
    @property
    def nbCasesBasiques(self):
        return self.total - self.nbCasesInfectes - self.nbCasesGueries - self.nbCasesMortes

    def getNbCasesVivantes(self):
        return self.nbCasesVivantes

    # initialise la grille avec un pourcentage de cases sereines
    def initGrille(self):
        grille = [[0 for j in range(self.nbColonnes)] for i in range(self.nbLignes)]
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                if randint(0, 100) < self.pourcentage:
                    grille[i][j] = ETAT_INFECTE
                 
                else:
                    grille[i][j] = ETAT_SAIN
        return grille
    


    # compte le nombre de cases infectés autour de la case (i, j)
    def compteVoisinsInfectes(self,i,j):
        nbVoisins = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if (x,y) != (i,j) and x >= 0 and x < self.nbLignes and y >= 0 and y < self.nbColonnes:
                    if self.grille[x][y] == 1:
                        nbVoisins += 1
        return nbVoisins
    
    # fait évoluer la grille d'une génération
    def evolution(self):
        nouvelleGrille = [[0 for j in range(self.nbColonnes)] for i in range(self.nbLignes)]

        nbCasesInfectes=0
        nbCasesGueries=0
        nbCasesMortes=0
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                if self.grille[i][j] == 0: # S
                    nbVoisinsInfectes = self.compteVoisinsInfectes(i, j)
                    # on infecte la cellule avec alpha
                    if np.random.rand() < self.a * nbVoisinsInfectes:
                        nouvelleGrille[i][j] = ETAT_INFECTE
                        nbCasesInfectes+=1
                elif self.grille[i][j] == 1: # I
                    rand = np.random.rand()
                    # elle guérit avec beta
                    if rand < self.b:
                        nouvelleGrille[i][j] = ETAT_GUERI
                        nbCasesGueries+=1
                    # elle meurt avec beta + gamma
                    elif rand < self.b + self.c:
                        nouvelleGrille[i][j] = ETAT_MORT
                        nbCasesMortes+=1
                    else: # sinon elle reste infectée
                        nouvelleGrille[i][j] = ETAT_INFECTE
                        nbCasesInfectes+=1
                elif self.grille[i][j] == 2: # R
                    nouvelleGrille[i][j] = ETAT_GUERI
                    nbCasesGueries+=1
                else: # M
                    nouvelleGrille[i][j] = ETAT_MORT
                    nbCasesMortes+=1
        self.grille = nouvelleGrille
        self.nbCasesInfectes = nbCasesInfectes
        self.nbCasesGueries = nbCasesGueries
        self.nbCasesMortes = nbCasesMortes
        self.historiqueCasesInfectes.append(self.nbCasesInfectes)
        self.historiqueCasesGueries.append(self.nbCasesGueries)
        self.historiqueCasesMortes.append(self.nbCasesMortes)

    # vérifie si le jeu est fini
    def estFini(self):
        return self.nbCasesVivantes == 0 or self.nbCasesVivantes == self.total

    # affiche la grille sous forme textuelle
    def __str__(self):
        result = ""
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                result += str(self.grille[i][j])
            result+="\n"
        return result
    
    
