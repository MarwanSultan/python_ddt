import os
import sys
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


URL = "https://www.amazon.com"




with open('C:/Users/marwa/python/amazon/tests/data/product_data.json') as data_file:
    data = json.load(data_file)



class amazon:

    def search_test(self):


        for i in data['products']:
            # Install ChromeDriverManager, open a browser and navigate to Amazon.com
            driver = webdriver.Chrome(ChromeDriverManager().install())

            driver.get(URL)
            # Maximize the browser.
            driver.maximize_window()
            # Enter a product in the search field.
            search = driver.find_element_by_id('twotabsearchtextbox')
            search.send_keys(i['product'])

            search.send_keys(Keys.ENTER)

            driver.close()


a = amazon()
a.search_test()