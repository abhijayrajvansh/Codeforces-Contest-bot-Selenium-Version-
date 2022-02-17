#/
#    author:   abhijayrajvansh
#    created:  17.02.2022 12:55:55
#/
from curses.ascii import isalpha
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options #to by-pass chrome broswer notification, and other stuff
from selenium.webdriver.common.by import By
from colorama import Fore
import subprocess
import os
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

url = input("Enter The Problem URL : ")

pwd = os.getcwd()
PATH = Service(pwd + "/chromedriver")

# Handling Chrome Window with Options:
chromeOptions = Options()
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-notifications") # chromeOptions.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 2 }) 

# driver setup:
driver = webdriver.Chrome(service = PATH, options = chromeOptions) # driver.maximize_window() driver.minimize_window()
driver.minimize_window()
driver.get(url) # launches the broswer and open url

pb_name = ""

problem_name_data = driver.find_element(By.CLASS_NAME, "title").text
# print(problem_name_data)
for char in problem_name_data:
   if char == " ":
      pb_name += '-'
   elif char.isalpha():
      pb_name += char

# print(pb_name)
CF_Path = "/Users/abhijayrajvansh/desktop/onlineJudge/codeforces/upsolve/" + pb_name

#directory creation
try : 
   os.mkdir(CF_Path)
except FileExistsError:
   print("[Looking For Problems Beep.. Boop..]")

#global path
curr_prob_path = CF_Path

def linear_search (arr, element):

   counter = 0
   for i in range(len(arr)) :
      if arr[i] == element:
         counter += 1
   return counter
   
