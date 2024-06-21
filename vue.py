from modele import Modele
import pygame
import matplotlib.pyplot as plt
import os
from var import *

pygame.font.init()

class Vue:
    def __init__(self, modele):
        self.modele = modele
        self.largeur = 800
        self.hauteur = 800
        self.tailleCase = self.largeur // self.modele.nbColonnes
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        self.clock = pygame.time.Clock()
        self.running = True
        self.pause = False
        self.couleurBordure = (100, 100, 100)
        self.couleurFond = (50, 50, 50)
        self.couleurTexte = (255, 255, 255)
        self.font = pygame.font.Font(None, 36)
   


    def afficheGrille(self):
        self.fenetre.fill(self.couleurFond)
        for i in range(self.modele.nbLignes):
            for j in range(self.modele.nbColonnes):
                if self.modele.grille[i][j] == ETAT_SAIN:
                    couleur = (0,0,255)
                elif self.modele.grille[i][j] == ETAT_INFECTE:
                    couleur = (255,0,0)
                elif self.modele.grille[i][j] == ETAT_GUERI:
                    couleur = (0,255,0)
                else:
                    couleur = (0,0,0)
                rect = pygame.Rect(j * self.tailleCase, i * self.tailleCase, self.tailleCase, self.tailleCase)
                pygame.draw.rect(self.fenetre, couleur, rect)
                pygame.draw.rect(self.fenetre, self.couleurBordure, rect, 1)
        self.texte = self.font.render(f"Nombre de cases mortes : {self.modele.nbCasesMortes}", True, self.couleurTexte)
        self.fenetre.blit(self.texte, (10, self.hauteur-50))
        self.texte2 = self.font.render(f"Nombre de cases infectées : {self.modele.nbCasesInfectes}", True, self.couleurTexte)
        self.fenetre.blit(self.texte2, (10, self.hauteur-110))
        self.texte3 = self.font.render(f"Nombre de cases guéries : {self.modele.nbCasesGueries}", True, self.couleurTexte)
        self.fenetre.blit(self.texte3, (10, self.hauteur-80))
        self.texte4 = self.font.render(f"Nombre de cases saines : {self.modele.nbCasesBasiques}", True, self.couleurTexte)
        self.fenetre.blit(self.texte4, (10, self.hauteur-140))
        pygame.display.flip()

    def run(self):
        while self.running:
            self.afficheGrille()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.pause = not self.pause
                    if event.key == pygame.K_r:
                        plt.clf()
                        plt.plot(self.modele.historiqueCasesInfectes, label='Infectées')
                        plt.plot(self.modele.historiqueCasesGueries, label='Guéries')
                        plt.plot(self.modele.historiqueCasesMortes, label='Mortes')
                        plt.legend()
                        plt.title("Evolution de la pandémie en fonction des générations")
                        plt.savefig('graphique.png')
            if not self.pause:
                self.modele.evolution()
            self.clock.tick(5)
        pygame.quit()

    
