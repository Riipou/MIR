#Defintion de toute les fonctions à appeller dans l'interface
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import os
import cv2
import numpy as np
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
from skimage import io, color, img_as_ubyte
from matplotlib import pyplot as plt
from skimage.feature import hog, greycomatrix, greycoprops, local_binary_pattern
from skimage.color import rgb2gray
def showDialog():
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Merci de sélectionner un descripteur via le menu ci-dessus")
    msgBox.setWindowTitle("Pas de Descripteur sélectionné")
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    returnValue = msgBox.exec()

def generateHistogramme_HSV(filenames, progressBar):
    if not os.path.isdir("HSV"):
        os.mkdir("HSV")
    i=0
    for path in os.listdir(filenames):
        img = cv2.imread(filenames+"/"+path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        histH = cv2.calcHist([img],[0],None,[180],[0,180])
        histS = cv2.calcHist([img],[1],None,[256],[0,256])
        histV = cv2.calcHist([img],[2],None,[256],[0,256])
        feature = np.concatenate((histH, np.concatenate((histS,histV),axis=None)),axis=None)

        num_image, _ = path.split(".")
        np.savetxt("HSV/"+str(num_image)+".txt" ,feature)
        
        progressBar.setValue(100*((i+1)/len(os.listdir(filenames))))
        i+=1
    print("indexation Hist HSV terminée !!!!")
        
def generateHistogramme_Color(filenames, progressBar):
    if not os.path.isdir("BGR"):
        os.mkdir("BGR")
    i=0
    for path in os.listdir(filenames):
        img = cv2.imread(filenames+"/"+path)
        histB = cv2.calcHist([img],[0],None,[256],[0,256])
        histG = cv2.calcHist([img],[1],None,[256],[0,256])
        histR = cv2.calcHist([img],[2],None,[256],[0,256])
        feature = np.concatenate((histB, np.concatenate((histG,histR),axis=None)),axis=None)

        num_image, _ = path.split(".")
        np.savetxt("BGR/"+str(num_image)+".txt" ,feature)
        progressBar.setValue(100*((i+1)/len(os.listdir(filenames))))
        i+=1
    print("indexation Hist Couleur terminée !!!!")

def generateSIFT(filenames, progressBar):
    if not os.path.isdir("SIFT"):
        os.mkdir("SIFT")
    i=0
    target_size = (600, 400)
    for path in os.listdir(filenames):
        img = cv2.imread(filenames+"/"+path)
        if img.shape[0] != target_size[0] or img.shape[1] != target_size[1] :
            img=resize(img, target_size)
        featureSum = 0
        sift = cv2.SIFT_create()  
        kps , des = sift.detectAndCompute(img,None)

        num_image, _ = path.split(".")
        np.savetxt("SIFT/"+str(num_image)+".txt" ,des)
        progressBar.setValue(100*((i+1)/len(os.listdir(filenames))))
        
        featureSum += len(kps)
        i+=1
    print("Indexation SIFT terminée !!!!")    


def generateORB(filenames, progressBar):
    if not os.path.isdir("ORB"):
        os.mkdir("ORB")
    i=0
    target_size = (600, 400)
    for path in os.listdir(filenames):
        img = cv2.imread(filenames+"/"+path)
        if img.shape[0] != target_size[0] or img.shape[1] != target_size[1] :
            img=resize(img, target_size)
        orb = cv2.ORB_create()
        key_point1,descrip1 = orb.detectAndCompute(img,None)
        
        num_image, _ = path.split(".")
        np.savetxt("ORB/"+str(num_image)+".txt" ,descrip1 )
        progressBar.setValue(100*((i+1)/len(os.listdir(filenames))))
        i+=1
    print("indexation ORB terminée !!!!")

def lbpDescriptor(image):                 # function : return LBP Image
# settings for LBP
  METHOD = 'uniform'
  radius = 3
  n_points = 8 * radius
  gray = rgb2gray(image)
  lbp = local_binary_pattern(gray, n_points, radius, METHOD)
  return lbp

def generateLBP(filenames, progressBar):
    target_size = (600, 400)
    if not os.path.isdir("LBP"):
        os.mkdir("LBP")
    i = 0
    for path in os.listdir(filenames):
        img = cv2.imread(filenames + "/" + path)
        if img.shape[0] != target_size[0] or img.shape[1] != target_size[1] :
            img=resize(img, target_size)
        des = lbpDescriptor(img)
        lbp_features = des.flatten()
        descrip1 = np.array(lbp_features)
        num_image, _ = path.split(".")
        np.savetxt("LBP/" + str(num_image) + ".txt", descrip1)
        progressBar.setValue(100 * ((i + 1) / len(os.listdir(filenames))))
        i += 1
    print("indexation LBP terminée !!!!")

def generateHOG(filenames, progressBar):
    target_size = (600, 400)
    if not os.path.isdir("HOG"):
        os.mkdir("HOG")
    i = 0
    for path in os.listdir(filenames):
        img = cv2.imread(filenames + "/" + path)
        if img.shape[0] != target_size[0] or img.shape[1] != target_size[1] :
            img=resize(img, target_size)
        descrip1, hog_image = hog(img, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2),visualize=True, multichannel=True)
        num_image, _ = path.split(".")
        np.savetxt("HOG/" + str(num_image) + ".txt", descrip1)
        progressBar.setValue(100 * ((i + 1) / len(os.listdir(filenames))))
        i += 1
    print("indexation HOG terminée !!!!")

