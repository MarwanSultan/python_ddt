import os
import sys
import re
import py
import json
import pytest
from selenium import webdriver
from multiprocessing.forkserver import main
import random

from faker.providers import BaseProvider


fake = Faker()


class DataProvider(BaseProvider):
    def item_Provider(self):
        products = ["Samsung Widescreen TV", "Vizio", "Alexa", "Dewalt Power Tools"]
        
        return random.choice(products)
    
fake.add_provider(item_Provider)

for i in range(10):
    print(fake.products())

def product_search():
    


        
    for val in val_dict:
            # Install ChromeDriverManager, open a browser and navigate to Amazon.com
            print("initializing ChromeDriver")
            driver = webdriver.Chrome(ChromeDriverManager().install())
            #Navigate to the URL under test.
            driver.get("https://www.amazon.com")
            # Maximize the browser.
            driver.maximize_window()
            # Enter a product in the search field.
            search = driver.find_element_by_id('twotabsearchtextbox')
            obj = json.loads(str(val_dict))
            product = (fake)
            search.send_keys(product)
            search.send_keys(Keys.ENTER)
            product_count = driver.find_element_by_css_selector(
                "#search > span > div > span > h1 > div > div.sg-col-14-of-20.sg-col.s-breadcrumb.sg-col-10-of-16.sg-col-6-of-12 > div > div > span:nth-child(1)")
            clickable_item = driver.find_element_by_css_selector(
                "#search > span > div > span > h1 > div > div.sg-col-14-of-20.sg-col.s-breadcrumb.sg-col-10-of-16.sg-col-6-of-12 > div > div > span:nth-child(1)")
            assert(product_count)
            assert(clickable_item)
            driver.close()
            return driver
product_search()