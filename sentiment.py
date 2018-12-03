# -*- coding: utf-8 -*-
# importing the requests library
import requests
from langdetect import detect
from googletrans import Translator
import json
import os

print("HERE")
# defining the api-endpoint 
API_URL = 'http://text-processing.com/api/sentiment/'

def get_sentiment_score(raw_tweet):
    print ("get_sentiment")
    text = raw_tweet['tweet_text']
    language = detect(text)

    if(language == 'hi'):
        translator = Translator()
        response = translator.translate(text)
        text = response.text

    data = { "text": text }

    response = requests.post(url = API_URL, data = data)
    result = response.json()
    print(result)
    return result

def get_raw_tweets_from_file(file_name):
    print ("get_raw_tweets_from_file")
    with open(file_name, mode='r', encoding='utf-8') as tweets_json:
        current_tweets = json.load(tweets_json)
        return current_tweets

def process_tweet(raw_tweet):
    print ("process_tweet")
    raw_tweet['sentiment'] = get_sentiment_score(raw_tweet)
    return raw_tweet

def create_file(new_file, tweet_array):
    print ("create_file")
    # create file 
    if not os.path.exists(new_file):
        open(new_file, 'w+').close()
        with open(new_file, mode='w', encoding='utf-8') as f:
            json.dump([], f)
            
    # append to file
    with open(new_file, mode='r', encoding='utf-8') as tweets_json:
        current_tweets = json.load(tweets_json)
        
    with open(new_file, mode='w', encoding='utf-8') as tweets_json:
        current_tweets = current_tweets + tweet_array
        json.dump(current_tweets, tweets_json)


def process_file(input_file_path, output_file_path):
    print('process_file')
    tweets = get_raw_tweets_from_file(input_file_path)
    processed_tweets = []
    for tweet in tweets:
        processed_tweets.append(process_tweet(tweet))
    create_file(output_file_path, processed_tweets)


def process_all_files(root_path):
    print('process_all_file')
    for root, dirs, files in os.walk(root_path):
        print("inside first loop")
        for file in files:
            print("inside second loop")
            input_file_path = root + '/' + file
            output_filename = file.replace('.json','_new.json')
            output_file_path = root + '/' + output_filename
            try:
                process_file(input_file_path, output_file_path)
                print('Successfully processed: ' + output_file_path)
            except:
                print('Error caused by:')
                print('File Name: ' + file)
                print('File Path: ' + output_file_path)
            print(" ")


ROOT_PATH = '/Users/sonalsingh/Documents/MSCS/1stSEM/IR/Projects/Project4/dev/tweets/'
process_all_files(ROOT_PATH)




# The text to analyze
# text = u'अमेरिका को फिर से महान बनाने देता है'
# language = detect(text)

# if(language == 'hi'):
#     translator = Translator()
#     response = translator.translate(text)
#     text = response.text

# data = { "text": text }

# response = requests.post(url = API_URL, data = data)
# result = response.json()
# print(result)
# print(result['probability'])
# print(result['label'])