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
        solution_file_path = curr_prob_path + "/" + pb_char + ".cpp"
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
        solution_file_path = curr_prob_path + "/" + pb_char + ".cpp"
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