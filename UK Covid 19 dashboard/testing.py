'''Covid_data_Handler related test function calls'''
from Tests.test_covid_data_handler import test_parse_csv_data
from Tests.test_covid_data_handler import test_process_covid_csv_data
from Tests.test_covid_data_handler import test_schedule_covid_updates
from Tests.test_covid_data_handler import test_covid_API_request
test_parse_csv_data()
test_process_covid_csv_data()
test_schedule_covid_updates()
#test_covid_API_request() function does not work/is not finished

'''Covid_news_handling related test function calls'''
from Tests.test_covid_news_handling import test_news_API_request
from Tests.test_covid_news_handling import test_update_news
test_news_API_request()
#test_update_news() function does not work/is not finished

#from Tests.test_main import
    
