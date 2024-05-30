# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design_MIR.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import matplotlib.pyplot as plt 



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Ouvrir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Ouvrir.setGeometry(QtCore.QRect(20, 390, 80, 23))
        self.btn_Ouvrir.setObjectName("btn_Ouvrir")
        self.btn_fm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fm.setGeometry(QtCore.QRect(140, 490, 80, 23))
        self.btn_fm.setObjectName("btn_fm")
        self.btn_fmedrian = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fmedrian.setGeometry(QtCore.QRect(20, 490, 80, 23))
        self.btn_fmedrian.setObjectName("btn_fmedrian")
        self.btn_fgaussien = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fgaussien.setGeometry(QtCore.QRect(240, 490, 131, 23))
        self.btn_fgaussien.setObjectName("btn_fgaussien")
        self.btn_sobelX = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sobelX.setGeometry(QtCore.QRect(400, 490, 80, 23))
        self.btn_sobelX.setObjectName("btn_sobelX")
        self.btn_histo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_histo.setGeometry(QtCore.QRect(320, 400, 80, 21))
        self.btn_histo.setObjectName("btn_histo")
        self.btn_sobely = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sobely.setGeometry(QtCore.QRect(520, 490, 80, 23))
        self.btn_sobely.setObjectName("btn_sobely")
        self.btn_sobel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sobel.setGeometry(QtCore.QRect(630, 490, 80, 23))
        self.btn_sobel.setObjectName("btn_sobel")
        self.btn_openCV = QtWidgets.QPushButton(self.centralwidget)
        self.btn_openCV.setGeometry(QtCore.QRect(600, 400, 80, 23))
        self.btn_openCV.setObjectName("btn_openCV")
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(70, 30, 651, 311))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_Ouvrir.clicked.connect(self.Ouvrir)  # liaison entre le bouton Ouvrir et la fonction Ouvrir
        self.btn_openCV.clicked.connect(self.OpenCV)  # liaison entre le bouton Ouvrir et la fonction Ouvrir
        self.btn_sobel.clicked.connect(self.Filtre_G)
        self.btn_sobely.clicked.connect(self.Filtre_Sobel_Y)
        self.btn_sobelX.clicked.connect(self.Filtre_Sobel_H)
        self.btn_fm.clicked.connect(self.Filtre_Moyen)
        self.btn_fmedrian.clicked.connect(self.Filtre_Median)
        self.btn_fgaussien.clicked.connect(self.Filtre_gaussien)
        self.btn_histo.clicked.connect(self.Histogramme)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Ouvrir(self, MainWindow):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "","Image Files (*.png *.jpeg *.jpg *.bmp)")
        if self.fileName:
            pixmap = QtGui.QPixmap(self.fileName)
        pixmap = pixmap.scaled(self.label_image.width(), self.label_image.height(), QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(pixmap)
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)

    def OpenCV(self,MainWindow):
        image = cv2.imread(self.fileName)  # lire l'image
        cv2.circle(image, (447, 63), 63, (0, 0, 255), 2)
        window_name = 'Image'  # nom de la fenêtre d'affichage
        cv2.imshow(window_name, image)  # Afficher l'image dans la fenêtre
        cv2.waitKey(0)  # Garder l'affichage visible

    def Filtre_Moyen(self,MainWindow):
        image = cv2.imread(self.fileName)  # lire l'image
        image=cv2.blur(image, (3, 3))
        window_name = 'Image'  # nom de la fenêtre d'affichage
        cv2.imshow(window_name, image)  # Afficher l'image dans la fenêtre
        cv2.waitKey(0)  # Garder l'affichage visible

    def Filtre_Median(self,MainWindow):
        image = cv2.imread(self.fileName)  # lire l'image
        image=cv2.medianBlur(image, 5)
        window_name = 'Image'  # nom de la fenêtre d'affichage
        cv2.imshow(window_name, image)  # Afficher l'image dans la fenêtre
        cv2.waitKey(0)  # Garder l'affichage visible

    def Filtre_gaussien(self,MainWindow):
        image = cv2.imread(self.fileName)  # lire l'image
        image=cv2.GaussianBlur(image, (7, 7), 0)
        window_name = 'Image'  # nom de la fenêtre d'affichage
        cv2.imshow(window_name, image)  # Afficher l'image dans la fenêtre
        cv2.waitKey(0)  # Garder l'affichage visible

    def Filtre_Sobel_H(self,MainWindow):
        image = cv2.imread(self.fileName)  # lire l'image
        image=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image=cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
        window_name = 'Image'  # nom de la fenêtre d'affichage
        cv2.imshow(window_name, image)  # Afficher l'image dans la fenêtre
        cv2.waitKey(0)  # Garder l'affichage visible

    def Filtre_Sobel_Y(self,MainWindow):
        image = cv2.imread(self.fileName)  # lire l'image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image = cv2.Sobel(image, cv2.CV_64F,0 , 1, ksize=5)

        window_name = 'Image'  # nom de la fenêtre d'affichage
        cv2.imshow(window_name, image)  # Afficher l'image dans la fenêtre
        cv2.waitKey(0)  # Garder l'affichage visible

    def Filtre_G(self,MainWindow):
        image = cv2.imread(self.fileName)  # lire l'image
        image=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image=(cv2.Sobel(image, cv2.CV_64F,0 , 1, ksize=5)**2+cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)**2)**(0.5)
        window_name = 'Image'  # nom de la fenêtre d'affichage
        cv2.imshow(window_name, image)  # Afficher l'image dans la fenêtre
        cv2.waitKey(0)  # Garder l'affichage visible

    def Histogramme(self,MainWindow):
        image = cv2.imread(self.fileName)  # lire l'image
        # Calculer les histogrammes pour chaque canal de couleur
        histr = cv2.calcHist([image], [0], None, [256], [0, 256])
        histb = cv2.calcHist([image], [1], None, [256], [0, 256])
        histg = cv2.calcHist([image], [2], None, [256], [0, 256])

        # Créer une nouvelle figure avec des sous-tracés
        fig, axs = plt.subplots(2, 1, figsize=(10, 8))

        # Tracer les histogrammes de chaque canal de couleur sur le premier sous-tracé
        axs[0].plot(histr, color='r', label='Rouge')
        axs[0].plot(histb, color='b', label='Bleu')
        axs[0].plot(histg, color='g', label='Vert')
        axs[0].set_title('Histogrammes de chaque canal de couleur')
        axs[0].legend()

        # Tracer l'histogramme de l'image en niveaux de gris sur le deuxième sous-tracé
        axs[1].hist(image.ravel(), 256, [0, 256], color='gray')
        axs[1].set_title('Histogramme en niveaux de gris')

        # Afficher les tracés
        plt.tight_layout()
        plt.show()

       
        






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_Ouvrir.setText(_translate("MainWindow", "Ouvrir"))
        self.btn_fm.setText(_translate("MainWindow", "Filtre Moyen"))
        self.btn_fmedrian.setText(_translate("MainWindow", "Filtre Median"))
        self.btn_fgaussien.setText(_translate("MainWindow", "Filtre Gaussien"))
        self.btn_sobelX.setText(_translate("MainWindow", "Sobel X"))
        self.btn_histo.setText(_translate("MainWindow", "Histogramme"))
        self.btn_sobely.setText(_translate("MainWindow", "Sobel Y"))
        self.btn_sobel.setText(_translate("MainWindow", "Sobel"))
        self.btn_openCV.setText(_translate("MainWindow", "OpenCV"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
