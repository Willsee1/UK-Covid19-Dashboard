from flask import Flask
from flask import render_template
import sched
import json
import time
import csv
from flask import request
import flask
import random
import logging
from covid_data_handler import covid_data
from covid_news_handling import news_articles


# Once code is ran check the logger for Web page link

# Creating and configuring a logger
logging.basicConfig(filename="logging_file.log",
                    format='%(asctime)s - %(message)s - %(levelname)s',
                    filemode='w')
# In write mode so it is easy to see what happens every run
# Creating an object
logger = logging.getLogger()
# Setting the logger to DEBUG so all levels appear in the file
logger.setLevel(logging.DEBUG)


# This modules global variables
s = sched.scheduler(time.time, time.sleep)
app = Flask(__name__)
news = [
        {
            "title": news_articles[0][0],
            "content": news_articles[1][0]
        },
        {
            "title": news_articles[0][1],
            "content": news_articles[1][1]
        }

]

'''news - A dictionary within a list, that is responsible for
        the display of the news on the webpage.It uses the 'title
        and 'content' tags from 'index.html' to allow the real life
        news and content pulled from the NEWSAPI to be displayed.

news_articles - imported from the data handling module - holds the titles
and contents of news articles and is used to dislay them on the web page.'''


def new_news_articles():
    '''Variables:
            article_number - is assigned a random number in the range
            2 --> 20
    This function appends 'news' by adding more articles to be displayed,
    it uses a random number generator to pick an article out of new_articles'''
    article_number = random.randint(2, 20)
    news.append(
                {
                 "title": news_articles[0][article_number],
                 "content": news_articles[1][article_number],
                }
        )
logger.info("new articles added to the web page")


@app.route('/')
@app.route('/index')
def web_page():
    '''This function deals with the web page and its display.
    It uses the 'index.html'terms (found on the left hand side
    of the equals signs) and assigns value or variable depending
    on what needs to be displayed.'''
    global news
    s.run(blocking=False)
    request_txt_field = request.args.get('two')
    if request_txt_field:
        update_news()
    return render_template('index.html',
                           title='Daily update',
                           news_articles=news,
                           location=local,
                           nation_location=national,
                           national_7day_infections=covid_data[0],
                           deaths_total='Total deaths: ' + str(covid_data[1]),
                           hospital_cases='Hospital cases: ' + str(covid_data[2]),
                           )
# On lines 86 and 87 data must be turned into a str value to allow concatination


'''lines 63-65 use covid_data imported from 'covid_data_handler' and
use it to assign the correct covid statistic to be displayed on the website
next to its relavent title'''


def update_news():
    updated_news = s.enter(4, 1, new_news_articles)
    logger.info("New news articles have been scheduled")
    
    '''This function gets called in the 'web_page'
    function and is used to schedule an update on the page
    with addtional news articles along the right hand
    side of the web page when requested after a set
    interval of time.'''


def covid_locations():
    '''This function reads location information
    out of 'config.json' to find out both the national and
    local locations relavent to the data on the web page.
    Returns:
        national - the national location as found in config.json
        local - the local location as found in config.json'''
    with open('config.json') as json_file:
        data = json.load(json_file)
        locations = data['location']
# creates location variable assigned to 'location'  in 'config.json'
    national = locations['national']
    local = locations['Local']
    return national, local


def article_removal():
    ''' Function allows the user to remove news articles from the list on
    the side of the web page - comes in to play when the 'x' button next to
    the article is pressed.'''
    pass


if __name__ == '__main__':
    national, local = covid_locations()
    '''national and local are assigned each
    to the 1st and 2nd returns of covid_locations'''
    if national == ' ':
        logger.error('national location not retrived from config.json')
    else:
        logger.info('data has been retrived from the json file')
    app.run()
