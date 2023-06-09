#
#
#
# This file have more settings for scraper's firefox browser

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
#
#
def configured_driver(): 
    """ This function configure webdriver! """

    # set driver;
    options = webdriver.FirefoxOptions()

    # with this argument, browser work in background
    #options.add_argument('-headless')

    # set random user Agent
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0") 

    # disable notifications from site, but not popups
    # options.add_argument("--disable-notifications")

    options.add_argument('--no-sandbox')
    options.add_argument('--start-maximized')
    options.add_argument("--incognito")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.set_capability('useAutomationExtension', False)
    options.set_capability("excludeSwitches", ["enable-automation"])
    #options.add_argument("disable-infobars")

    # set path to firefox driver;
    firefox_service = Service(executable_path="/home/linuxtramp/Documents/Python3_projects/SocialMedia_Scraper/Firefox_Driver/geckodriver")
    driver = webdriver.Firefox(service=firefox_service, options=options)

    return driver

