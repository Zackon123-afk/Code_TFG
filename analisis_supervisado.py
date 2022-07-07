from tkinter import Y
import pandas as pd
import matplotlib.pyplot as plt
import sys
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

## PREPARACION DE PANDAS

tweet_atributes = pd.read_csv('atributes_etiquetado.csv',engine='python')
tweet_atributes = pd.get_dummies(data=tweet_atributes, drop_first=False)

# original_stdout = sys.stdout
# with open("describe_supervisado.txt","w") as f:
#     sys.stdout = f
#     print(tweet_atributes.describe(include='all'))
#     sys.stdout = original_stdout

#Despues de sacar el describe.txt, eliminamos columnas innecesarias

tweet_atributes.drop(['contVerbosEnPrimeraPersona'],axis=1,inplace=True)
tweet_atributes.drop(['contVerbosEnSegundaPersona'],axis=1,inplace=True)
tweet_atributes.drop(['contVerbosIndicativos'],axis=1,inplace=True)
tweet_atributes.drop(['contVerbosSubjuntivos'],axis=1,inplace=True)
tweet_atributes.drop(['contVerbosPresente'],axis=1,inplace=True)
tweet_atributes.drop(['contVerbosImperativo'],axis=1,inplace=True)
tweet_atributes.drop(['contVerbosPreterito'],axis=1,inplace=True)
tweet_atributes.drop(['contVerbosFuturo'],axis=1,inplace=True)
tweet_atributes.drop(['contVerbosCondicional'],axis=1,inplace=True)

# Canvi

# tweet_atributes.drop(['seguits'],axis=1,inplace=True)
# tweet_atributes.drop(['seguidors'],axis=1,inplace=True)
tweet_atributes.drop(['hora'],axis=1,inplace=True)
tweet_atributes.drop(['diaSetmana'],axis=1,inplace=True)
# tweet_atributes.drop(['retweets'],axis=1,inplace=True)
# tweet_atributes.drop(['likes'],axis=1,inplace=True)

tweet_atributes_norm=(tweet_atributes-tweet_atributes.min())/(tweet_atributes.max()-tweet_atributes.min())
tweet_atributes_norm.fillna(0, inplace=True)

# original_stdout = sys.stdout
# with open("describe_norm_supervisado.txt","w") as f:
#     sys.stdout = f
#     print(tweet_atributes_norm.describe(include='all'))
#     sys.stdout = original_stdout

# Seleccio de variables

# INICIO DEL MODEL DE DECISION TREE

explicativas = tweet_atributes_norm.drop(['violento'],axis=1)
objetivo = tweet_atributes.violento

# Utilizamos el hiperparametro max_depth para acotar el arbol
model = DecisionTreeClassifier(max_depth=3)

model.fit(X=explicativas, y=objetivo)

# Visualizamos el modelo

plt.figure(figsize=(14,8))
plot_tree(decision_tree=model, feature_names=explicativas.columns, filled=True, fontsize=10);