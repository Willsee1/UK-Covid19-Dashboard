from types import resolve_bases
import flask
import requests
import pprint
import json
import csv
import time
import sched
import logging
from csv import reader
from requests.models import Response

# Logging code explained in 'main.py'
logging.basicConfig(filename="logging_file.log",
                    format='%(asctime)s - %(message)s - %(levelname)s',
                    filemode='w')
logger = logging.getLogger('covid_data_handler')
logger.setLevel(logging.DEBUG)


def news_API_request(covid_terms="Covid, COVID-19, coronavirus"):
    '''Function arguments:
        covid_terms = "Covid, COVID-19, coronavirus"
    These are the default values and will be used to
    find news articles in the NEWSAPI containing the
    terms.

    The top part of this function takes in the
    default values of the variable covid_terms.
    It the opens the json file known as 'config.json'
    and retrieves my hidden api key which it uses to
    search the NEWSAPI for articles containing the terms in
    covid_terms.

    Function returns:
        headlines - a list of the latest covid
                    news article headings from the news API
        content - a list of the latest covid news
                  articles content from the news API'''

    covid_terms = covid_terms.replace(" ", " OR ")

    with open('config.json', 'r') as f_json:
        data = json.load(f_json)
        news_json = data['news']

    key_api = news_json['key_api']
    # Getting my api key from 'config.json'
    url = 'https://newsapi.org/v2/everything?'
    # Parameters for searching the API
    parameters_api = {
        'q': covid_terms,
        'apiKey': key_api
    }
    request = requests.get(url, params=parameters_api)
    request_json = request.json()
    articles = request_json['articles']

    headlines = []
    content = []
    '''Headlines and content are empty lists that will have news
    article headlines and news article content added to them
    which will be used to display on the web page'''
    for article in articles:
        headlines.append(article['title'])
        content.append(article['description'])
    # The article titles and content are being added to the lists
    return headlines, content
    # returns the lists to main program


def update_news():
    '''the local variable news is the returned data from the function above'''
    news = news_API_request()


news_articles = news_API_request()
