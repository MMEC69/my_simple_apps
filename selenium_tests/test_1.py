from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Allow to use chrome as a user in the code
#executable pather = path to chrome driver .exe file
service = Service(executable_path="chromedriver.exe")

driver = webdriver.Chrome(service=service)

# Get to this site
driver.get("https://google.com")

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
# We are going to uniquely access the particular element by it's class name (Note - use inspect in web browser to find it prior to the testing)
input_element.send_keys("coding" + Keys.ENTER)
# search something

time.sleep(10)
# To have little delay

driver.quit()
#Quit the opened chrome
