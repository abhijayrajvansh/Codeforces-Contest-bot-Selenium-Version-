#/
#    author:   abhijayrajvansh
#    created:  16.02.2022 12:42:28
#/
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options #to by-pass chrome broswer notification, and other stuff
from selenium.webdriver.common.by import By
from colorama import Fore
import subprocess
import os
import sys
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
global url
global curr_prob_path


contest_name = sys.argv[1]
url = "https://codeforces.com/contest/" + contest_name
print("Contest url : " + url)

CF_Path = "/Users/abhijayrajvansh/desktop/onlineJudge/codeforces/" + contest_name

try : 
    os.mkdir(CF_Path)
except FileExistsError:
    print("[Looking For Problems Beep.. Boop..]")

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

   counter = 0
   for i in range(len(arr)) :
      if arr[i] == element:
         counter += 1
   return counter

def download_testcases():
   global curr_prob_path

   url = driver.current_url
   # initialising URL as elements into an array list
   pb_arr = []
   for i in url:
      pb_arr.append(i)
   # print(pb_arr)

   pb_char = pb_arr[len(pb_arr) - 1] # initialising character
   if pb_char == '1' or pb_char == '2':
    pb_char = pb_arr[len(pb_arr) - 2] + pb_arr[len(pb_arr) - 1]

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
   no_of_testcases = linear_search(arr, "input")

   curr_prob_path = CF_Path + '/' + pb_char
   try : 
    os.mkdir(curr_prob_path)
   except FileExistsError:
    print("Downloading " + pb_char + "... (Testcases Found: " + f'{Fore.GREEN}',str(no_of_testcases), f'{Fore.WHITE}' + ')')



    if no_of_testcases == 1:
        sample_input_1 = open(curr_prob_path + "/sample_input_1.txt", "w")
        sample_output_1 = open(curr_prob_path + "/sample_output_1.txt", "w")
        #solution file:-
        solution_file_path = curr_prob_path + "/" + pb_char + ".cpp"
        solution_file = open(solution_file_path, "w")
        subprocess.run(["code", solution_file_path])

        array_file = [sample_input_1, sample_output_1]


    if no_of_testcases == 2:
        sample_input_1 = open(curr_prob_path + "/sample_input_1.txt", "w")
        sample_output_1 = open(curr_prob_path + "/sample_output_1.txt", "w")
        sample_input_2 = open(curr_prob_path + "/sample_input_2.txt", "w")
        sample_output_2 = open(curr_prob_path + "/sample_output_2.txt", "w")
        #solution file:-
        solution_file_path = curr_prob_path + "/" + pb_char + ".cpp"
        solution_file = open(solution_file_path, "w")
        subprocess.run(["code", solution_file_path])

        array_file = [sample_input_1, sample_output_1, sample_input_2, sample_output_2]
    

    if no_of_testcases == 3:
      sample_input_1 = open(curr_prob_path + "/sample_input_1.txt", "w")
      sample_output_1 = open(curr_prob_path + "/sample_output_1.txt", "w")
      sample_input_2 = open(curr_prob_path + "/sample_input_2.txt", "w")
      sample_output_2 = open(curr_prob_path + "/sample_output_2.txt", "w")
      sample_input_3 = open(curr_prob_path + "/sample_input_3.txt", "w")
      sample_output_3 = open(curr_prob_path + "/sample_output_3.txt", "w")
      #solution file:-
      solution_file_path = curr_prob_path + "/" + pb_char + ".cpp"
      solution_file = open(solution_file_path, "w")
      subprocess.run(["code", solution_file_path])

      array_file = [sample_input_1, sample_output_1, sample_input_2, sample_output_2, sample_input_3, sample_output_3]


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
        solution_file_path = curr_prob_path + "/" + pb_char + ".cpp"
        solution_file = open(solution_file_path, "w")
        subprocess.run(["code", solution_file_path])

        array_file = [sample_input_1, sample_output_1, sample_input_2, sample_output_2, sample_input_3, sample_output_3, sample_input_4, sample_output_4]
    

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
        solution_file_path = curr_prob_path + "/" + pb_char + ".cpp"
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

def problem_G():
    driver.get(url + "/problem/G")
    download_testcases()
    driver.get(url + "/problem/G1")
    download_testcases()
    driver.get(url + "/problem/G2")
    download_testcases()

def problem_H():
    driver.get(url + "/problem/H")
    download_testcases()
    driver.get(url + "/problem/H1")
    download_testcases()
    driver.get(url + "/problem/H2")
    download_testcases()

problem_A()
problem_B()
problem_C()
problem_D()
problem_E()
problem_F()
problem_G()
problem_H()

dir = CF_Path + '/a'
print("Contest Problem A Dir:⬇\n" + dir)


