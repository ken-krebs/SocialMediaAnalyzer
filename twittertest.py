#	EC601_ Project 2 Part 1
#	EC601 Product Design
#	Ken Krebs
#   9/26/20
#	--------------
#	This program utilizes twitters API and has defined function for accessing timelines, users, hashtags
#	using tweepy.  
#	--------------



import tweepy 
import json


#Twitter API credentials
consumer_key = "your consumer key"
consumer_secret = "your consumer secret"
access_token = "your access token"
token_secret = "your token secret"

#This function retrieves a select number of tweets from a specific username 
# @params --  the select username and number of tweets desired to retrieve
# prints in text the number of tweets specified from the user starting from the most recent
def get_user_tweets(screen_name, num_tweets):
        
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, token_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    user_tweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    user_tweets = api.user_timeline(screen_name = screen_name,count=num_tweets)
    
    for tweet in user_tweets:
        try: 
            print(tweet.text)
        except:
            #if unable to retreive tweets, give tweepy error
            print(tweepy.error.TweepError)
        


    


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
    


## This function prints the most recent tweets under a specific hashtag
# @params -- specific hashtag desired to scrape tweets from
# prints tweets from specific hashtag
def get_hashtags(hashtag):

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, token_secret)
    api = tweepy.API(auth)

  
    for tweet in tweepy.Cursor(api.search, lang="en", q=hashtag, rpp=100).items(5):
        print(tweet.text)
            


## This function prints the trending topic based on a specific location, limited to select North American cities
# defined in the citydict dictionary. 
# @params -- takes the name of the geolocation to find trending topics from.
# 
def trending_topics(location):

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, token_secret)
    api = tweepy.API(auth)

    citydict = {

        "New York": "2459115",
        "Boston": "2367105",
        "Los Angeles": "2442047",
        "Chicago": "2379574",
        "Toronto": "4118"
    }
  
    print(location)
    woeid = citydict[location]
    print(woeid)
    # fetching the trends 
    trends = api.trends_place(id = woeid) 
  
    # printing the information 
    print("Top trends for ", location) 
  
    for value in trends: 
        for trend in value['trends']: 
            print(trend['name']) 


if __name__ == '__main__':
    #pass in the username of the account you want to download and the number of tweets to receive
    get_user_tweets("@this user", 5)
    get_hashtags("#thishashtag")
    trending_topics("Boston")