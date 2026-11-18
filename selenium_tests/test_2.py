from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# This can be used wait for the presence for the element before going forward

import time

#Allow to use chrome as a user in the code
#executable pather = path to chrome driver .exe file
service = Service(executable_path="chromedriver.exe")

driver = webdriver.Chrome(service=service)

# Get to this site
driver.get("https://google.com")

WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "gLFyf"))
)
# Use the web driver -> wait for 5 seconds -> Until we locate an element by class name "gLFyf" unless crash
# This will prevent faulty errors due to poor network connections

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
# We are going to uniquely access the particular element by it's class name (Note - use inspect in web browser to find it prior to the testing)
input_element.clear()
# Clear any left out items in  the particular element or maybe used so simpy clean
input_element.send_keys("coding" + Keys.ENTER)
# search something

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Coding")
# By doing this we can find any single link tag / anchor tag if it has similar type of text "coding" or whatever
link.click()

# link = driver.find_element(By.LINK_TEXT, "Coding")
# By doing this we can find any single link tag / anchor tag if it has exact type of text "coding" or whatever
# link.click()

link = driver.find_elements(By.PARTIAL_LINK_TEXT, "Coding")
# By doing this we can find any multiple link tag / anchor tag if it has similar type of text "coding" or whatever
# This will create a list of elements regarding the given conditions and go through them continuously.
# link.click()

time.sleep(10)
# To have little delay

driver.quit()
#Quit the opened chrome
