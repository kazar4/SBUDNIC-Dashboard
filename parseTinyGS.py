
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

websiteLink = "https://tinygs.com/station/SBUDNIC_TEST_2@5242050888"

# start web browser
browser = webdriver.Chrome('./chromedriver_mac')

# get source code
browser.get(websiteLink)
#html = browser.find_element_by_xpath("/html/body/div/div/main/div/div[1]/div/div[2]/div[3]").text
#html = browser.find_element_by_class_name("flex xs12 sm12 pa-4")
#print(html)
time.sleep(4)
#nt(by=By.XPATH, value=xpath) instead
html = browser.find_element(by=By.XPATH, value="/html/body/div/div/main/div/div[1]/div/div[2]/div[3]")
html = html.get_attribute('innerHTML')

# close web browser
browser.close()


#html_dump = BeautifulSoup(html, 'html.parser')

#print(r.html.html)

#print(type(r.html.text))
#page_html = req.content
#html_dump = BeautifulSoup(page_html, 'html.parser')

#print(html_dump)

#print(html_dump)

#for divList in html_dump.find_all(".flex xs12 sm12 pa-4"):
#    print(divList)