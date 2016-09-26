#!usr/bin/env python
# Author: jsnreddy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import urllib
from bs4 import BeautifulSoup
import sys


def playsong(searchinput, webBrowser):
    display = searchinput
    print display + "!"
    print "\nThat's a nice song! Playing right away!"
    # webBrowser = webdriver.Firefox() # no need to create new browser as we are searching in same browser for next song

    url = "https://www.youtube.com/results?search_query="
    url += searchinput

    webBrowser.get(url)
    # webBrowser.maximize_window()

    # time.sleep(2)
    url = webBrowser.current_url
    request = urllib.urlopen(url).read()
    soup = BeautifulSoup(request, "lxml")
    searchdiv = soup.find_all("div",class_="yt-lockup-dismissable yt-uix-tile")  # This is the div class of the search results in YouTube

    prefix = "http://youtube.com"
    prefix = prefix + searchdiv[0].a["href"]  # Get the url of the first search result
    webBrowser.get(prefix)

userInput = raw_input("Enter the song name : ")
search = userInput

if userInput == "exit":	#if the user wants to exit, enter "exit"
	sys.exit()

browserChoice = raw_input("Enter browser : \n 1 - Chrome \n 2 - Firefox \n")
if browserChoice == "1":
    print "You chose Chrome browser"
    browser = webdriver.Chrome()	#add the chrome driver to the path or give the path of the driver as an argument
    browser.maximize_window()
elif browserChoice == "2":
    print "You chose Firefox browser"
    browser = webdriver.Firefox()
    browser.maximize_window()
else:
    print "Enter a valid input"
    sys.exit()

playsong(search, browser)

#This loop is for user to be able to provide the next song in the command line,
#and the song is played in the same tab of the browser with out opening a new tab or a new browser
while 1:
    nextUserInput = raw_input("Enter the next song name : ")
    if nextUserInput == "exit":	#if the user enter "exit" as input, it ends the program
		browser.close()
		break
    playsong(nextUserInput, browser)

sys.exit()