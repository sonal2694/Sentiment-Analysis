# -*- coding: utf-8 -*-
# importing the requests library
import requests
from langdetect import detect
from googletrans import Translator

# defining the api-endpoint 
API_URL = 'http://text-processing.com/api/sentiment/'




# The text to analyze
text = u'अमेरिका को फिर से महान बनाने देता है'
language = detect(text)





if(language == 'hi'):
    translator = Translator()
    response = translator.translate(text)
    text = response.text

data = { "text": text }

response = requests.post(url = API_URL, data = data)
result = response.json()
print(result)
# print(result['probability'])
# print(result['label'])