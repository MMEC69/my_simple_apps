from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://practicetestautomation.com/practice-test-login/")

username_id = "username"
password_id = "password"
submit_btn_id = "submit"

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, username_id))
)

username_field = driver.find_element(By.ID, username_id)
username_field.send_keys("student" + Keys.ENTER)

password_field = driver.find_element(By.ID, password_id)
password_field.send_keys("Password123" + Keys.ENTER)

submit_btn = driver.find_element(By.ID, submit_btn_id)
submit_btn.click()


time.sleep(10)
# To have little delay

driver.quit()
#Quit the opened chrome
