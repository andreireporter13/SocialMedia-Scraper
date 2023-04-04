#
#
#
# SocialMedia Scraper with Python#(...3...) and Selenium + WebDriver Firefox.
# This script can scrap facebook groups and can notified you if someone posted something 
# ... you interested in.
# ---> This script is for educational purposes!
# 
# test facebook group for this script is ---> https://www.facebook.com/webautomation.romania
#
#
# Author        ---> number_1101
# Website       ---> https://webautomation.ro
# Linkedin      ---> https://www.linkedin.com/in/andrei-cojocaru-985932204/
# Youtube       ---> https://www.youtube.com/channel/UCgx_Y9OHi5KPVzLJo9setxw
# Facebook      ---> https://www.facebook.com/webautomation.romania
#
#
# python packages
from time import sleep
from random import randint
#
# my modules
from browser_settings import configured_driver
#
# installed modules: selenium and all dependencies...
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
import re
#
#
################################################# START CODE HERE #################################################
#
def get_acces_to_facebook(driver) -> None:
    """ 
    This func() get acces to facebook with login and password.
    """
    
    # find cookies button by regex
    regex_data = re.compile(r"^Allow\s(?:essential\s)?and\s(?:optional\s)?cookies$")

    try:
        for button in WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//button"))):
            
            # text from elem
            text = driver.execute_script("return arguments[0].innerHTML;", button)

            if re.search(regex_data, text):
                driver.execute_script("arguments[0].click();", button)
                sleep(0.5)

                break
    
    #            
    except Exception as ex:
        print(ex)

#
#
def main():
    """
    This function store all logic of this project.
    Important section!
    """
    
    # get driver
    driver = configured_driver()

    try: 
        # get first acces to facebook
        driver.get('https://facebook.com')
        driver.maximize_window()

        #acces facebook via bot
        get_acces_to_facebook(driver)

    except Exception as ex:
        print(ex)

    finally: 
        sleep(10)
        driver.quit()
        driver.close()



if __name__ == "__main__":
  main()
