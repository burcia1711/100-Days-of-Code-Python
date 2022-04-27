from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/burcualakus/Development/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("http://secure-retreat-92358.herokuapp.com/")

name_input = driver.find_element(By.XPATH, "/html/body/form/input[1]")
name_input.send_keys("Name")
surname_input = driver.find_element(By.XPATH, "/html/body/form/input[2]")
surname_input.send_keys("Surname")
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("name.surname@mail.com")

sign_up_button = driver.find_element(By.XPATH, "/html/body/form/button")
# go_button.click()
sign_up_button.click()

