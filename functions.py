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
def showDialog(message, msg_title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(message)
    msgBox.setWindowTitle(msg_title)
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
    i = 0
    for path in os.listdir(filenames):
        img = cv2.imread(filenames+"/"+path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        featureSum = 0
        sift = cv2.SIFT_create()  
        kps , des = sift.detectAndCompute(img,None)

        num_image, _ = path.split(".")
        np.savetxt("SIFT/"+str(num_image)+".txt" ,des)
        progressBar.setValue(100*((i+1)/len(os.listdir(filenames))))
        
        featureSum += len(kps)
        i += 1
    print("Indexation SIFT terminée !!!!")    


def generateORB(filenames, progressBar):
    if not os.path.isdir("ORB"):
        os.mkdir("ORB")
    i=0
    for path in os.listdir(filenames):
        img = cv2.imread(filenames+"/"+path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        orb = cv2.ORB_create()
        key_point1, descrip1 = orb.detectAndCompute(img,None)
        
        num_image, _ = path.split(".")
        np.savetxt("ORB/"+str(num_image)+".txt" ,descrip1 )
        progressBar.setValue(100*((i+1)/len(os.listdir(filenames))))
        i+=1
    print("indexation ORB terminée !!!!")

def lbpDescriptor(image, radius, n_points):                 # function : return LBP Image
    # settings for LBP
    METHOD = 'default'
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image,(350,350))
    lbp = local_binary_pattern(image, n_points, radius, METHOD)
    return lbp

def generateLBP(filenames, progressBar):
    if not os.path.isdir("LBP"):
        os.mkdir("LBP")
    i = 0
    for path in os.listdir(filenames):
        img = cv2.imread(filenames + "/" + path)
        radius = 1
        n_points = 8 * radius
        des = lbpDescriptor(img, radius, n_points)
        subSize=(70,70)
        histograms = []
        for k in range(int(des.shape[0]/subSize[0])):
            for j in range(int(des.shape[1]/subSize[1])):
                subVector = des[k*subSize[0]:(k+1)*subSize[0],j*subSize[1]:(j+1)*subSize[1]].ravel()
                subHist,edges = np.histogram(subVector,bins=int(2**n_points),range=(0,2**n_points))
                histograms = np.concatenate((histograms,subHist),axis=None)
        num_image, _ = path.split(".")
        np.savetxt("LBP/" + str(num_image) + ".txt", histograms)
        progressBar.setValue(100 * ((i + 1) / len(os.listdir(filenames))))
        i += 1
    print("indexation LBP terminée !!!!")

def generateHOG(filenames, progressBar):
    if not os.path.isdir("HOG"):
        os.mkdir("HOG")
    i = 0
    cellSize = (25,25)
    blockSize = (50,50)
    blockStride = (25,25)
    nBins = 9
    winSize = (350,350)
    for path in os.listdir(filenames):
        img = cv2.imread(filenames + "/" + path)
        
        image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image,winSize)
        hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nBins)
        feature = hog.compute(image)
        num_image, _ = path.split(".")
        np.savetxt("HOG/" + str(num_image) + ".txt", feature)
        progressBar.setValue(100 * ((i + 1) / len(os.listdir(filenames))))
        i += 1
    print("indexation HOG terminée !!!!")

def generateGLCM(filenames, progressBar):
    if not os.path.isdir("GLCM"):
        os.mkdir("GLCM")
    
    distances=[1,-1]
    angles=[0, np.pi/4, np.pi/2, 3*np.pi/4]
    i = 0
    for path in os.listdir(filenames):
        image = cv2.imread(filenames+"/"+path)
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        gray = img_as_ubyte(gray)
        glcmMatrix = greycomatrix(gray, distances=distances, angles=angles, normed=True)
        glcmProperties1 = greycoprops(glcmMatrix,'contrast').ravel()
        glcmProperties2 = greycoprops(glcmMatrix,'dissimilarity').ravel()
        glcmProperties3 = greycoprops(glcmMatrix,'homogeneity').ravel()
        glcmProperties4 = greycoprops(glcmMatrix,'energy').ravel()
        glcmProperties5 = greycoprops(glcmMatrix,'correlation').ravel()
        glcmProperties6 = greycoprops(glcmMatrix,'ASM').ravel()
        feature = np.array([glcmProperties1,glcmProperties2,glcmProperties3,glcmProperties4,glcmProperties5,glcmProperties6]).ravel()
        num_image, _ = path.split(".")
        np.savetxt("GLCM/"+str(num_image)+".txt" ,feature)
        progressBar.setValue(100 * ((i + 1) / len(os.listdir(filenames))))
        i += 1
    print("indexation GLCM terminée !!!!")
	