def generateGLCM(filenames, progressBar):
    target_size = (600, 400)
    if not os.path.isdir("GLCM"):
        os.mkdir("GLCM")
    i = 0
    for path in os.listdir(filenames):
        img = cv2.imread(filenames + "/" + path)
        if img.shape[0] != target_size[0] or img.shape[1] != target_size[1] :
            img=resize(img, target_size)
        if img.dtype == np.float64:
            img = (img * 255).astype(np.uint8)
        image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        glcm = greycomatrix(image, distances=[1], angles= [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4], symmetric = True, normed = True)
        descrip1 = glcm.flatten()
        num_image, _ = path.split(".")
        np.savetxt("GLCM/" + str(num_image) + ".txt", descrip1)
        progressBar.setValue(100 * ((i + 1) / len(os.listdir(filenames))))
        i += 1
    print("indexation GLCM terminée !!!!")
	
def extractReqFeatures(fileName,algo_choice):
    target_size=(600,400)
    print(algo_choice)
    if fileName : 
        img = cv2.imread(fileName)


        if algo_choice==1: #Couleurs
            histB = cv2.calcHist([img],[0],None,[256],[0,256])
            histG = cv2.calcHist([img],[1],None,[256],[0,256])
            histR = cv2.calcHist([img],[2],None,[256],[0,256])
            vect_features = np.concatenate((histB, np.concatenate((histG,histR),axis=None)),axis=None)
        
        elif algo_choice==2: # Histo HSV
            hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
            histH = cv2.calcHist([hsv],[0],None,[180],[0,180])
            histS = cv2.calcHist([hsv],[1],None,[256],[0,256])
            histV = cv2.calcHist([hsv],[2],None,[256],[0,256])
            vect_features = np.concatenate((histH, np.concatenate((histS,histV),axis=None)),axis=None)

        elif algo_choice==3: #SIFT
            sift = cv2.SIFT_create() #cv2.xfeatures2d.SIFT_create() pour py < 3.4 
            # Find the key point
            kps , vect_features = sift.detectAndCompute(img,None)
    
        elif algo_choice==4: #ORB
            orb = cv2.ORB_create()
            # finding key points and descriptors of both images using detectAndCompute() function
            key_point1,vect_features = orb.detectAndCompute(img,None)

        elif algo_choice==5: #LBP
            if img.shape[0] != target_size[0] or img.shape[1] != target_size[1]:
                img = resize(img, target_size)
            des = lbpDescriptor(img)
            lbp_features = des.flatten()
            vect_features = np.array(lbp_features)
            print(vect_features)
        elif algo_choice==6 : #HOG
            if img.shape[0] != target_size[0] or img.shape[1] != target_size[1]:
                img = resize(img, target_size)
            # Calculer le descripteur HOG et obtenir l'image HOG
            vect_features, hog_image = hog(img, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True, multichannel=True)
        elif algo_choice==7 : #GLCM
            if img.shape[0] != target_size[0] or img.shape[1] != target_size[1]:
                img = resize(img, target_size)
            # Calculer le descripteur GLCM et
            if img.dtype == np.float64:
                img = (img * 255).astype(np.uint8)
            image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            glcm = greycomatrix(image, distances=[1], angles=[0, np.pi / 4, np.pi / 2, 3 * np.pi / 4], symmetric=True, normed=True)
            vect_features=glcm.flatten()
        np.savetxt("Methode_"+str(algo_choice)+"_requete.txt" ,vect_features)
        print("saved")
        #print("vect_features", vect_features)
        return vect_features