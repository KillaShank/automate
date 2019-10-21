from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import wget
import os
username=os.environ.get('uname')
password=os.environ.get('password')
driver=webdriver.Chrome()
r=driver.get('https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1#identifier')

driver.find_element_by_id('identifierId').send_keys(username)
ele=driver.find_element_by_class_name('CwaK9')
ele.click()
driver.find_element_by_name('password').send_keys(password)
time.sleep(10)
e=driver.find_element_by_id('CwaK9')
e.click()

try:
    g=driver.find_element_by_link_text('Login to V-TOP')
except:
    print("UNABLE TO LOGIN")
