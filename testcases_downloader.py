from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options #to by-pass chrome broswer notification, and other stuff
from selenium.webdriver.common.by import By
import os

url = input("Enter The URL : ")

pwd = os.getcwd()
PATH = Service(pwd + "/chromedriver")

# Handling Chrome Window with Options:
chromeOptions = Options()
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-notifications") # chromeOptions.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 2 }) 

# driver setup:
driver = webdriver.Chrome(service = PATH, options = chromeOptions) # driver.maximize_window() driver.minimize_window()
driver.get(url) # launches the broswer and open url

def download_testcases():

   

   sample_testcases = driver.find_element(By.XPATH, "//div[@class='sample-tests']").text
   sample_testcases = sample_testcases + "\nabhijayrajvansh"
   arr = []
   
   temp = ""
   for i in sample_testcases:
      if i == '\n':
         arr.append(temp)
         temp = ""
      else:
         temp += i
   # print(arr)
   inputfile = open("input.txt", "w")
   outputfile = open("output.txt", "w")

   n = len(arr) 
   i = 3
   while True:
      if arr[i] == "output":
         break
      inputfile.write(arr[i] + '\n')
      i += 1

   j = i + 2
   while j < n:
      outputfile.write(arr[j] + '\n')
      j += 1
   
download_testcases()


