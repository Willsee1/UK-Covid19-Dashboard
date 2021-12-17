import csv
import json
from typing import TextIO
from uk_covid19 import Cov19API
import sched
import time
import logging

# Logging code explained in 'main.py'
logging.basicConfig(filename="logging_file.log",
                    format='%(asctime)s - %(message)s - %(levelname)s',
                    filemode='w')
logger = logging.getLogger('covid_data_handler')
logger.setLevel(logging.DEBUG)

# This modules global variables
csv_filename = "nation_2021-10-28.csv"
s = sched.scheduler(time.time, time.sleep)


def parse_csv_data(csv_filename):
    '''Parameters/Arguements:
    csv_filename -
        A variable assigned the string of
        the csv file containing national COVID
        data.

This function takes in the variable csv_filename and
opens the file stored inside it before putting it
in a list called contents.

    Returns/Outputs:
        contents
            A list within a list containing the data
            found within 'nation_2021-10-28.csv'.'''

    with open(csv_filename, 'r') as file:
        # Opens the file in read mode so data can't be affected
        data = csv.reader(file)
        contents = list(data)
        if csv_filename == []:
            logger.critical("csv_filename is not assigned to anything")
            exit()
        else:
            logger.info("List containing nation_2021-10-28.csv is made")
    return contents

def process_covid_csv_data(covid_csv_data):


    '''Parameters/Arguements:
        Covid_csv_data
            A variable assigned to the output
            of parse_csv_data (contents).

    This function takes in an arguement and uses it
    to find the location of the data required to be displayed
    on the web page.

    Returns/Outputs:
        last7days - The amount of Covid cases in the last 7 days
        total_deaths - The total amount of deaths due to Covid
                in England for the range of dates in the CSV file.
        current_hospital_cases - The amount of current hospital cases
                Due to Covid.'''

    current_hospital_cases = int(covid_csv_data[1][5])
    # Navigates covid_csv_data to find the current hospital cases
    total_deaths = int(covid_csv_data[14][-3])
    # Navigates covid_csv_data to find the total deaths
    last7days = int(0)
    for j in range(2, 9):
        last7days += int(covid_csv_data[j+1][-1])
    # Gets data across last 7 days using a for loop
    return last7days, total_deaths, current_hospital_cases


def covid_API_request(location='Exeter', location_type='ltla'):

    '''Parameters/Arguements:
        location -  A variable With a default value of 'Exeter' is
                    the default location to get data out of the API from.
        loction type - A Varaible assigned a default string value of 'ltla'
                       that is assigned the type of location the value of
                       the 'location' variable is.'''

    '''Not sure how to complete function/get it working'''

    API_filter = [
        "areaType=" + location_type,
        "areaName=" + location
    ]
    structure = {
        "date": "date",
        "areaName": "areaName",
        "areaCode": "areaCode",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "cumCasesByPublishDate": "cumCasesByPublishDate",
        "hospitalCase": "hospitalcases",
        "newCasesBySpeciemenDate": "newCasesBySpecimenDate"
    }

    initialise_Api = Cov19API(filters=API_filter, structure=structure)

    api_extraction = initialise_Api.get_csv()

    return(api_extraction)


def schedule_covid_updates(update_interval=10, update_name='update data'):
    '''Arguements/inputs
        update_interval - An integer variable who's value is a defaultly
        assigned to 10. This variable determines (in seconds) how long after
        its function call will it run the update.
        update_name - A string variable assigning the name of the update'''
    updated_data = s.enter(update_interval, 1, parse_csv_data)


# MAIN CODE of the module
covid_csv_data = parse_csv_data(csv_filename)
covid_data = process_covid_csv_data(covid_csv_data)
if covid_data == []:
    logger.error("NO data was retrived from covid_csv_data")
    exit()
else:
    logger.info("data is retrived from covid_csv_data")
# Local covid data
# covid_API_request()
# National data call command
# covid_API_request('England', 'nation')
