from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

#Allow to use chrome as a user in the code
#executable pather = path to chrome driver .exe file
service = Service(executable_path="chromedriver.exe")

driver = webdriver.Chrome(service=service)

# Get to this site
driver.get("https://google.com")

time.sleep(10)
# To have little delay

driver.quit()
#Quit the opened chrome
