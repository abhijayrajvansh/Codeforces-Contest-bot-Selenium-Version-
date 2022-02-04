# data = "Example\ninput\nCopy\n4\n1\n1\n2\n10\n2\n01\n4\n1010\noutput\nCopy\nYES\nYES\nYES\nNO"
import requests
from bs4 import BeautifulSoup

url = 'https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster' #sample url

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Creating empty lists to hold the heights in inches and original scraped heights
height_inches = []
height_list = []

heights = soup.find_all('span', class_= "sidearm-roster-player-height")
heights = "Example\ninput\nCopy\n4\n1\n1\n2\n10\n2\n01\n4\n1010\noutput\nCopy\nYES\nYES\nYES\nNO"
print(heights)

# For some reason, the 23 heights printed twice, hence -23 from the length
for i in range(0, (len(heights)-23)):
  {
      print(heights[i].get_text())
  }
# ^This line of code allows me to see all the heights in a normal list^

#Trying to append the newly found heights in a list
height_list.append(heights[0])
print(height_list)