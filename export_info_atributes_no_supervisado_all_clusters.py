from tkinter.tix import Select
import pandas as pd
import sys
import xlsxwriter

with open('nombre de funciones - supervisado.txt','r') as file:
    atributes = file.read()
    atributes = atributes.split(',')
atributes.remove("tema")

archivo=xlsxwriter.Workbook('results_analisis_clusters.xlsx')

# ESCRIVIM LA INFORMACIO DEL ANALISIS DE 3 CLUSTERS

tweet_atributes = pd.read_csv('atributs_results_3_clusters.csv',engine='python')

header = ['Atributes','Mean - 1','Std - 1','Mean - 2','Std - 2','Mean - 3','Std - 3']

condition = tweet_atributes['KMeans_Clusters'] == 0

tweet_results_1 = tweet_atributes[condition]

condition = tweet_atributes['KMeans_Clusters'] == 1

tweet_results_2 = tweet_atributes[condition]

condition = tweet_atributes['KMeans_Clusters'] == 2

tweet_results_3 = tweet_atributes[condition]

hoja=archivo.add_worksheet('3_clusters')

for i in range(len(header)):
    hoja.write(0,i,header[i])

for i in range(len(atributes)):
    for j in range(len(header)):
        if header[j] == "Atributes":
            hoja.write(i+1,j,atributes[i])
        elif header[j] == "Mean - 1":
            hoja.write(i+1,j,tweet_results_1[atributes[i]].mean())
        elif header[j] == "Std - 1":
            hoja.write(i+1,j,tweet_results_1[atributes[i]].std())
        elif header[j] == "Mean - 2":
            hoja.write(i+1,j,tweet_results_2[atributes[i]].mean())
        elif header[j] == "Std - 2":
            hoja.write(i+1,j,tweet_results_2[atributes[i]].std())
        elif header[j] == "Mean - 3":
            hoja.write(i+1,j,tweet_results_3[atributes[i]].mean())
        elif header[j] == "Std - 3":
            hoja.write(i+1,j,tweet_results_3[atributes[i]].std())


# ESCRIVIM LA INFORMACIO DEL ANALISIS DE 4 CLUSTERS

tweet_atributes = pd.read_csv('atributs_results_4_clusters.csv',engine='python')

header = ['Atributes','Mean - 1','Std - 1','Mean - 2','Std - 2','Mean - 3','Std - 3','Mean - 4','Std - 4']

condition = tweet_atributes['KMeans_Clusters'] == 0

tweet_results_1 = tweet_atributes[condition]

condition = tweet_atributes['KMeans_Clusters'] == 1

tweet_results_2 = tweet_atributes[condition]

condition = tweet_atributes['KMeans_Clusters'] == 2

tweet_results_3 = tweet_atributes[condition]

condition = tweet_atributes['KMeans_Clusters'] == 3

tweet_results_4 = tweet_atributes[condition]

hoja=archivo.add_worksheet('4_clusters')

for i in range(len(header)):
    hoja.write(0,i,header[i])

for i in range(len(atributes)):
    for j in range(len(header)):
        if header[j] == "Atributes":
            hoja.write(i+1,j,atributes[i])
        elif header[j] == "Mean - 1":
            hoja.write(i+1,j,tweet_results_1[atributes[i]].mean())
        elif header[j] == "Std - 1":
            hoja.write(i+1,j,tweet_results_1[atributes[i]].std())
        elif header[j] == "Mean - 2":
            hoja.write(i+1,j,tweet_results_2[atributes[i]].mean())
        elif header[j] == "Std - 2":
            hoja.write(i+1,j,tweet_results_2[atributes[i]].std())
        elif header[j] == "Mean - 3":
            hoja.write(i+1,j,tweet_results_3[atributes[i]].mean())
        elif header[j] == "Std - 3":
            hoja.write(i+1,j,tweet_results_3[atributes[i]].std())
        elif header[j] == "Mean - 4":
            hoja.write(i+1,j,tweet_results_4[atributes[i]].mean())
        elif header[j] == "Std - 4":
            hoja.write(i+1,j,tweet_results_4[atributes[i]].std())


# ESCRIVIM LA INFORMACIO DEL ANALISIS DE 5 CLUSTERS

tweet_atributes = pd.read_csv('atributs_results_5_clusters.csv',engine='python')

header = ['Atributes','Mean - 1','Std - 1','Mean - 2','Std - 2','Mean - 3','Std - 3','Mean - 4','Std - 4','Mean - 5','Std - 5']

condition = tweet_atributes['KMeans_Clusters'] == 0

tweet_results_1 = tweet_atributes[condition]

condition = tweet_atributes['KMeans_Clusters'] == 1

tweet_results_2 = tweet_atributes[condition]

