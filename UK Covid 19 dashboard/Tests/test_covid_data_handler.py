'''DATA HANDLER TESTS'''
import pytest
# TEST FOR CHECKING 'covid_data_handler' IS OPENED AND HAS 639 LINES IN THE CREATED LIST
from requests.models import ContentDecodingError
from covid_data_handler import parse_csv_data
from covid_data_handler import process_covid_csv_data
from covid_data_handler import covid_API_request
from covid_data_handler import schedule_covid_updates
def test_parse_csv_data ():
    data = parse_csv_data ('nation_2021-10-28.csv')
    assert len ( data ) == 639

# TEST FOR RETRIVING DATA FROM THE CSV FILE IN 'covid_data_handler'
def test_process_covid_csv_data ():
    last7days_cases ,total_deaths ,current_hospital_cases = process_covid_csv_data ( parse_csv_data ('nation_2021-10-28.csv' ) )
    assert last7days_cases == 240_299
    assert total_deaths == 141_544
    assert current_hospital_cases == 7_019

def test_covid_API_request():
    data = covid_API_request()
    assert isinstance(data, dict)

def test_schedule_covid_updates():
    schedule_covid_updates(update_interval=10, update_name='update data')