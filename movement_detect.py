#import os
#import sys
#import time
import numpy as np
import cv2


#cap=cv2.VideoCapture(0)

cap=cv2.VideoCapture('29-06-2021-vrai7fps.avi')
kernel_blur=5
seuil=25

ret, originale=cap.read()                 #on retient la premiere image de la video 
originale=cv2.cvtColor(originale, cv2.COLOR_BGR2GRAY)                 #convertit la video en noir et blanc
originale=cv2.GaussianBlur(originale, (kernel_blur, kernel_blur), 0)
kernel_dilate=np.ones((5, 5), np.uint8)
while True:
    #cv2.waitKey(150)
    ret, frame=cap.read()
    frame_contour=frame.copy()
    frame_contour1=frame.copy()
    extract_video= frame_contour[0:675,0:750]                   #on prend que la partie de la vidéo où il y a les pièges de fourmilion.
    gray=cv2.cvtColor(frame_contour, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray, (kernel_blur, kernel_blur), 0)
    mask=cv2.absdiff(originale, gray)
    mask=cv2.threshold(mask, seuil, 255, cv2.THRESH_BINARY)[1]
    mask=cv2.dilate(mask, kernel_dilate, iterations=3)
    contours, nada=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        cv2.drawContours(extract_video, [c], 0, (0, 255, 0), 3)
        cv2.drawContours(frame_contour1, [c], 0, (0, 255, 0), 3)
    originale=gray
    
    
    cv2.putText(extract_video, "[a|d]seuil: {:d}".format(seuil), (10, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 255), 2)
    cv2.imshow("zone analyse", extract_video)
    cv2.imshow("Traitement partiel", frame_contour)
    cv2.imshow("Video traitement entier", frame_contour1)
    cv2.imshow("Video de base ", frame)
    
    
    key=cv2.waitKey(0)
    if key == ord('q'):
        break
    if key==ord('a'):
        seuil=min(255, seuil+1)
    if key==ord('d'):
        seuil=max(1, seuil-1)
    
    while key not in [ord('q'),ord('k'),ord('a'),ord('d')]:
        key = cv2.waitKey(0)
       
    
    
cap.release()
cv2.destroyAllWindows()
