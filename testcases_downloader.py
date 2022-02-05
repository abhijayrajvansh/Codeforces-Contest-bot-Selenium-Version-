from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options #to by-pass chrome broswer notification, and other stuff
from selenium.webdriver.common.by import By
# from demo import url
import os

url = input("Enter The Problem URL : ")
url = "https://codeforces.com/problemset/problem/1633/E"

pwd = os.getcwd()
PATH = Service(pwd + "/chromedriver")

# Handling Chrome Window with Options:
chromeOptions = Options()
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-notifications") # chromeOptions.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 2 }) 

# driver setup:
driver = webdriver.Chrome(service = PATH, options = chromeOptions) # driver.maximize_window() driver.minimize_window()
driver.get(url) # launches the broswer and open url

def linear_search (arr, element):

   count = 0
   for i in range(len(arr)) :
      if arr[i] == element:
         count += 1
   return count
   
def download_testcases():

   # initialising URL as elements into an array list
   pb_url_arr = []
   for i in url:
      pb_url_arr.append(i)
   pb_char = pb_url_arr[len(pb_url_arr) - 1]
   print("Problem No. : " + pb_char)

   
   # scrapped sample testcases with garbage texts
   sample_testcases = driver.find_element(By.XPATH, "//div[@class='sample-tests']").text
   sample_testcases = sample_testcases + "\nabhijayrajvansh"
   print()
   print(sample_testcases)


   # initialising scrapped data testcases into an array list
   arr = []
   temp = ""
   for i in sample_testcases:
      if i == '\n':
         arr.append(temp)
         temp = ""
      else:
         temp += i
   print('\n')
   print(arr) 

   # Counting no. of testcases
   no_of_testcases = linear_search(arr, "input")
   print("\nTotal no of testcases : " + str(no_of_testcases) + '\n')

   
   # creating input & output files
   files = []
   for i in range(1, no_of_testcases + 1):
      print(i)
      
      


   


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



