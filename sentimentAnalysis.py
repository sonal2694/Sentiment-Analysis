# -*- coding: utf-8 -*-
from langdetect import detect
from googletrans import Translator
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = u'Bonjour, le monde!'
text = u"अमेरिका को फिर से महान बनाने देता है"
language = detect(text)

print language

if(language == 'hi'):
    translator = Translator()
    print translator.translate(text)


document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
annotation = client.analyze_sentiment(document=document)
sentiment = annotation.document_sentiment

print (annotation)
#print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))