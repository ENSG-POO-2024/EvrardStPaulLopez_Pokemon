import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt



class Menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color : green")
        #titre principal
        self.setWindowTitle("Pokemon")
        #définir la taille du menu
        self.setGeometry(0, 0, 15000, 8000)
        #self.label = QLabel("Green", self)

        #affichage du logo Pokemon
        self.logo("data/logo_pokemon.png")

        #affichage des options
        self.options()
        self.show()
        return
    
    def logo(self, pixpath):
        """
        fonction générant le logo Pokemon dans le menu de démarrage
        """
        titre = QtWidgets.QGraphicsScene()



        return
    def options(self):
        """
        fonction affichant les options du ménu de démarrage
        """
        #et avec QStackedWidget ?
        #création des boutons et alignement vertical
        nouvPartie = QtWidgets.QPushButton("Nouvelle partie")
        nouvPartie.setAlignment(Qt.AlignTop)
        rePartie = QtWidgets.QPushButton("Reprendre une partie")
        rePartie.setAlignment(Qt.AlignCenter)
        quitte = QtWidgets.QPushButton("Quitter")
        quitte.setAlignment(Qt.AlignBottom)
        #QtGui.QIcon()

        #connexion aux fonctions
        nouvPartie.clicked.connect(self.nouveau())
        rePartie.clicked.connect(self.reprendre())
        quitte.clicked.connect(self.quitter())

        return
    #fonctions déclenchant les options

    def nouveau(self):
        """
        lance une partie
        """
        return
    
    def reprendre(self):
        """
        permet de choisir une ancienne partie et de la reprendre
        """
        return
    def quitter(self):
        """
        permet de quitter le jeu
        """
        return
    
    
    
    