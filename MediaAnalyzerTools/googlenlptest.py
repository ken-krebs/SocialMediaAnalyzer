#	EC601_ Project 2 Part 1
#	EC601 Product Design
#	Ken Krebs
#   9/26/20
#	--------------
#	This program explores Google Natural Language Processing API with two main functions showing sentiment and 
#   specific entities of speech.  
#	--------------

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


# This function turns a string of text into a sentiment analysis score
# @params --  the specific text as a string that is to be analyzed for sentiment. 
# @returns an overall score of sentiment on a scale from 1 (very positive) to -1 (very negative). Neutral is defined as 
# -.25 to .25. It also returns a magnitude score from 0 to infinity on the strength of sentiment regardless of score. 
def analyze_text_sentiment(text):
    # Instantiates a client
    client = language.LanguageServiceClient()

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))


# This function turns a string of text into a entities analysis.
# @params --  the specific text as a string that is to be analyzed for entities. 
# @returns -- returns the name of entities identified in the text as well as the type and salience (on a scale of 0 to 1).
# Salience shows the importance of the entity to the entire document. 
def analyze_text_entities(text):
    # Instantiates a client
    client = language.LanguageServiceClient()

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    response = client.analyze_entities(document=document)

    for entity in response.entities:
        print(u"Representative name for the entity: {}".format(entity.name))
        print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))
        print(u"Salience: {}".format(entity.salience))


   

if __name__ == '__main__':
    #pass in the username of the account you want to download and the number of tweets to receive
    text = u"Today is a very good day. It is sunny and the weather is beautiful. I ate cake and drank a glass of water."


    analyze_text_sentiment(text)
    analyze_text_entities(text)
