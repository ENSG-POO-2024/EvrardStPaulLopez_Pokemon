from PyQt5 import QtCore, QtGui, QtWidgets  
import ressources

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1346, 968)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(500, -100, 1201, 500))
        self.label_2.setObjectName("label_2")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(500, -100, 1201, 500))
        self.label_1.setObjectName("label_1")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_1.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/dresseur.png\"/></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/map.jpg\"/></p></body></html>"))
       