def extractReqFeatures(fileName,algo_choice):
    target_size=(600,400)
    if fileName : 
        img = cv2.imread(fileName)


        if 1 in algo_choice: #Couleurs
            histB = cv2.calcHist([img],[0],None,[256],[0,256])
            histG = cv2.calcHist([img],[1],None,[256],[0,256])
            histR = cv2.calcHist([img],[2],None,[256],[0,256])
            vect_features = np.concatenate((histB, np.concatenate((histG,histR),axis=None)),axis=None)
            vect_features=vect_features.ravel()
            if algo_choice[0]==1 :
                tot_feature=vect_features
            else :
                tot_feature = np.concatenate([tot_feature,vect_features])

        if 2 in algo_choice: # Histo HSV
            hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
            histH = cv2.calcHist([hsv],[0],None,[180],[0,180])
            histS = cv2.calcHist([hsv],[1],None,[256],[0,256])
            histV = cv2.calcHist([hsv],[2],None,[256],[0,256])
            vect_features = np.concatenate((histH, np.concatenate((histS,histV),axis=None)),axis=None)
            vect_features = vect_features.ravel()
            if algo_choice[0] == 2:
                tot_feature = vect_features
            else:
                tot_feature = np.concatenate([tot_feature, vect_features])

        if 3 in algo_choice: #SIFT
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            sift = cv2.SIFT_create()  
            kps , vect_features = sift.detectAndCompute(img,None)
            vect_features = vect_features

            if algo_choice[0] == 3:
                tot_feature = vect_features
        if 4 in algo_choice: #ORB
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            orb = cv2.ORB_create()
            # finding key points and descriptors of both images using detectAndCompute() function
            key_point1,vect_features = orb.detectAndCompute(img,None)
            if algo_choice[0] == 4:
                tot_feature = vect_features
    
        if 5 in algo_choice: #LBP
            radius = 1
            n_points = 8 * radius
            des = lbpDescriptor(img, radius, n_points)
            subSize=(70,70)
            histograms = []
            for k in range(int(des.shape[0]/subSize[0])):
                for j in range(int(des.shape[1]/subSize[1])):
                    subVector = des[k*subSize[0]:(k+1)*subSize[0],j*subSize[1]:(j+1)*subSize[1]].ravel()
                    subHist,edges = np.histogram(subVector,bins=int(2**n_points),range=(0,2**n_points))
                    histograms = np.concatenate((histograms,subHist),axis=None)
            vect_features=histograms
            if algo_choice[0] == 5:
                tot_feature = vect_features
            else:
                tot_feature = np.concatenate([tot_feature, vect_features])
        if 6 in algo_choice : #HOG
            cellSize = (25,25)
            blockSize = (50,50)
            blockStride = (25,25)
            nBins = 9
            winSize = (350,350)
            image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            image = cv2.resize(image,winSize)
            hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nBins)
            vect_features = hog.compute(image)
            if algo_choice[0] == 6:
                tot_feature = vect_features
            else:
                tot_feature = np.concatenate([tot_feature, vect_features])
        if 7 in algo_choice : #GLCM
            distances=[1,-1]
            angles=[0, np.pi/4, np.pi/2, 3*np.pi/4]
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            gray = img_as_ubyte(gray)
            glcmMatrix = greycomatrix(gray, distances=distances, angles=angles, normed=True)
            glcmProperties1 = greycoprops(glcmMatrix,'contrast').ravel()
            glcmProperties2 = greycoprops(glcmMatrix,'dissimilarity').ravel()
            glcmProperties3 = greycoprops(glcmMatrix,'homogeneity').ravel()
            glcmProperties4 = greycoprops(glcmMatrix,'energy').ravel()
            glcmProperties5 = greycoprops(glcmMatrix,'correlation').ravel()
            glcmProperties6 = greycoprops(glcmMatrix,'ASM').ravel()
            vect_features = np.array([glcmProperties1,glcmProperties2,glcmProperties3,glcmProperties4,glcmProperties5,glcmProperties6]).ravel()
            if algo_choice[0] == 7:
                tot_feature = vect_features
            else:
                tot_feature = np.concatenate([tot_feature, vect_features])
        save_folder = os.path.join(".", "requests")
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        save_name = os.path.join(save_folder, "Methode_"+str(algo_choice)+"_request.txt")
        np.savetxt(save_name, tot_feature)
        print("saved")

        return tot_feature