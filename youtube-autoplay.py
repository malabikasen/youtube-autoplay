from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import urllib
from bs4 import BeautifulSoup
import sys

arg = len(sys.argv)
search = ""
display = ""
for x in range(1, arg):
	search += sys.argv[x]
	display += sys.argv[x]
	display += " "
	if (x == arg-1):
		break
	search += "+"

print display + "!"
print "\nThat's a nice song! Playing right away!"
browser = webdriver.Firefox()

url = "https://www.youtube.com/results?search_query=" 
url += search

browser.get(url)

time.sleep(2)


url = browser.current_url
request = urllib.urlopen(url).read()
soup = BeautifulSoup(request)
searchdiv = soup.find_all("div", class_="yt-lockup-dismissable yt-uix-tile") #This is the div class of the search results in YouTube


prefix = "http://youtube.com"
prefix = prefix + searchdiv[0].a["href"] #Get the url of the first search result
browser.get(prefix)
