# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QApplication
import cv2
import numpy as np
from skimage.transform import resize
from skimage.io import imread
from skimage.feature import hog
from skimage import exposure
from matplotlib import pyplot as plt
from functions import extractReqFeatures, showDialog, generateSIFT,generateHistogramme_HSV, generateHistogramme_Color, generateORB, generateLBP, generateHOG, generateGLCM
import time
from distances import *
filenames= "images"
folder_model=""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1234, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imagelabel = QtWidgets.QLabel(self.centralwidget)
        self.imagelabel.setGeometry(QtCore.QRect(10, 110, 261, 231))
        self.imagelabel.setText("")
        self.imagelabel.setObjectName("imagelabel")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1041, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.checkBox_SIFT = QtWidgets.QCheckBox(self.tab)
        self.checkBox_SIFT.setGeometry(QtCore.QRect(120, 0, 85, 21))
        self.checkBox_SIFT.setObjectName("checkBox_SIFT")
        self.checkBox_ORB = QtWidgets.QCheckBox(self.tab)
        self.checkBox_ORB.setGeometry(QtCore.QRect(190, 0, 85, 21))
        self.checkBox_ORB.setObjectName("checkBox_ORB")
        self.checkBox_HistC = QtWidgets.QCheckBox(self.tab)
        self.checkBox_HistC.setGeometry(QtCore.QRect(260, 0, 121, 21))
        self.checkBox_HistC.setObjectName("checkBox_HistC")
        self.checkBox_HSV = QtWidgets.QCheckBox(self.tab)
        self.checkBox_HSV.setGeometry(QtCore.QRect(380, 0, 101, 21))
        self.checkBox_HSV.setObjectName("checkBox_HSV")
        self.checkBox_GLCM = QtWidgets.QCheckBox(self.tab)
        self.checkBox_GLCM.setGeometry(QtCore.QRect(480, 0, 81, 21))
        self.checkBox_GLCM.setObjectName("checkBox_GLCM")
        self.checkBox_LBP = QtWidgets.QCheckBox(self.tab)
        self.checkBox_LBP.setGeometry(QtCore.QRect(560, 0, 61, 21))
        self.checkBox_LBP.setObjectName("checkBox_LBP")
        self.checkBox_HOG = QtWidgets.QCheckBox(self.tab)
        self.checkBox_HOG.setGeometry(QtCore.QRect(630, 0, 71, 21))
        self.checkBox_HOG.setObjectName("checkBox_HOG")
        self.charger = QtWidgets.QPushButton(self.tab)
        self.charger.setGeometry(QtCore.QRect(10, 20, 441, 51))
        self.charger.setObjectName("charger")
        self.indexer = QtWidgets.QPushButton(self.tab)
        self.indexer.setGeometry(QtCore.QRect(460, 20, 451, 51))
        self.indexer.setObjectName("indexer")
        self.indexer_2 = QtWidgets.QPushButton(self.tab)
        self.indexer_2.setGeometry(QtCore.QRect(920, 20, 71, 51))
        self.indexer_2.setObjectName("indexer_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(460, 80, 531, 31))
        self.label_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 80, 441, 31))
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(460, 120, 531, 331))
        self.tableView.setObjectName("tableView")
        self.image = QtWidgets.QLabel(self.tab)
        self.image.setGeometry(QtCore.QRect(10, 120, 441, 331))
        self.image.setFrameShape(QtWidgets.QFrame.Panel)
        self.image.setText("")
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(10, 462, 981, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 0, 91, 21))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.checkBox_GLCM_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_GLCM_2.setGeometry(QtCore.QRect(200, 110, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_GLCM_2.setFont(font)
        self.checkBox_GLCM_2.setObjectName("checkBox_GLCM_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.checkBox_LBP_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_LBP_2.setGeometry(QtCore.QRect(120, 110, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_LBP_2.setFont(font)
        self.checkBox_LBP_2.setObjectName("checkBox_LBP_2")
        self.label_requete = QtWidgets.QLabel(self.tab_2)
        self.label_requete.setGeometry(QtCore.QRect(10, 180, 361, 251))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_requete.setFont(font)
        self.label_requete.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_requete.setText("")
        self.label_requete.setScaledContents(True)
        self.label_requete.setAlignment(QtCore.Qt.AlignCenter)
        self.label_requete.setObjectName("label_requete")
        self.checkBox_HistC_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_HistC_2.setGeometry(QtCore.QRect(120, 50, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_HistC_2.setFont(font)
        self.checkBox_HistC_2.setObjectName("checkBox_HistC_2")
        self.chercher = QtWidgets.QPushButton(self.tab_2)
        self.chercher.setGeometry(QtCore.QRect(840, 50, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.chercher.setFont(font)
        self.chercher.setObjectName("chercher")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(380, 140, 561, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.charger_2 = QtWidgets.QPushButton(self.tab_2)
        self.charger_2.setGeometry(QtCore.QRect(10, 50, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.charger_2.setFont(font)
        self.charger_2.setObjectName("charger_2")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(700, 50, 131, 41))
        self.comboBox.setObjectName("comboBox")
        self.checkBox_HOG_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_HOG_2.setGeometry(QtCore.QRect(300, 50, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_HOG_2.setFont(font)
        self.checkBox_HOG_2.setObjectName("checkBox_HOG_2")
        self.checkBox_SIFT_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_SIFT_2.setGeometry(QtCore.QRect(120, 80, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_SIFT_2.setFont(font)
        self.checkBox_SIFT_2.setObjectName("checkBox_SIFT_2")
        self.checkBox_HSV_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_HSV_2.setGeometry(QtCore.QRect(200, 50, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_HSV_2.setFont(font)
        self.checkBox_HSV_2.setObjectName("checkBox_HSV_2")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_2.setGeometry(QtCore.QRect(10, 440, 931, 41))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.charger_desc = QtWidgets.QPushButton(self.tab_2)
        self.charger_desc.setGeometry(QtCore.QRect(380, 50, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.charger_desc.setFont(font)
        self.charger_desc.setObjectName("charger_desc")
        self.checkBox_ORB_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_ORB_2.setGeometry(QtCore.QRect(200, 80, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_ORB_2.setFont(font)
        self.checkBox_ORB_2.setObjectName("checkBox_ORB_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(120, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(380, 10, 561, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(590, 50, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(380, 180, 561, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Quitter_2 = QtWidgets.QPushButton(self.tab_2)
        self.Quitter_2.setGeometry(QtCore.QRect(950, 440, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Quitter_2.setFont(font)
        self.Quitter_2.setObjectName("Quitter_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.image_2 = QtWidgets.QLabel(self.tab_3)
        self.image_2.setGeometry(QtCore.QRect(10, 110, 441, 331))
        self.image_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.image_2.setText("")
        self.image_2.setScaledContents(True)
        self.image_2.setObjectName("image_2")
        self.tableView_2 = QtWidgets.QTableView(self.tab_3)
        self.tableView_2.setGeometry(QtCore.QRect(460, 110, 531, 331))
        self.tableView_2.setObjectName("tableView_2")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(10, 70, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(460, 70, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.afficher = QtWidgets.QPushButton(self.tab_3)
        self.afficher.setGeometry(QtCore.QRect(460, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.afficher.setFont(font)
        self.afficher.setObjectName("afficher")
        self.Choix = QtWidgets.QComboBox(self.tab_3)
        self.Choix.setGeometry(QtCore.QRect(610, 20, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Choix.setFont(font)
        self.Choix.setObjectName("Choix")
        self.Choix.addItem("")
        self.Choix.addItem("")
        self.indexer_3 = QtWidgets.QPushButton(self.tab_3)
        self.indexer_3.setGeometry(QtCore.QRect(900, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.indexer_3.setFont(font)
        self.indexer_3.setObjectName("indexer_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.calcul_RP = QtWidgets.QPushButton(self.tab_4)
        self.calcul_RP.setGeometry(QtCore.QRect(20, 50, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.calcul_RP.setFont(font)
        self.calcul_RP.setObjectName("calcul_RP")
        self.label_courbe = QtWidgets.QLabel(self.tab_4)
        self.label_courbe.setGeometry(QtCore.QRect(20, 100, 351, 321))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_courbe.setFont(font)
        self.label_courbe.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_courbe.setText("")
        self.label_courbe.setScaledContents(True)
        self.label_courbe.setAlignment(QtCore.Qt.AlignCenter)
        self.label_courbe.setObjectName("label_courbe")
        self.Quitter = QtWidgets.QPushButton(self.tab_4)
        self.Quitter.setGeometry(QtCore.QRect(480, 340, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Quitter.setFont(font)
        self.Quitter.setObjectName("Quitter")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(380, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(380, 50, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.top_50_result_r = QtWidgets.QLabel(self.tab_4)
        self.top_50_result_r.setGeometry(QtCore.QRect(380, 110, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.top_50_result_r.setFont(font)
        self.top_50_result_r.setFrameShape(QtWidgets.QFrame.Panel)
        self.top_50_result_r.setText("")
        self.top_50_result_r.setAlignment(QtCore.Qt.AlignCenter)
        self.top_50_result_r.setObjectName("top_50_result_r")
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(380, 180, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.top_100_result_r = QtWidgets.QLabel(self.tab_4)
        self.top_100_result_r.setGeometry(QtCore.QRect(380, 240, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.top_100_result_r.setFont(font)
        self.top_100_result_r.setFrameShape(QtWidgets.QFrame.Panel)
        self.top_100_result_r.setText("")
        self.top_100_result_r.setAlignment(QtCore.Qt.AlignCenter)
        self.top_100_result_r.setObjectName("top_100_result_r")
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setGeometry(QtCore.QRect(560, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.top_50_result_p = QtWidgets.QLabel(self.tab_4)
        self.top_50_result_p.setGeometry(QtCore.QRect(560, 110, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.top_50_result_p.setFont(font)
        self.top_50_result_p.setFrameShape(QtWidgets.QFrame.Panel)
        self.top_50_result_p.setText("")
        self.top_50_result_p.setAlignment(QtCore.Qt.AlignCenter)
        self.top_50_result_p.setObjectName("top_50_result_p")
        self.top_100_result_p = QtWidgets.QLabel(self.tab_4)
        self.top_100_result_p.setGeometry(QtCore.QRect(560, 240, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.top_100_result_p.setFont(font)
        self.top_100_result_p.setFrameShape(QtWidgets.QFrame.Panel)
        self.top_100_result_p.setText("")
        self.top_100_result_p.setAlignment(QtCore.Qt.AlignCenter)
        self.top_100_result_p.setObjectName("top_100_result_p")
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        self.label_18.setGeometry(QtCore.QRect(740, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.top_50_result_ap = QtWidgets.QLabel(self.tab_4)
        self.top_50_result_ap.setGeometry(QtCore.QRect(740, 110, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.top_50_result_ap.setFont(font)
        self.top_50_result_ap.setFrameShape(QtWidgets.QFrame.Panel)
        self.top_50_result_ap.setText("")
        self.top_50_result_ap.setAlignment(QtCore.Qt.AlignCenter)
        self.top_50_result_ap.setObjectName("top_50_result_ap")
        self.top_100_result_ap = QtWidgets.QLabel(self.tab_4)
        self.top_100_result_ap.setGeometry(QtCore.QRect(740, 240, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.top_100_result_ap.setFont(font)
        self.top_100_result_ap.setFrameShape(QtWidgets.QFrame.Panel)
        self.top_100_result_ap.setText("")
        self.top_100_result_ap.setAlignment(QtCore.Qt.AlignCenter)
        self.top_100_result_ap.setObjectName("top_100_result_ap")
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(920, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.tmax_label = QtWidgets.QLabel(self.tab_4)
        self.tmax_label.setGeometry(QtCore.QRect(920, 50, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tmax_label.setFont(font)
        self.tmax_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.tmax_label.setText("")
        self.tmax_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tmax_label.setObjectName("tmax_label")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1234, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.charger_2.clicked.connect(self.Ouvrir_2)  # lier le bouton Charger à la fonction Ouvrir
        self.charger_desc.clicked.connect(self.loadFeatures)
        self.chercher.clicked.connect(self.Recherche)
        self.calcul_RP.clicked.connect(self.rappel_precision)
        self.charger.clicked.connect(self.Ouvrir)  # lier le bouton Charger à la fonction Ouvrir
        self.tableView.clicked.connect(self.cliquerTab)
        self.indexer.clicked.connect(self.extractFeatures)
        self.Quitter.clicked.connect(self.Close)
        self.Quitter.clicked.connect(self.Close)
        self.indexer_3.clicked.connect(self.Close)
        self.indexer_2.clicked.connect(self.Close)
        self.afficher.clicked.connect(self.Fonction_Afficher)
        self.tableView_2.clicked.connect(self.cliquerTab_2)

    # Fonctions tab Indexation
    def Close(self):
        QApplication.quit()

    def Ouvrir(self, MainWindow):
        self.list_images = []
        # Sélectionner le dossier Wang
        self.Dossier_images = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select directory', "C://", QtWidgets.QFileDialog.ShowDirsOnly)+"/"
        for i in range(len(os.listdir(self.Dossier_images))):
            self.filenames = self.Dossier_images + str(os.listdir(self.Dossier_images)[i])
            self.list_images.append(self.filenames)
        # Afficher la première image
        pixmap = QtGui.QPixmap(self.list_images[0])
        pixmap = pixmap.scaled(self.image.width(), self.image.height(), QtCore.Qt.KeepAspectRatio)
        self.image.setPixmap(pixmap)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        model = QStandardItemModel()
        headerNames = []
        headerNames.append("File name")
        model.setHorizontalHeaderLabels(headerNames)
        pas = 0
        # Afficher la liste d'images dans le tableView
        for i in range(len(self.list_images)):
            row = []
            first = self.list_images[i]  # chemin complet
            second = os.path.basename(self.list_images[i])  # juste le nom du fichier
            item = QStandardItem(first)
            item.setEditable(False)
            row.append(item)
            model.setColumnCount(1)
            model.appendRow(row)
            pas += 1
            self.progressBar.setValue(int(100 * ((pas+1) / len(self.list_images))))
        self.tableView.setModel(model)

    def cliquerTab(self, MainWindow):
        index = self.tableView.selectionModel().currentIndex()
        UrlImg = index.sibling(index.row(), index.column()).data()
        pixmap = QtGui.QPixmap(UrlImg)
        pixmap = pixmap.scaled(self.image.width(), self.image.height(),QtCore.Qt.KeepAspectRatio)
        self.image.setPixmap(pixmap)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        
    def extractFeatures(self, MainWindow):
        
		# Appel de la fonction de calcul de l'histogramme de couleur BGR
        if self.Dossier_images and self.checkBox_HistC.isChecked():
            temps_debut = time.time()
            generateHistogramme_Color(self.Dossier_images, self.progressBar)
            # Calculer le temps écoulé
            temps_ecoule = time.time() - temps_debut

            # Afficher le temps écoulé dans le terminal
            print("Temps d'exécution Histogramme BGR : {:.2f} secondes".format(temps_ecoule))

        
		# Appel de la fonction de calcul de l'histogramme de couleur HSV
        if self.Dossier_images and self.checkBox_HSV.isChecked():
            temps_debut = time.time()
            generateHistogramme_HSV(self.Dossier_images, self.progressBar)
            # Calculer le temps écoulé
            temps_ecoule = time.time() - temps_debut

            # Afficher le temps écoulé dans le terminal
            print("Temps d'exécution Histogramme HSV : {:.2f} secondes".format(temps_ecoule))
		
		# Appel de la fonction de calcul du descripteur SIFT
        if self.Dossier_images and self.checkBox_SIFT.isChecked():
            temps_debut = time.time()
            generateSIFT(self.Dossier_images, self.progressBar)
            # Calculer le temps écoulé
            temps_ecoule = time.time() - temps_debut

            # Afficher le temps écoulé dans le terminal
            print("Temps d'exécution SIFT : {:.2f} secondes".format(temps_ecoule))

		# Appel de la fonction de calcul du descripteur ORB
        if self.Dossier_images and self.checkBox_ORB.isChecked():
            temps_debut = time.time()
            generateORB(self.Dossier_images, self.progressBar)
            # Calculer le temps écoulé
            temps_ecoule = time.time() - temps_debut

            # Afficher le temps écoulé dans le terminal
            print("Temps d'exécution ORB : {:.2f} secondes".format(temps_ecoule))

        # Appel de la fonction de calcul du descripteur LBP
        if self.Dossier_images and self.checkBox_LBP.isChecked():
            temps_debut = time.time()
            generateLBP(self.Dossier_images, self.progressBar)
            # Calculer le temps écoulé
            temps_ecoule = time.time() - temps_debut

            # Afficher le temps écoulé dans le terminal
            print("Temps d'exécution LBP : {:.2f} secondes".format(temps_ecoule))
            
        if self.Dossier_images and self.checkBox_HOG.isChecked():
            temps_debut = time.time()
            generateHOG(self.Dossier_images, self.progressBar)
            # Calculer le temps écoulé
            temps_ecoule = time.time() - temps_debut

            # Afficher le temps écoulé dans le terminal
            print("Temps d'exécution HOG : {:.2f} secondes".format(temps_ecoule))

        if self.Dossier_images and self.checkBox_GLCM.isChecked():
            temps_debut = time.time()
            generateGLCM(self.Dossier_images, self.progressBar)
            # Calculer le temps écoulé
            temps_ecoule = time.time() - temps_debut

            # Afficher le temps écoulé dans le terminal
            print("Temps d'exécution GLCM : {:.2f} secondes".format(temps_ecoule))

        
        if not self.checkBox_SIFT.isChecked() and not self.checkBox_HistC.isChecked() and not self.checkBox_HSV.isChecked() and not self.checkBox_ORB.isChecked() and not self.checkBox_LBP.isChecked() and not self.checkBox_HOG.isChecked() and not self.checkBox_GLCM.isChecked():
            print("Merci de selectionner un descripteur via le Menu  ...")
            showDialog()

        if len(self.Dossier_images)<1:
            print("Merci de charger la base de données avec le bouton Ouvrir")

    # Fonctions tab Recherche
    def Ouvrir_2(self, MainWindow):
        global fileName
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "","Image Files (*.png *.jpeg *.jpg *.bmp)")
        pixmap = QtGui.QPixmap(fileName)
        pixmap = pixmap.scaled(self.label_requete.width(),self.label_requete.height(), QtCore.Qt.KeepAspectRatio)
        self.label_requete.setPixmap(pixmap)
        self.label_requete.setAlignment(QtCore.Qt.AlignCenter)

    def loadFeatures(self, MainWindow):
        folder_model = []
        self.algo_choice = []
        if self.checkBox_HistC_2.isChecked():
            folder_model.append('./BGR')
            self.algo_choice.append(1)
        if self.checkBox_HSV_2.isChecked():
            folder_model.append('./HSV')
            self.algo_choice.append(2)
        if self.checkBox_SIFT_2.isChecked():
            folder_model.append('./SIFT')
            self.algo_choice.append(3)
        if self.checkBox_ORB_2.isChecked():
            folder_model.append('./ORB')
            self.algo_choice.append(4)
        if self.checkBox_LBP_2.isChecked():
            folder_model.append('./LBP')
            self.algo_choice.append(5)
        if self.checkBox_HOG_2.isChecked():
            folder_model.append('./HOG')
            self.algo_choice.append(6)
        if self.checkBox_GLCM_2.isChecked():
            folder_model.append('./GLCM')
            self.algo_choice.append(7)
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)
        if (self.checkBox_ORB_2.isChecked() or self.checkBox_SIFT_2.isChecked()) and (
                self.checkBox_GLCM_2.isChecked() or self.checkBox_HistC_2.isChecked() or self.checkBox_HSV_2.isChecked() or self.checkBox_LBP_2.isChecked() or self.checkBox_HOG_2.isChecked()):
            print("Vous ne pouvez pas combiner ORB ou SIFT avec d'autres descripteurs ")
            showDialog()
        if filenames:
            if 3 in self.algo_choice or 4 in self.algo_choice:
                self.comboBox.clear()
                self.comboBox.addItems(["Brute force", "Flann"])
            else:
                self.comboBox.clear()
                self.comboBox.addItems(["Euclidienne", "Correlation", "Chicarre","Intersection","Bhattacharyya"])
        if len(filenames) < 1:
            print("Merci de charger une image avec le bouton Ouvrir")
        # Charger les features de la base de données.
        self.features1 = []
        pas = 0
        print("chargement de descripteurs en cours ...")
        if len(folder_model) > 0:
            folder=folder_model[0]
            for j in os.listdir(folder):  # folder_model : dossier de features
                data = os.path.join(folder, j)
                if not data.endswith(".txt"):
                    continue
                feature1 = np.loadtxt(data)

                if self.algo_choice[0] == 1 or self.algo_choice[0] == 2:
                    feature1 = feature1.ravel()
                feature = feature1
                for index, folder2 in enumerate(folder_model):
                    if index > 0:
                        data2 = os.path.join(folder2, j)
                        if not data2.endswith(".txt"):
                            continue
                        feature2 = np.loadtxt(data2)
                        if self.algo_choice[0] == 1 or self.algo_choice[0] == 2:
                            feature2 = feature2.ravel()
                        feature=np.concatenate([feature,feature2])

                self.features1.append((os.path.join(filenames, os.path.basename(data).split('.')[0] + '.jpg'),feature))
                pas += 1
                self.progressBar_2.setValue(int(100 * ((pas+1) / 10000)))
        if not self.checkBox_SIFT_2.isChecked() and not self.checkBox_HistC_2.isChecked() and not self.checkBox_HSV_2.isChecked() and not self.checkBox_ORB_2.isChecked() and not self.checkBox_LBP_2.isChecked() and not self.checkBox_HOG_2.isChecked() and not self.checkBox_GLCM_2.isChecked():
            print("Merci de sélectionner au moins un descripteur dans le menu")
            showDialog()



    def Recherche(self, MainWindow):
        # Remise à 0 de la grille des voisins
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)
        voisins = ""
        if len(self.algo_choice) != 0:
            temps_debut = time.time()
            ##Generer les features de l'images requete
            req = extractReqFeatures(fileName, self.algo_choice)
            ##Definition du nombre de voisins
            self.sortie = 3
            # Aller chercher dans la liste de l'interface la distance choisie
            distanceName = self.comboBox.currentText()
            # Générer les voisins
            voisins = getkVoisins(self.features1, req, self.sortie, distanceName)
            self.path_image_plus_proches = []
            self.nom_image_plus_proches = []
            for k in range(self.sortie):
                self.path_image_plus_proches.append(voisins[k][0])
                self.nom_image_plus_proches.append(os.path.basename(voisins[k][0]))
            # Nombre de colonnes pour l'affichage
            col = 3
            k = 0
            for i in range(math.ceil(self.sortie / col)):
                for j in range(col):
                    if k < 9:
                        img = cv2.imread(self.path_image_plus_proches[k], 1)  # load image
                        # Remise de l'image en RGB pour l'afficher correctement
                        b,g,r = cv2.split(img)  # get b,g,r
                        img = cv2.merge([r, g, b])  # switch it to rgb
                        # convert image to QImage
                        height, width, channel = img.shape
                        bytesPerLine = 3 * width
                        qImg = QtGui.QImage(img.data, width, height, bytesPerLine,QtGui.QImage.Format_RGB888)
                        pixmap = QtGui.QPixmap.fromImage(qImg)
                        label = QtWidgets.QLabel("")
                        label.setAlignment(QtCore.Qt.AlignCenter)
                        label.setPixmap(pixmap.scaled(0.3 * width, 0.3 * height,QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
                        self.gridLayout.addWidget(label, i, j)
                        k += 1
            temps_ecoule = time.time() - temps_debut
            print("Temps d'exécution recherche : {:.2f} secondes".format(temps_ecoule))
        else:
            print("Il faut choisir une méthode !")

    def rappel_precision(self):
        rappel_precision = []
        rappels = []
        precisions = []
        filename_req = os.path.basename(fileName)
        num_image= filename_req.split('_')[0]
        classe_image_requete = int(num_image)
        val = 0

        # Calculer rappels et prec top 50 et 100
        for j in range(self.sortie):
            classe_image_proche = int(self.nom_image_plus_proches[j].split('_')[0])
            classe_image_requete = int(classe_image_requete)
            classe_image_proche = int(classe_image_proche)
            if classe_image_requete == classe_image_proche:
                rappel_precision.append(True)  # Bonne classe (pertinant)
                val += 1
            else:
                rappel_precision.append(False)  # Mauvaise classe (non pertinant)
        for i in range(self.sortie):
            j = i
            val = 0
            while (j >= 0):
                if rappel_precision[j]:
                    val += 1
                j -= 1
            precision = val / (i+1)
            rappel =  val/self.sortie # attention pour lisibilité diviser par 9 mais normalement c'est divisé par 100 le nombre total d'images
            rappels.append(rappel)
            precisions.append(precision)
            if i == 49:
                self.top_50_result_p.setText(str(precision))
                self.top_50_result_r.setText(str(rappel))
                self.top_50_result_ap.setText(str("{:.2f}".format(np.mean(precisions))))
            if i == 99:
                self.top_100_result_p.setText(str(precision))
                self.top_100_result_r.setText(str(rappel))
                self.top_100_result_ap.setText(str("{:.2f}".format(np.mean(precisions))))
        # Création de la courbe R/P
        plt.plot(rappels, precisions)
        plt.xlabel("Recall")
        plt.ylabel("Precision")
        plt.title("R/P voisins de l'image n°" + num_image)

        # Enregistrement de la courbe RP
        save_folder = os.path.join(".", num_image)
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        save_name = os.path.join(save_folder, num_image + '.png')
        plt.savefig(save_name, format='png', dpi=600)
        plt.close()

        # Affichage de la courbe R/P
        img = cv2.imread(save_name, 1)  # load image in color

        # Remise de l'image en RGB pour l'afficher correctement
        b, g, r = cv2.split(img)  # get b,g,r
        img = cv2.merge([r, g, b])  # switch it to rgb

        # convert image to QImage
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(img.data, width, height, bytesPerLine,QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qImg)
        width = self.label_requete.frameGeometry().width()
        height = self.label_requete.frameGeometry().height()
        self.label_courbe.setAlignment(QtCore.Qt.AlignCenter)
        self.label_courbe.setPixmap(pixmap.scaled(width, height,QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    # Fonctions Tab top liste

    def Fonction_Afficher(self, MainWindow):

        # Afficher la première image
        pixmap = QtGui.QPixmap(self.path_image_plus_proches[0])
        pixmap = pixmap.scaled(self.image_2.width(), self.image_2.height(), QtCore.Qt.KeepAspectRatio)
        self.image_2.setPixmap(pixmap)
        self.image_2.setAlignment(QtCore.Qt.AlignCenter)
        model = QStandardItemModel()
        headerNames = []
        headerNames.append("File name")
        model.setHorizontalHeaderLabels(headerNames)
        if self.Choix.currentIndex() == 0:
            l = 20
        elif self.Choix.currentIndex() == 1:
            l = 50
        # Afficher la liste d'images dans le tableView
        for i in range(l):
            row = []
            first = self.path_image_plus_proches[i]  # chemin complet
            second = self.nom_image_plus_proches[i]  # juste le nom du fichier
            item = QStandardItem(first)
            item.setEditable(False)
            row.append(item)
            model.setColumnCount(1)
            model.appendRow(row)
        self.tableView_2.setModel(model)

    def cliquerTab_2(self, MainWindow):

        index = self.tableView_2.selectionModel().currentIndex()
        UrlImg = index.sibling(index.row(), index.column()).data()
        pixmap = QtGui.QPixmap(UrlImg)
        pixmap = pixmap.scaled(self.image_2.width(), self.image_2.height(),QtCore.Qt.KeepAspectRatio)
        self.image_2.setPixmap(pixmap)
        self.image_2.setAlignment(QtCore.Qt.AlignCenter)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_SIFT.setText(_translate("MainWindow", "SIFT"))
        self.checkBox_ORB.setText(_translate("MainWindow", "ORB"))
        self.checkBox_HistC.setText(_translate("MainWindow", "Hist Couleur"))
        self.checkBox_HSV.setText(_translate("MainWindow", "Hist HSV"))
        self.checkBox_GLCM.setText(_translate("MainWindow", "GLCM"))
        self.checkBox_LBP.setText(_translate("MainWindow", "LBP"))
        self.checkBox_HOG.setText(_translate("MainWindow", "HOG"))
        self.charger.setText(_translate("MainWindow", "Charger et afficher la base de données"))
        self.indexer.setText(_translate("MainWindow", "Calculer les descripteurs"))
        self.indexer_2.setText(_translate("MainWindow", "Quitter"))
        self.label_3.setText(_translate("MainWindow", "Base d\'images"))
        self.label.setText(_translate("MainWindow", "Image"))
        self.label_2.setText(_translate("MainWindow", "Descripteurs :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Indexation"))
        self.checkBox_GLCM_2.setText(_translate("MainWindow", "GLCM"))
        self.label_4.setText(_translate("MainWindow", "Image requête"))
        self.checkBox_LBP_2.setText(_translate("MainWindow", "LBP"))
        self.checkBox_HistC_2.setText(_translate("MainWindow", "BGR"))
        self.chercher.setText(_translate("MainWindow", "Recherche"))
        self.label_6.setText(_translate("MainWindow", "Requête"))
        self.label_8.setText(_translate("MainWindow", "Résultats"))
        self.charger_2.setText(_translate("MainWindow", "Charger"))
        self.checkBox_HOG_2.setText(_translate("MainWindow", "HOG"))
        self.checkBox_SIFT_2.setText(_translate("MainWindow", "SIFT"))
        self.checkBox_HSV_2.setText(_translate("MainWindow", "HSV"))
        self.charger_desc.setText(_translate("MainWindow", "Charger descripteurs"))
        self.checkBox_ORB_2.setText(_translate("MainWindow", "ORB"))
        self.label_7.setText(_translate("MainWindow", "Choix de descripteur"))
        self.label_10.setText(_translate("MainWindow", "Recherche"))
        self.label_11.setText(_translate("MainWindow", "Distance :"))
        self.Quitter_2.setText(_translate("MainWindow", "Quitter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Recherche"))
        self.label_12.setText(_translate("MainWindow", "Image"))
        self.label_13.setText(_translate("MainWindow", "Top liste"))
        self.afficher.setText(_translate("MainWindow", "Afficher"))
        self.Choix.setItemText(0, _translate("MainWindow", "Top 20"))
        self.Choix.setItemText(1, _translate("MainWindow", "Top 50"))
        self.indexer_3.setText(_translate("MainWindow", "Quitter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Top liste"))
        self.calcul_RP.setText(_translate("MainWindow", "Calculer la courbe R/P"))
        self.Quitter.setText(_translate("MainWindow", "Quitter"))
        self.label_5.setText(_translate("MainWindow", "Rappel/Précision"))
        self.label_9.setText(_translate("MainWindow", "Rappel"))
        self.label_14.setText(_translate("MainWindow", "Top 50"))
        self.label_16.setText(_translate("MainWindow", "Top 100"))
        self.label_17.setText(_translate("MainWindow", "Précision"))
        self.label_18.setText(_translate("MainWindow", "Average Precision"))
        self.label_19.setText(_translate("MainWindow", "Tmax"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Résultats"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
