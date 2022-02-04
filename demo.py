#/
#    author:   abhijayrajvansh
#    created:  05.02.2022 01:49:50
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
url = input("Enter The Codeforces Contest Link : ")
# url = "https://codeforces.com/contest/1632/"

contest_name = ""
for char in url:
   if char.isdigit():
      contest_name += char
print("Contest No. : " + contest_name)

CF_Path = "/Users/abhijayrajvansh/desktop/onlineJudge/codeforces/" + contest_name

try : 
    os.mkdir(CF_Path)
except FileExistsError:
    print("Downloading TestCases...")

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

   url = driver.current_url
   pb_arr = []
   for i in url:
      pb_arr.append(i)

#    print(pb_arr)
   pb_char = pb_arr[len(pb_arr) - 1]
   

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

   curr_prob_path = CF_Path + '/' + pb_char
   try : 
    os.mkdir(curr_prob_path)
   except FileExistsError:
    print("Downloading TestCases...")

   inputfile = open(curr_prob_path + "/input.txt", "w")
   outputfile = open(curr_prob_path + "/output.txt", "w")

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