condition = tweet_atributes['KMeans_Clusters'] == 2

tweet_results_3 = tweet_atributes[condition]

condition = tweet_atributes['KMeans_Clusters'] == 3

tweet_results_4 = tweet_atributes[condition]

condition = tweet_atributes['KMeans_Clusters'] == 4

tweet_results_5 = tweet_atributes[condition]

hoja=archivo.add_worksheet('5_clusters')

for i in range(len(header)):
    hoja.write(0,i,header[i])

for i in range(len(atributes)):
    for j in range(len(header)):
        if header[j] == "Atributes":
            hoja.write(i+1,j,atributes[i])
        elif header[j] == "Mean - 1":
            hoja.write(i+1,j,tweet_results_1[atributes[i]].mean())
        elif header[j] == "Std - 1":
            hoja.write(i+1,j,tweet_results_1[atributes[i]].std())
        elif header[j] == "Mean - 2":
            hoja.write(i+1,j,tweet_results_2[atributes[i]].mean())
        elif header[j] == "Std - 2":
            hoja.write(i+1,j,tweet_results_2[atributes[i]].std())
        elif header[j] == "Mean - 3":
            hoja.write(i+1,j,tweet_results_3[atributes[i]].mean())
        elif header[j] == "Std - 3":
            hoja.write(i+1,j,tweet_results_3[atributes[i]].std())
        elif header[j] == "Mean - 4":
            hoja.write(i+1,j,tweet_results_4[atributes[i]].mean())
        elif header[j] == "Std - 4":
            hoja.write(i+1,j,tweet_results_4[atributes[i]].std())
        elif header[j] == "Mean - 5":
            hoja.write(i+1,j,tweet_results_5[atributes[i]].mean())
        elif header[j] == "Std - 5":
            hoja.write(i+1,j,tweet_results_5[atributes[i]].std())


# ESCRIVIM LA INFORMACIO DEL ANALISIS DE 6 CLUSTERS

tweet_atributes = pd.read_csv('atributs_results_6_clusters.csv',engine='python')

header = ['Atributes','Mean - 1','Std - 1','Mean - 2','Std - 2','Mean - 3','Std - 3','Mean - 4','Std - 4','Mean - 5','Std - 5','Mean - 6','Std - 6']

condition = tweet_atributes['KMeans_Clusters'] == 0

tweet_results_1 = tweet_atributes[condition]

condition = tweet_atributes['KMeans_Clusters'] == 1

tweet_results_2 = tweet_atributes[condition]

condition = tweet_atributes['KMeans_Clusters'] == 2

tweet_results_3 = tweet_atributes[condition]

condition = tweet_atributes['KMeans_Clusters'] == 3

tweet_results_4 = tweet_atributes[condition]

condition = tweet_atributes['KMeans_Clusters'] == 4

tweet_results_5 = tweet_atributes[condition]

condition = tweet_atributes['KMeans_Clusters'] == 5

tweet_results_6 = tweet_atributes[condition]

hoja=archivo.add_worksheet('6_clusters')

for i in range(len(header)):
    hoja.write(0,i,header[i])

for i in range(len(atributes)):
    for j in range(len(header)):
        if header[j] == "Atributes":
            hoja.write(i+1,j,atributes[i])
        elif header[j] == "Mean - 1":
            hoja.write(i+1,j,tweet_results_1[atributes[i]].mean())
        elif header[j] == "Std - 1":
            hoja.write(i+1,j,tweet_results_1[atributes[i]].std())
        elif header[j] == "Mean - 2":
            hoja.write(i+1,j,tweet_results_2[atributes[i]].mean())
        elif header[j] == "Std - 2":
            hoja.write(i+1,j,tweet_results_2[atributes[i]].std())
        elif header[j] == "Mean - 3":
            hoja.write(i+1,j,tweet_results_3[atributes[i]].mean())
        elif header[j] == "Std - 3":
            hoja.write(i+1,j,tweet_results_3[atributes[i]].std())
        elif header[j] == "Mean - 4":
            hoja.write(i+1,j,tweet_results_4[atributes[i]].mean())
        elif header[j] == "Std - 4":
            hoja.write(i+1,j,tweet_results_4[atributes[i]].std())
        elif header[j] == "Mean - 5":
            hoja.write(i+1,j,tweet_results_5[atributes[i]].mean())
        elif header[j] == "Std - 5":
            hoja.write(i+1,j,tweet_results_5[atributes[i]].std())
        elif header[j] == "Mean - 6":
            hoja.write(i+1,j,tweet_results_6[atributes[i]].mean())
        elif header[j] == "Std - 6":
            hoja.write(i+1,j,tweet_results_6[atributes[i]].std())


archivo.close()