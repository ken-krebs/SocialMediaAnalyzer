# This function takes the strongly sentimented tweet and prints out stock information day of the tweet
# @params --  tweet, company input
# @returns hourly stock price information for the date of the tweet. 
# 
import yfinance as yf 
import datetime



def export_tweet_stock_correlations(tweet_date, company):

    company_stock = yf.Ticker(company)
    print(company_stock.history(start = tweet_date, end = tweet_date+datetime.timedelta(days=1), interval = "1h"))



