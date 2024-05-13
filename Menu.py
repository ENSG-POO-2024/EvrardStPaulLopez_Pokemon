import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt



class Menu(QtWidgets.QMainWindow, object):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color : green")
        #titre principal
        self.setWindowTitle("Pokemon")
        #définir la taille du menu
        self.setGeometry(0, 0, 1100, 570)
        #self.label = QLabel("Green", self)
        font = QtGui.QFont()
        font.setFamily("Retro Gaming")

        #affichage du logo Pokemon
        self.logo("./qt_images/logo_pokemon.png")

        #créer l'icône en haut à droite de la fenêtre
        self.icone()

        #affichage des options
        self.options()
        self.show()
        return
    
    def icone(self):
        """
        génère l'icône de la fenêtre
        """
        #créer l'icône
        icone = QtGui.QIcon()
        #lui associer le logo Pokemon
        icone.addPixmap(QtGui.QPixmap("./qt_images/logo_pokemon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #associer le tout au Menu
        self.setWindowIcon(icone)
        return
    
    def logo(self, pixpath):
        """
        fonction générant le logo Pokemon dans le menu de démarrage
        """
        #créer le widget
        logo_pokemon = QtWidgets.QLabel(self)
        #charger l'image
        pixmap = QPixmap(pixpath)
        #l'associer au widget
        logo_pokemon.setPixmap(pixmap)
        #ajuster sa position et sa taille dans la fenêtre
        logo_pokemon.setGeometry(430, 50, 450, 300)

        


        return
    
    def nouveau(self, clicked = False):
        """
        lance une partie
        """
        

        return
    
    def reprendre(self, clicked = False):
        """
        permet de choisir une ancienne partie et de la reprendre
        """
        print(" Bouton Reprendre une partie ok")
        return
    
    def quitter(self, clicked = False):
        """
        permet de quitter le jeu
        """
        self.close()
        return
    
    def options(self):
        """
        fonction affichant les options du ménu de démarrage
        """
        #Créer la couche des options
        options = QtWidgets.QVBoxLayout()
        #et avec QStackedWidget ?

        #création des boutons et alignement vertical
        nouvPartie = QtWidgets.QPushButton("Nouvelle partie", self)
        Test = QtWidgets.QToolBar("Nouvelle partie", self)
        #750 de gauche vers la droite de l'écran
        #300 du haut vers le bas de l'écran
        nouvPartie.setGeometry(450, 285, 200, 50)

        rePartie = QtWidgets.QPushButton("Reprendre une partie", self)
        rePartie.setGeometry(450, 335, 200, 50)

        quitte = QtWidgets.QPushButton("Quitter", self)
        quitte.setGeometry(450, 385, 200, 50)
        
        #QtGui.QIcon()

        #connexion aux fonctions
        nouvPartie.clicked.connect(self.nouveau)
        rePartie.clicked.connect(self.reprendre)
        quitte.clicked.connect(self.quitter)

        return
    #fonctions déclenchant les options

    
    
    
    