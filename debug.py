
# def download_testcases():
#    sample_testcases = "Example\ninput\nCopy\n4\n1\n1\n2\n10\n2\n01\n4\n1010\noutput\nCopy\nYES\nYES\nYES\nNO"
#    textfile = open("input.txt", "w")
#    count = 0
#    for i in sample_testcases: 
#       if count >= 3: 
#          textfile.write(i)
#       if i == '\n':
#          count += 1
#       if i == 'o' and i+1 == 'u' : 
#          break
#          textfile.close()

# download_testcases()

from random import sample


def download_testcases():
   sample_testcases = "Example\ninput\nCopy\n4\n1\n1\n2\n10\n2\n01\n4\n1010\noutput\nCopy\nYES\nYES\nYES\nNO"
   # sample_testcases = driver.find_element(By.XPATH, "//div[@class='sample-tests']").text
   sample_testcases = sample_testcases + "\nabhijayrajvansh"
   arr = []
   
   temp = ""
   for i in sample_testcases:
      if i == '\n':
         arr.append(temp)
         temp = ""
      else:
         temp += i
   print(arr)


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


