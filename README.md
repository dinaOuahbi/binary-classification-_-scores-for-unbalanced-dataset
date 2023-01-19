# binary-classification-_-scores-for-unbalanced-dataset


### description du modéle
Il s'agit d'un réseau de neurones de type CNN qui a été entraîné sur une base de données composée de deux classes :
  - Normal : les images correspondant à la région normale d'une lame
  - Tumor : les images correspondant à la région normale d'une lame
  
l'Objectif était de faire ensuite une annotation avec ce modèle sur la totalité d'une cohorte indépendante, afin d'analysé la survie des patients à l'origine de ces lames.

 
 # Cette étape du projet vise seulement à évaluer notre CNN (de type DenseNet) sur ces données ayant été servi à son entraînement.
 
 
### DATA folder
Comporte les proba de prédiction du modèle sur chaque tranche des données d'entraînement.



### history 
Il s'agit ici de l'évolution de la fonction de perte du modèle ainsi que de sa précision à travers les 10 epochs d'entraînement.

![Image of aciduino on protoboard]()
![Image of aciduino on protoboard]()



PS: le script python prend en entrée le chemin vers le DATA
