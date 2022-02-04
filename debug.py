from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options #to by-pass chrome broswer notification, and other stuff
from selenium.webdriver.common.by import By
import os

# url = input("Enter The URL : ")
url = "https://codeforces.com/problemset/problem/1633/A"

pwd = os.getcwd()
PATH = Service(pwd + "/chromedriver")

# Handling Chrome Window with Options:
chromeOptions = Options()
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-notifications") # chromeOptions.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 2 }) 

# driver setup:
driver = webdriver.Chrome(service = PATH, options = chromeOptions) # driver.maximize_window() driver.minimize_window()
# driver.get(url) # launches the broswer and open url

pb_arr = []
for i in url:
    pb_arr.append(i)
pb_char = pb_arr[len(pb_arr) - 1]