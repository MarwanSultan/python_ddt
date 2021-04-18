import os
import sys
import json
import pytest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from webdriver_manager import driver
from _pytest import unittest
from multiprocessing.forkserver import main

with open("C:/Users/marwa/python/amazon/tests/data/values.json", 'r') as f:
        val_dict = json.load(f)

class Amazon:
    
    
    def test_search():
        
        for val in val_dict['prod_dict']:
            # Install ChromeDriverManager, open a browser and navigate to Amazon.com
            print("initializing ChromeDriver")
            driver = webdriver.Chrome(ChromeDriverManager().install())
            #Navigate to the URL under test.
            driver.get("https://www.amazon.com")
            # Maximize the browser.
            driver.maximize_window()
            # Enter a product in the search field.
            search = driver.find_element_by_id('twotabsearchtextbox')
            search.send_keys(val['product'])
            search.send_keys(Keys.ENTER)
            product_count = driver.find_element_by_css_selector(
                "#search > span > div > span > h1 > div > div.sg-col-14-of-20.sg-col.s-breadcrumb.sg-col-10-of-16.sg-col-6-of-12 > div > div > span:nth-child(1)")
            clickable_item = driver.find_element_by_css_selector(
                "#search > span > div > span > h1 > div > div.sg-col-14-of-20.sg-col.s-breadcrumb.sg-col-10-of-16.sg-col-6-of-12 > div > div > span:nth-child(1)")

            assert(product_count)
            assert(clickable_item)
            driver.close()
            return driver

        if __name__ == '__main__':
            test_search()
