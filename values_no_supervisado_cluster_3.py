import analize_corpus
import sys
import pandas as pd

tweet_atributes = pd.read_csv('atributs_results_3_clusters.csv',engine='python')

corpus = pd.read_excel("corpus_etiquetado.xlsx")
listOfTweets = corpus['tweet']

for index,row in tweet_atributes.iterrows():
    if row['KMeans_Clusters'] == 2:
        print(analize_corpus.contUnicSignosPunt(listOfTweets[index]))

# for i in range(len(tweet_atributes)):
#     if tweet_atributes[i]['KMeans_Clusters'] == 3:
#         print("yes")


# original_stdout = sys.stdout

# with open("values_no_supervisado_cluster_3.txt","w") as f:
#     sys.stdout = f
#     print()
#     sys.stdout = original_stdout