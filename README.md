# Current CEO's Twitter Sentiment and Stock Prices
Utilizing both Twitter and Google's NLP API's I designed a program to explore the correlation between a stronly sentimented tweet by various CEO's and their respective companies stock prices in the hours following the tweet. 

# Motivation and Uses
Although there are many aspects that go into a company's evaluation and stock price, the growing influence of social media and ability of a CEO to communicate to a large audience in real time is a factor I thought was worth exploring. This product could be useful for an indidual trader buying and selling stocks who is interested in all pertinent information regarding a stock, including the CEO's social media. It could also be useful for research analysts making business decisions regarding shareholding and understanding the effect social media can have on the stock market in general. 

# Features
The scope of the tool I designed is limited to active twitter using CEO's for more popular companies in the S&P500 including Apple, Tesla, Twitter, PayPal etc. While many CEO's twitter are mostly positive, the program returns tweets that have a very strong positive sentiment and also medium to strong negative sentiment. Along with the tweets, the program also returns companies stock performance by hour following the tweet. 

# Use
**Input**
Upon initializing the program, the program will request a company to analyze. 
The current list of companies available for analysis are listed below. 
The desired *stock symbol* from the chart can serve as the input
Companies and their Stock Symbol
-AAPL : Apple Inc.
-TSLA : Tesla Inc. 
-TWTR : Twitter Inc.
-PYPL: PayPal Holdings Inc.
-PEP: PepsiCo, Inc.
-VZ : Verizon Communications Inc.
-GM : General Motors Company
-SPOT :  Spotify Technology SA
-AMZN : Amazon.com, Inc.
-FB : Facebook, Inc. Common Stock
-GOOGL : Alphabet Inc Class A (Google)
-BOX : Box Inc
-MSFT : Microsoft Corporation


**Output**
For every strongly sentimented tweet, the program will print the tweet, teh sentiment score of the tweet, and hour by hour stock price of the company the day of the tweet or following day. 
```
Text: The extreme difficulty of scaling production of new technology is not well understood. It’s 1000% to 10,000% harder than making a few prototypes. The machine that makes the machine is vastly harder than the machine itself.
Sentiment: -0.5, 1.7000000476837158
              Open    High     Low   Close    Volume  Dividends  Stock Splits
Date                                                                         
2020-09-22  429.60  437.60  422.55  428.05  19444884          0             0
2020-09-22  428.20  431.65  417.60  421.29  12257016          0             0
2020-09-22  421.37  428.86  420.21  427.86   8007740          0             0
2020-09-22  427.80  432.74  423.44  431.90   7185708          0             0
2020-09-22  431.80  433.85  427.54  430.20   7623521          0             0
2020-09-22  430.27  430.27  422.33  422.74   7717675          0             0
2020-09-22  422.60  428.47  421.17  423.97   5820778          0             0
```

# Limitations
Many strongly sentimented tweets can be irrelevant to the performance of the company for example remembering a loved one, celebrating a holiday etc. Also many CEO's may be well aware to the fact of damaging the company's image with a strongly sentimented tweet and avoid it altogether. 

Technical limitations include the Yahoo finance library only being able to pull range of stock prices from the past 730 days, when some CEO's only post a few times per year. Additionally tweets from the weekends are ignored as well. In the future a more accurate finance API could be utilized to icnrease accuracy and range.  

