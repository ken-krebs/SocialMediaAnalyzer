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
    return twitter_name