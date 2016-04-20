#!usr/bin/env python
# Author: Malabika Sen

import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


display = ' '.join(sys.argv[1:])
search = '+'.join(sys.argv[1:])

print display, "!"
print "\nThat's a nice song! Playing right away!"

browser = webdriver.Firefox()
browser.maximize_window()

url = "https://www.youtube.com/results?search_query=" + search 

browser.get(url)
browser.implicitly_wait(30)

result1 = browser.find_element_by_class_name("yt-lockup-title ")
result1.click()
