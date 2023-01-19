

# calculer les scores suivant pour chaque cnn binaires
    # ACC
    # F1
    # MCC

#IMPORTS
import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, fbeta_score, matthews_corrcoef




def scores(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    mcc = matthews_corrcoef(y_true, y_pred)
    return round(acc,3), round(f1,3), round(mcc,3)


# on predit quoi ? pour les index 0 et 1, a verifier le classement des class folders dans la database d'entrainement
class_name = {'PROG':0, 'REP':1}


# le path ou est stocker nos matrice de prediction
root = '/work/shared/ptbc/CNN_Pancreas_V2/cnn_models/model8/Evaluation/'

# normalement on en a 3 matrices correspodant au TRAIN, VAL ET TEST
print(os.listdir(root))



# load dataframe
df = pd.read_csv(f'{root}myPrediction_test.csv').T.reset_index().T

# renomer les colonnes
df.rename(columns={0:'tiles',
                  1:'PROG',
                  2:'REP'},
         inplace=True)

print(df.head())

# extraire les vrai class
df['True'] = [i.split('/')[0] for i in df['tiles']]
df['tiles'] = [i.split('/')[1] for i in df['tiles']]

# recuperer l'index de chaque class
df['True']=[class_name[i] for i in df['True']]

# extraire la classe predite en comparant les proba des deux classes
df['Pred'] = ['PROG' if float(i)>float(j) else 'REP' for i, j in zip(df['PROG'],df['REP'])]

# get l'index de chaque classe predite
df['Pred']=[class_name[i] for i in df['Pred']]

# into array
y_true = df['True'].values
y_pred = df['Pred'].values


# apply our scores function
acc, f1, mcc = scores(y_true, y_pred)


# afficher les resultat dans un format comprehensible
f_string = f'RESULTS : \n - Accuracy = {acc}\n - F1_score = {f1}\n - Matt corr coef = {mcc}'
print(f_string)


print('DONE')
