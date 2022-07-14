from datetime import date, datetime
from unittest import result
import pandas as pd
import analize_corpus
import csv
import tweepy
import json

def tweeterInformation(usernames):

    followers = []
    following = []

    consumer_key= "kxKPh40tJz4dTHIDJxCulXVmH"
    consumer_secret= "Tb3j4u3jAmqyZI0ueQomwaDZuGXOTgQ2P3r6R0r6pHdEuLHyqm"
    access_token="1900139084-Kf1x4ozKXOPO65ZzVQC0Gn8U7dQ2m2KywwIS41J"
    access_token_secret= "OnOsjdLK6OJkuHh4WUWUL0v9lNdIHVgRhfk13F1UrYr16"

    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    for username in usernames:
        try:
            data= api.get_user(username)
            data = json.loads(json.dumps(data._json,indent=2))
            followers.append(str(data["followers_count"]))
            following.append(str(data['friends_count']))
        except:
            followers.append(str('0'))
            following.append(str('0'))
        

    return followers,following

def dateToWeekday(datesToChange):
    listOfDayWeeks = []
    for date in datesToChange:
        today = date
        listOfDayWeeks.append(today.dayofweek)
    return listOfDayWeeks

def hourToSec(hoursToChange):
    listOfSec = []
    for hour in hoursToChange:
        try:
            (h, m, s) = str(hour).split(':')
        except:
            (h, m, s) = 0,0,0
        result = int(h) * 3600 + int(m) * 60 + int(s)
        listOfSec.append(result)
    return listOfSec

print("--- Preparation of data ---\n")

df = pd.read_excel("C:\\Users\\arnau\\Dropbox\\TFG\\Code_TFG\\corpus_etiquetado.xlsx")

listOfUsernames = df['username']

listOfTweets = df['tweet']
listOfRetweets = df['retweets_count']
listOfLikes = df['likes_count']
listOfDates = dateToWeekday(df['date'])
listOfTimes = hourToSec(df['time'])
listOfFollowers, listOfFollowing = tweeterInformation(listOfUsernames)
listOfTopics = df['tema']
listOfResults = df['etiquetado']

with open('nombre de funciones - supervisado.txt','r') as file:
    header = file.read()
    header = header.split(',')

print("--- Writing in csv ---\n")

with open('atributes_etiquetado.csv','w',newline='') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerow(header)
    for tweet,like,retweet,dates,time,follower,following,topic,resulted in zip(listOfTweets,listOfLikes,listOfRetweets,listOfDates,listOfTimes,listOfFollowers,listOfFollowing,listOfTopics,listOfResults):
        atributos = analize_corpus.tractarTweet(str(tweet))
        atributos.append(str(like))
        atributos.append(str(retweet))
        atributos.append(str(dates))
        atributos.append(str(time))
        atributos.append(str(follower))
        atributos.append(str(following))
        atributos.append(str(topic))
        atributos.append(str(resulted))
        writer.writerow(atributos)

print("--- FINISHED ---\n")