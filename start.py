from modele import Modele
from vue import Vue
import matplotlib.pyplot as plt
import sys

def main(indice, nbLignes, nbColonnes, mode):

    tableau = [
        [0.03, 0.02, 0.005],  # grippe saisonnière
        [0.1, 0.02, 0.01],  # covid-19
        [0.2, 0.05, 0.1]  # peste noire
    ]

    if mode == 0:
        modele = Modele(nbLignes, nbColonnes,tableau[indice][0],tableau[indice][1],tableau[indice][2],1)
        vue = Vue(modele)
        vue.run()

    else:
        tab1 = []
        tab2 = []
        tab3 = []

        modele = Modele(nbLignes, nbColonnes,tableau[indice][0],tableau[indice][1],tableau[indice][2],1)
        cpt = 0
        while cpt < 300:
            modele.evolution()
            cpt+=1



        plt.clf()
        plt.plot(modele.historiqueCasesInfectes, label='Infectées')
        plt.plot(modele.historiqueCasesGueries, label='Guéries')
        plt.plot(modele.historiqueCasesMortes, label='Mortes')
        plt.legend(loc='lower right')
        plt.title("Peste noire | Evolution de la pandémie en fonction des générations")
        plt.xlabel('Générations')
        plt.ylabel('Nombre de cas')
        plt.savefig('images/graphique.png')
        print("Graphique généré dans le dossier images/graphique.png")


def printHelp():
    print("------------------------------------")
    print("Usage: python start.py [MODEL] [NB_LIGNES] [NB_COLONNES] [MODE]")
    print("Simule l'évolution d'une épidémie en fonction du modèle choisi.")
    print()
    print("Modèles disponibles :")
    print("0 : grippe saisonnière")
    print("1 : covid-19")
    print("2 : peste noire")
    print()
    print("Mode disponible :")
    print("0 : Mode graphique (par défaut)")
    print("1 : Mode pour générer un graphique")
    print()
    print("Options:")
    print("-h, --help  affiche ce message d'aide")
    print("------------------------------------")



if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] in ["-h", "--help"]:
            printHelp()
            sys.exit(0)
        indice = int(sys.argv[1])
        if len(sys.argv) > 2:
            nbLignes = int(sys.argv[2])
        else:
            nbLignes = 100
        if len(sys.argv) > 3:
            nbColonnes = int(sys.argv[3])
        else:
            nbColonnes = 100
        if len(sys.argv) > 4:
            mode = int(sys.argv[4])
        else:
            mode = 0

        print("Simulation du modèle", indice, "avec une grille de", nbLignes, "lignes et", nbColonnes, "colonnes. Mode", mode)
        main(indice, nbLignes, nbColonnes, mode)
    else:
        print()
        print("Il faut passer un argument minimum pour choisir le modèle à simuler (0, 1 ou 2)")
        printHelp()
        sys.exit(1)