from matplotlib.axis import Axis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from requests import head
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import openpyxl

import sys

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

## PREPARACION DE PANDAS

tweet_atributes = pd.read_csv('atributes.csv',engine='python')

# original_stdout = sys.stdout
# with open("describe.txt","w") as f:
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

# with open("describe_norm.txt","w") as f:
#     sys.stdout = f
#     print(tweet_atributes_norm.describe(include='all'))
#     sys.stdout = original_stdout

# # PROCEDIMENT CODO DE JAMBU

# wcss = [] #Within-Cluster-Sum-of-Squares

# for i in range(1,15):
#     kmeans = KMeans(n_clusters=i, max_iter= 300)
#     kmeans.fit(tweet_atributes_norm) #Aplicamos K-means a la base de datos
#     wcss.append(kmeans.inertia_)

# #Aplicamos Codo de Jambú

# plt.plot(range(1,15),wcss)
# plt.title("Codo de Jambú")
# plt.xlabel("Nº de Clusters")
# plt.ylabel("WCSS")
# plt.show()


## EJECTUTAMOS EL CLUSTERING Y ANALIZAMOS

clustering = KMeans(n_clusters=3,max_iter=300)
clustering.fit(tweet_atributes_norm)

# Añadimos los clusters a la matriz de información
tweet_atributes['KMeans_Clusters'] = clustering.labels_

# Creamos un csv con los resultados
tweet_atributes.to_excel('atributs_results.xlsx',index=False)

# 1.Resultados de PCA en matriz de 2 dimensiones

pca = PCA(n_components=2)
pca_tweets = pca.fit_transform(tweet_atributes_norm)
pca_tweets_df = pd.DataFrame(data=pca_tweets,columns=['Component_1','Component_2'])
pca_names_tweets = pd.concat([pca_tweets_df, tweet_atributes[['KMeans_Clusters']]], axis=1)

fig = plt.figure(figsize=(6,6))

ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Component 1', fontsize = 15)
ax.set_ylabel('Component 2', fontsize = 15)
ax.set_title('Componentes principales', fontsize=20)

color_theme = np.array(["blue","green","orange","red"])
ax.scatter(x = pca_names_tweets.Component_1, y = pca_names_tweets.Component_2,
    c=color_theme[pca_names_tweets.KMeans_Clusters], s = 50)

plt.show()

# 2.Resultados de PCA con:

# # 2.1. Con la varianza explicada individual

# pca = PCA()
# X_pca = pca.fit_transform(tweet_atributes_norm)

# exp_var_pca = pca.explained_variance_ratio_

# cum_sum_eigenvalues = np.cumsum(exp_var_pca)

# plt.bar(range(0,len(exp_var_pca)), exp_var_pca, alpha=0.5, align='center', label='Individual explained variance')
# plt.step(range(0,len(cum_sum_eigenvalues)), cum_sum_eigenvalues, where='mid', label='Cumulative explained variance')
# plt.ylabel('Explained variance ratio')
# plt.xlabel('Principal component index')
# plt.legend(loc='best')
# plt.tight_layout()
# plt.show

# # 2.2. Que variables son las mas importantes

# with open('nombre de funciones.txt','r') as file:
#     header = file.read()
#     header = header.split(',')


# model = PCA().fit(tweet_atributes_norm)
# X_pc = model.transform(tweet_atributes_norm)

# n_pcs = model.components_.shape[0]

# most_important = [np.abs(model.components_[i]).argmax() for i in range(n_pcs)]

# initial_features_names = header

# most_important_names = [initial_features_names[most_important[i]] for i in range(n_pcs)]
# dic = {'PC{}'.format(i): most_important_names[i] for i in range(n_pcs)}

# df = pd.DataFrame(dic.items())

# original_stdout = sys.stdout

# with open("pca_all_pcs.txt","w") as f:
#     sys.stdout = f
#     print(df)
#     sys.stdout = original_stdout