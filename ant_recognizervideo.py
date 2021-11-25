import cv2
import numpy as np
import time

#haar_cascade=cv2.CascadeClassifier('antdetector.xml')                       # utiliser le classifieur de visage
haar_cascade=cv2.CascadeClassifier('antdetectorfinal.xml')                       # utiliser le classifieur de visage

#haar_cascade=cv2.CascadeClassifier('cascade.xml')                       # utiliser le classifieur de visage

#cap =cv2.VideoCapture(0)
cap=cv2.VideoCapture('videofourmis2.mp4')
#cap=cv2.VideoCapture('videofourmis.mp4')

while(True):
    ret ,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    #photo en noir et blanc 
    faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.04,minNeighbors=15,minSize=(70,70))   # detecter les visages présent sur l'images  
    for(x,y,w,h) in faces_rect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),thickness=4)         #faire un rectangle sur chaque visage détecté
    cv2.imshow('Detected face',frame)
    #key=cv2.waitKey(30)&0xFF
    #cv2.waitKey(1)#si on met rien en paramètre il va attendre quon tape sur le clavier 
    #if key==ord('q'):
        #break
    
    key=cv2.waitKey(1)
    if key == ord('q'):
      break
#     while key not in [ord('q'),ord('k'),ord('a'),ord('d')]:
#         key = cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
 


 
 