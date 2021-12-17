INTRODUCTION
    Why was the product made?
This product was made to display data on the Coronavirus situation 
within the UK, and tp display news articles on Coronavirus to users 
on a web page whose link is provided once the python code is run.
This product was made as part of a continuous form of assesment for the 
ECM1400 programming module.

    What does the product do?
This product - a COVID dshaboard, and code - displays COVID-19 news and data on a web page;
pulling statisitcs and data from a public file and news articles from around the world
using an API. This is achieved with the use of python programming language and addtional
supporting files.


PREREQUISITES
    python version : 3.7.9 64-bit 
    Flask
    uk_Covid19

INSTALLATION
    pip install statement:

    python setup.py instal


GETTING STARTED TUTORIAL
    When getting started, open up the three python modules named:
    'Covid_data_handler.py', 'Covid_news_handling.py' and 'main.py'
    as well as the 'config.jsona and the 'nation_2021-10-28.csv' files.
    In addition to this check you have an internet connection and browser 
    to open the web page in.

TESTING
    All testing is found under the 'TESTS' folder - and each python module 
    has its own testing module assigned to it signfied by its name (the
    original module name with 'test_' infront)
    Each testing module will test the key parts of the major functions to
    ensure and prove they work as expected.
    Each test runs using 'pytest' and the 'testing.py' module which calls the
    tests functions. When run a clean terminal means that the tests have passed
    any errors that pop up into the terminal mean the tests have failed and not
    worked as intended.


DEVELOPER DOCUMENTATION
    How to use code - 
    In order to use the code properly you must first open up 'Covid_data_handler.py',
    'Covid_news_handling.py' and 'main.py' as well as the files:
    'config.json', 'nation_2021-10-28-csv' and 'logging_file.log'
    Run the 'Main.py' module - can be done by having the python file open and pressing 'CTRL + F5'
    which will cause both other python files to run as well.Whilst the code is running go over to
    the 'logging_file.log' where you will find a line that provides a link which you are to
    'CTRL + click' on to open up the web page.

    What does each module do?
        Covid_data_handler.py
    
        This module deals with the data side of the project that gets 
        displayed onto the web page - hence its name - and contains a 
        number of different functions that help do this.
        The majority of the module revolves around opening and then pulling 
        data from the csv file named 'nation_2021-10-28.csv'. The data, is then used
        in the the main.py module.
        

        Covid_news_handling.py

        In the news handling module the written python code uses a news API to pull
        news stories mentioning one of three words: "Covid, COVID-19, coronavirus".
        It then takes the url's of each web page's that contains one of the three previously
        mentioned words and then puts them into a list.


        Main.py

        The main module of code forms the web page itself acting as a central place for 
        all infromation gathered in the news and data handling modules. Furthermore,
        the main.py module is responsible for providing the web page link for the user 
        as well as the web page display and the processes ran by the different buttons
        on the page.


DETAILS
    Name - William See
    Github link - https://github.com/Willsee1
    License - Copyright <2021> <William See>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR 
THE USE OR OTHER DEALINGS IN THE SOFTWARE.