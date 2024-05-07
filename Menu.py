import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from PyQt5.QtGui import *



class Menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color : green")
        #titre principal
        self.setWindowTitle("Pokemon")
        #définir la taille du menu
        self.setGeometry(0, 0, 15000, 8000)
        #self.label = QLabel("Green", self)
        self.logo()
        self.show()
        return
    def logo(self, pixpath):
        """
        fonction générant le logo Pokemon dans le menu de démarrage
        """
        label = QtWidgets.QLabel(self)
        logoPokemon = QPixmap(pixpath)
        label.setPixmap(logoPokemon)
        self.setCentralWidget(label)

        logoPokemon.set


        return
