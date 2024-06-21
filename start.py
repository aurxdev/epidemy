from modele import Modele
from vue import Vue
import matplotlib.pyplot as plt
import sys

def main():

    tableau = [
        [0.03, 0.02, 0.005],  # grippe saisonnière
        [0.1, 0.02, 0.01],  # covid-19
        [0.2, 0.05, 0.1]  # peste noire
    ]
    indice=1

    modele = Modele(200, 200,tableau[indice][0],tableau[indice][1],tableau[indice][2],1)
    vue = Vue(modele)
    vue.run()

    """
    tab1 = []
    tab2 = []
    tab3 = []

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
    plt.xlabel('Générations')  # Ajoute une étiquette à l'axe des x
    plt.ylabel('Nombre de cas')  # Ajoute une étiquette à l'axe des y
    plt.savefig('graphique.png')"""


if __name__ == "__main__":
    main()