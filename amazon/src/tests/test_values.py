import os
import sys
import re
import py
import json
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.common.keys import Keys
import attr



        
def test_loop():
    
    
        
        
    items = {"Samsung Widescreen Monitor", "Vizio", "Alexa",
        "hp", "Dell Computers", "Advanced projectors", "Dewalt Power Tools"}
            
            
            
    for i in items:
                
                #Install ChromeDriverManager, open a browser and navigate to Amazon.com
                print('initializing ChromeDriver')
                driver = webdriver.Chrome(ChromeDriverManager().install())
                #Navigate to the URL under test.
                driver.get('https://www.amazon.com')
                # Maximize the browser.
                driver.maximize_window()
                # Enter a product in the search field.
                search = driver.find_element_by_id('twotabsearchtextbox')
                search.send_keys(i)
                search.send_keys(Keys.ENTER)
                product_count = driver.find_element_by_css_selector(
                    '#search > span > div > span > h1 > div > div.sg-col-14-of-20.sg-col.s-breadcrumb.sg-col-10-of-16.sg-col-6-of-12 > div > div > span:nth-child(1)')
                clickable_item = driver.find_element_by_css_selector(
                    "#search > span > div > span > h1 > div > div.sg-col-14-of-20.sg-col.s-breadcrumb.sg-col-10-of-16.sg-col-6-of-12 > div > div > span:nth-child(1)")
                assert(product_count)
                assert(clickable_item)
                driver.close()



