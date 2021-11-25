# StageFourmilion


Observatoire d'une colonie de fourmillons sous la tutelle du Pr.Lorent:

L' objectif de ce stage était d'observer l’activité des insectes autour des pièges de fourmilions.

-Observation des pièges des fourmillions avec une caméra de Raspberry PI par l'intermédiaire de code en Python et Crontab (un outil permettant de configurer des tâches planifiées sur les systèmes Unix).

-Observation des pièges des fourmilions avec Motioneye (logiciel permettant de faire de la surveillance avec la Raspberry PI et envoyer des notifications par mail lorsque la caméra détecte un mouvement).

-Traitement des images obtenues:

--> Stockage des images à l'aide d'un serveur NAS entre la Raspberry PI et mon PC avec Samba.
--> Stacking d'image pour créer une vidéo avec ImageJ.
--> Reconnaissance de mouvement avec OpenCV.

-Reconnaissance d'objet (détection de fourmis) :

-->Entraînement d'un modèle avec le logiciel Cascade Trainer GUI pour obtenir un classifieur HAAR Cascade en format XML.
-->Écriture d'un script python avec la bibliothèque OpenCV pour tracer un rectangle rouge autour de fourmis qu'il détecte dans un flux vidéo.
