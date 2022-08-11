from tkinter import Y
import pandas as pd
import matplotlib.pyplot as plt
import sys
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

## PREPARACION DE PANDAS

tweet_atributes = pd.read_csv('atributes_etiquetado.csv',engine='python')
tweet_atributes_general = tweet_atributes.drop(['tema'],axis=1)

tweet_atributes = pd.get_dummies(data=tweet_atributes, drop_first=False)

original_stdout = sys.stdout
with open("describe_attributes.txt","w") as f:
    sys.stdout = f
    print(tweet_atributes.describe(include='all'))
    sys.stdout = original_stdout

# Seleccio de variables

condition = tweet_atributes['tema_C'] == 1
tweet_atributes_tema_C = tweet_atributes[condition]
tweet_atributes_tema_C.drop(['tema_C'],axis=1,inplace=True)

condition = tweet_atributes['tema_F'] == 1
tweet_atributes_tema_F = tweet_atributes[condition]
tweet_atributes_tema_F.drop(['tema_F'],axis=1,inplace=True)

condition = tweet_atributes['tema_P'] == 1
tweet_atributes_tema_P = tweet_atributes[condition]
tweet_atributes_tema_P.drop(['tema_P'],axis=1,inplace=True)

condition = tweet_atributes['tema_S'] == 1
tweet_atributes_tema_S = tweet_atributes[condition]
tweet_atributes_tema_S.drop(['tema_S'],axis=1,inplace=True)

condition = tweet_atributes['tema_TV'] == 1
tweet_atributes_tema_TV = tweet_atributes[condition]
tweet_atributes_tema_TV.drop(['tema_TV'],axis=1,inplace=True)

# INICIO DEL MODEL DE DECISION TREE

plt.figure(figsize=(29,12))

# # Model con todo

# explicativas = tweet_atributes_general.drop(['violento'],axis=1)
# objetivo = tweet_atributes_general.violento

# # Utilizamos el hiperparametro max_depth para acotar el arbol
# model = DecisionTreeClassifier(max_depth=4)
# model.fit(X=explicativas, y=objetivo)

# # Visualizamos el modelo

# plot_tree(decision_tree=model, feature_names=explicativas.columns, filled=True, fontsize=10);


# # Modelo con el tema del Covid

# explicativas = tweet_atributes_tema_C.drop(['violento'],axis=1)
# objetivo = tweet_atributes_tema_C.violento

# # Utilizamos el hiperparametro max_depth para acotar el arbol
# model = DecisionTreeClassifier(max_depth=4)
# model.fit(X=explicativas, y=objetivo)

# # Visualizamos el modelo

# plot_tree(decision_tree=model, feature_names=explicativas.columns, filled=True, fontsize=10);


# # Modelo con el tema del Futbol

# explicativas = tweet_atributes_tema_F.drop(['violento'],axis=1)
# objetivo = tweet_atributes_tema_F.violento

# # Utilizamos el hiperparametro max_depth para acotar el arbol
# model = DecisionTreeClassifier(max_depth=4)
# model.fit(X=explicativas, y=objetivo)

# # Visualizamos el modelo

# plot_tree(decision_tree=model, feature_names=explicativas.columns, filled=True, fontsize=10);


# # Modelo con el tema del Polític

# explicativas = tweet_atributes_tema_P.drop(['violento'],axis=1)
# objetivo = tweet_atributes_tema_P.violento

# # Utilizamos el hiperparametro max_depth para acotar el arbol
# model = DecisionTreeClassifier(max_depth=4)
# model.fit(X=explicativas, y=objetivo)

# # Visualizamos el modelo

# plot_tree(decision_tree=model, feature_names=explicativas.columns, filled=True, fontsize=10);


# # Modelo con el tema del Social

# explicativas = tweet_atributes_tema_S.drop(['violento'],axis=1)
# objetivo = tweet_atributes_tema_S.violento

# # Utilizamos el hiperparametro max_depth para acotar el arbol
# model = DecisionTreeClassifier(max_depth=4)
# model.fit(X=explicativas, y=objetivo)

# # Visualizamos el modelo

# plot_tree(decision_tree=model, feature_names=explicativas.columns, filled=True, fontsize=10);


# Modelo con el tema del Televisió

explicativas = tweet_atributes_tema_TV.drop(['violento'],axis=1)
objetivo = tweet_atributes_tema_TV.violento

# Utilizamos el hiperparametro max_depth para acotar el arbol
model = DecisionTreeClassifier(max_depth=4)
model.fit(X=explicativas, y=objetivo)

# Visualizamos el modelo

plot_tree(decision_tree=model, feature_names=explicativas.columns, filled=True, fontsize=10);