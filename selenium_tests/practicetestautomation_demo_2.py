from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import csv
import time

def enter_values_in_to_fields(driver, username_id, password_id, username_value, password_value):
    username_field = driver.find_element(By.ID, username_id)
    username_field.send_keys(username_value + Keys.ENTER)

    password_field = driver.find_element(By.ID, password_id)
    password_field.send_keys(password_value + Keys.ENTER)

def submit(driver, submit_btn_id, ):
    submit_btn = driver.find_element(By.ID, submit_btn_id)
    submit_btn.click()

def logout(driver):
    try:
        logout_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Log out")
        logout_btn.click()
        print("Log out Passed")
    except:
        print("Log out failed")

def csv_data_transformer(csv_file_path, remove_header):
    transformed_csv = []
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        # Create a reader object
        csv_reader = csv.reader(file)

        # Optional: Skip the header row if your file has one
        if remove_header:
            header = next(csv_reader)

        # Iterate through the rows
        for row in csv_reader:
            # print(row)  # Each row is a list, e.g., ['John', '30', 'New York']
            transformed_csv.append(row)

        return transformed_csv


# ========================================================================

if __name__ == "__main__":
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get("https://practicetestautomation.com/practice-test-login/")

    username_id = "username"
    password_id = "password"
    submit_btn_id = "submit"

    transformed_csv = csv_data_transformer("./datasets/sample1.csv", True)
    # print(transformed_csv)
    for data in transformed_csv:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, username_id))
        )
        print(data)
        enter_values_in_to_fields(driver, username_id, password_id, data[1], data[2])
        submit(driver, submit_btn_id)
        logout(driver)
        print(f"Row {data[0]} Done!")
        time.sleep(3)

    time.sleep(2)
    # To have little delay

    driver.quit()
    # Quit the opened chrome