def download_testcases():

   url = driver.current_url
   # initialising URL as elements into an array list
   pb_url_arr = []
   for i in url:
      pb_url_arr.append(i)
   pb_char = pb_url_arr[len(pb_url_arr) - 1]
   print("Problem No. : " + pb_char)

   # scrapped sample testcases with garbage texts
   sample_testcases = driver.find_element(By.XPATH, "//div[@class='sample-tests']").text
   sample_testcases = sample_testcases + "\nabhijayrajvansh"
   # print()
   # print(sample_testcases)

   # initialising scrapped data testcases into an array list
   arr = []
   temp = ""
   for i in sample_testcases:
      if i == '\n':
         arr.append(temp)
         temp = ""
      else:
         temp += i
   no_of_testcases = linear_search(arr, "input")
   print("Downloading... (Testcases Found:" + f'{Fore.GREEN}',str(no_of_testcases),f'{Fore.WHITE})')

   if no_of_testcases == 4:
      sample_input_1 = open(curr_prob_path + "/sample_input_1.txt", "w")
      sample_output_1 = open(curr_prob_path + "/sample_output_1.txt", "w")
      sample_input_2 = open(curr_prob_path + "/sample_input_2.txt", "w")
      sample_output_2 = open(curr_prob_path + "/sample_output_2.txt", "w")
      sample_input_3 = open(curr_prob_path + "/sample_input_3.txt", "w")
      sample_output_3 = open(curr_prob_path + "/sample_output_3.txt", "w")
      sample_input_4 = open(curr_prob_path + "/sample_input_4.txt", "w")
      sample_output_4 = open(curr_prob_path + "/sample_output_4.txt", "w")

      #solution file:-
      solution_file_path = curr_prob_path + "/" + "main.cpp"
      solution_file = open(solution_file_path, "w")
      subprocess.run(["code", solution_file_path])

      array_file = [sample_input_1, sample_output_1, sample_input_2, sample_output_2, sample_input_3, sample_output_3, sample_input_4, sample_output_4]

      n = len(arr)
      file_num = -1
      i = 0
      while True:       
         if i == n:
            break

         if arr[i] == "input" or arr[i] == "output":
            i += 2
            file_num += 1
         
         if file_num >= 0:
            array_file[file_num].write(arr[i] + '\n')

         i += 1

   if no_of_testcases == 5:
      sample_input_1 = open(curr_prob_path + "/sample_input_1.txt", "w")
      sample_output_1 = open(curr_prob_path + "/sample_output_1.txt", "w")
      sample_input_2 = open(curr_prob_path + "/sample_input_2.txt", "w")
      sample_output_2 = open(curr_prob_path + "/sample_output_2.txt", "w")
      sample_input_3 = open(curr_prob_path + "/sample_input_3.txt", "w")
      sample_output_3 = open(curr_prob_path + "/sample_output_3.txt", "w")
      sample_input_4 = open(curr_prob_path + "/sample_input_4.txt", "w")
      sample_output_4 = open(curr_prob_path + "/sample_output_4.txt", "w")
      sample_input_5 = open(curr_prob_path + "/sample_input_5.txt", "w")
      sample_output_5 = open(curr_prob_path + "/sample_output_5.txt", "w")

      #solution file:-
      solution_file_path = curr_prob_path + "/" + "main.cpp"
      solution_file = open(solution_file_path, "w")
      subprocess.run(["code", solution_file_path])

      array_file = [sample_input_1, sample_output_1, sample_input_2, sample_output_2, sample_input_3, sample_output_3, sample_input_4, sample_output_4, sample_input_5, sample_output_5]

      n = len(arr)
      file_num = -1
      i = 0
      while True:       
         if i == n:
            break

         if arr[i] == "input" or arr[i] == "output":
            i += 2
            file_num += 1
         
         if file_num >= 0:
            array_file[file_num].write(arr[i] + '\n')

         i += 1

   if no_of_testcases == 3:
      sample_input_1 = open(curr_prob_path + "/sample_input_1.txt", "w")
      sample_output_1 = open(curr_prob_path + "/sample_output_1.txt", "w")
      sample_input_2 = open(curr_prob_path + "/sample_input_2.txt", "w")

      sample_output_2 = open(curr_prob_path + "/sample_output_2.txt", "w")
      sample_input_3 = open(curr_prob_path + "/sample_input_3.txt", "w")
      sample_output_3 = open(curr_prob_path + "/sample_output_3.txt", "w")
      
      #solution file:-
      solution_file_path = curr_prob_path + "/" + "main.cpp"
      solution_file = open(solution_file_path, "w")
      subprocess.run(["code", solution_file_path])

      array_file = [sample_input_1, sample_output_1, sample_input_2, sample_output_2, sample_input_3, sample_output_3]

      n = len(arr)
      file_num = -1
      i = 0
      while True:       
         if i == n:
            break

         if arr[i] == "input" or arr[i] == "output":
            i += 2
            file_num += 1
         
         if file_num >= 0:
            array_file[file_num].write(arr[i] + '\n')

         i += 1

   if no_of_testcases == 2:
      sample_input_1 = open(curr_prob_path + "/sample_input_1.txt", "w")
      sample_output_1 = open(curr_prob_path + "/sample_output_1.txt", "w")

      sample_input_2 = open(curr_prob_path + "/sample_input_2.txt", "w")
      sample_output_2 = open(curr_prob_path + "/sample_output_2.txt", "w")

      #solution file:-
      solution_file_path = curr_prob_path + "/" + "main.cpp"
      solution_file = open(solution_file_path, "w")
      subprocess.run(["code", solution_file_path])

      array_file = [sample_input_1, sample_output_1, sample_input_2, sample_output_2]

      n = len(arr)
      file_num = -1
      i = 0
      while True:       
         if i == n:
            break

         if arr[i] == "input" or arr[i] == "output":
            i += 2
            file_num += 1
         
         if file_num >= 0:
            array_file[file_num].write(arr[i] + '\n')

         i += 1


   if no_of_testcases == 1:
      sample_input_1 = open(curr_prob_path + "/sample_input_1.txt", "w")
      sample_output_1 = open(curr_prob_path + "/sample_output_1.txt", "w")

      #solution file:-
      solution_file_path = curr_prob_path + "/" + "main.cpp"
      solution_file = open(solution_file_path, "w")
      subprocess.run(["code", solution_file_path])

      array_file = [sample_input_1, sample_output_1]

      n = len(arr)
      file_num = -1
      i = 0
      while True:       
         if i == n:
            break

         if arr[i] == "input" or arr[i] == "output":
            i += 2
            file_num += 1
         
         if file_num >= 0:
            array_file[file_num].write(arr[i] + '\n')

         i += 1

      
download_testcases()
driver.quit()

dir = CF_Path 
print("Contest Problem A Dir: " + dir)