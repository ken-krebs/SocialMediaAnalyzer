#	EC601_ Project 2 Part 2
#	EC601 Product Design
#	Ken Krebs
#   9/26/20
#	--------------
#	This program utilizes twitters API and has defined function for accessing timelines, users, hashtags
#	using tweepy to analyze sentiment of CEO's tweets and the corresponding stock prices after strongly sentimented tweets. 
#	--------------



import tweepy 
import json


# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import yfinance as yf 
import datetime


#Twitter API credentials
consumer_key = "your consumer key"
consumer_secret = "your consumer secret"
access_token = "your access token"
token_secret = "your token secret"

#This function retrieves a select number of tweets from a specific username 
# @params --  the select username and number of tweets desired to retrieve
# prints in text the number of tweets specified from the user starting from the most recent
def get_user_tweets(screen_name, company, num_tweets):
        
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, token_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    user_tweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    user_tweets = api.user_timeline(screen_name = screen_name,count=num_tweets, tweet_mode='extended')
    
    for tweet in user_tweets:
        analyze_text_sentiment(tweet, company)
        
        

#This function saves the specified tweets and exports them in a json file
# @params --  list of tweets desired to be exported, must by type <class 'tweepy.models.Status'>
# @return -- a file saved of the tweets in json
def save_to_json(user_tweets):
    file = open('tweet.json', 'w') 
    for status in user_tweets:
        try: json.dump(status._json,file,sort_keys = True,indent = 4)
        except:
            print("unable to export to JSON file")
    
    #close the file
    print("Tweets exported as JSON file")
    file.close()
    


## This function turns gets the CEO's twitter handle and executes the twitter API functions
# @params -- specific company stock symbol to inspect
# 
def get_ceo_name(company):

    company_ceo = {

        "AAPL": "@tim_cook",
        "TSLA": "@elonmusk",
        "TWTR": "@jack",
        "PYPL": "@Dan_Schulman",
        "PEP": "@ramonlaguarta",
        "VZ" : "@hansvestberg",
        "GM" : "@mtbarra",
        "SPOT" :  "@eldsjal",
        "AMZN" : "@jeffbezos",
        "FB" : "@finkd",
        "GOOGL" : "@sundarpichai",
        "BOX" : "@levie",
        "MSFT" : "@satyanadella"
    }
    
    twitter_name = company_ceo[company]
    print(twitter_name)
    get_user_tweets(twitter_name, company, 200)
    



# This function turns a string of text into a sentiment analysis score
# @params --  the specific text as a string that is to be analyzed for sentiment. 
# @returns an overall score of sentiment on a scale from 1 (very positive) to -1 (very negative). Neutral is defined as 
# -.25 to .25. It also returns a magnitude score from 0 to infinity on the strength of sentiment regardless of score. 
def analyze_text_sentiment(tweet, company):

    
    # Instantiates a client
    client = language.LanguageServiceClient()

    document = types.Document(
        content=tweet.full_text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text and sends to stock price function
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    if sentiment.score > .85 or sentiment.score < -.25:
        print('Text: {}'.format(tweet.full_text))
        print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
        export_tweet_stock_correlations(tweet, company)
        
        
# This function takes the strongly sentimented tweet and prints out stock information day of the tweet
# @params --  tweet, company input
# @returns hourly stock price information for the date of the tweet. 
# 
def export_tweet_stock_correlations(tweet, company):

    company_stock = yf.Ticker(company)
    print(company_stock.history(start = tweet.created_at, end = tweet.created_at+datetime.timedelta(days=1), interval = "1h"))
    





if __name__ == '__main__':

    name = input ("Enter company to analyze: ")
    get_ceo_name(name)
    