#/
#    author:   abhijayrajvansh
#    created:  04.02.2022 12:20:33
#/
from random import sample
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options #to by-pass chrome broswer notification, and other stuff
from selenium.webdriver.common.by import By
import os
import datetime
import time
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
global url
url = input("Enter The Codeforces Contest Link : [Press Return For Default]")
url = "https://codeforces.com/contest/1632/"

pwd = os.getcwd()
PATH = Service(pwd + "/chromedriver")

# Handling Chrome Window with Options:
chromeOptions = Options()
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-notifications") # chromeOptions.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 2 }) 

# driver setup:
driver = webdriver.Chrome(service = PATH, options = chromeOptions) # driver.maximize_window() driver.minimize_window()
driver.get(url) # launches the broswer and open url

def linear_search(data):
    print()

def download_testcases():
    sample_testcases = driver.find_element(By.XPATH, "//div[@class='sample-tests']").text
    io_data = []
    i = 0
    for i in range(0, (len(sample_testcases))):
        io_data.append(sample_testcases[i])
    print(io_data)

def problem_A():
    driver.get(url + "/problem/A")
    download_testcases()
    driver.get(url + "/problem/A1")
    download_testcases()
    driver.get(url + "/problem/A2")
    download_testcases()

def problem_B():
    driver.get(url + "/problem/B")
    download_testcases()
    driver.get(url + "/problem/B1")
    download_testcases()
    driver.get(url + "/problem/B2")
    download_testcases()

def problem_C():
    driver.get(url + "/problem/C")
    download_testcases()
    driver.get(url + "/problem/C1")
    download_testcases()
    driver.get(url + "/problem/C2")
    download_testcases()

def problem_D():
    driver.get(url + "/problem/D")
    download_testcases()
    driver.get(url + "/problem/D1")
    download_testcases()
    driver.get(url + "/problem/D2")
    download_testcases()

def problem_E():
    driver.get(url + "/problem/E")
    download_testcases()
    driver.get(url + "/problem/E1")
    download_testcases()
    driver.get(url + "/problem/E2")
    download_testcases()

def problem_F():
    driver.get(url + "/problem/F")
    download_testcases()
    driver.get(url + "/problem/F1")
    download_testcases()
    driver.get(url + "/problem/F2")
    download_testcases()

def All_Problems():
    problem_A()
    problem_B()
    problem_C()
    problem_D()
    problem_E()
    problem_F()

All_Problems()



