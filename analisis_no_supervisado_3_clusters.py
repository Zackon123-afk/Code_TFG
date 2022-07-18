import pandas as pd
import sys

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

## PREPARACION DE PANDAS

tweet_atributes = pd.read_csv('atributs_results_3_clusters.csv',engine='python')

original_stdout = sys.stdout


condition = tweet_atributes['KMeans_Clusters'] == 0

tweet_results = tweet_atributes[condition]

with open("results_analisis_3_clusters_0.txt","w") as f:
    sys.stdout = f
    print(tweet_results.describe(include='all'))


condition = tweet_atributes['KMeans_Clusters'] == 1

tweet_results = tweet_atributes[condition]

with open("results_analisis_3_clusters_1.txt","w") as f:
    sys.stdout = f
    print(tweet_results.describe(include='all'))


condition = tweet_atributes['KMeans_Clusters'] == 2

tweet_results = tweet_atributes[condition]

with open("results_analisis_3_clusters_2.txt","w") as f:
    sys.stdout = f
    print(tweet_results.describe(include='all'))


sys.stdout = original_stdout