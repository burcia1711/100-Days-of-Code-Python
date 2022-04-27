from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import time, sleep

timeout = time() + 5
five_min = time() + 60 * 5

chrome_driver_path = "/Users/burcualakus/Development/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by=By.ID, value="cookie")


def money_exchange():
    sleep(0.05)
    money = driver.find_element(by=By.ID, value="money")
    if "," not in money.text:
        return int(money.text)
    else:
        return int(money.text.replace(",", ""))


def buy():
    store = driver.find_elements(by=By.CSS_SELECTOR, value="#rightPanel div#store div b")
    reversed_store = store[::-1]
    for item in reversed_store:
        new_text = item.text.split("-")
        if len(new_text) != 1:
            cleaned = int(new_text[1].strip().replace(",", ""))
            if money_exchange() >= cleaned:
                item.click()
                break


while True:
    cookie.click()
    if time() >= timeout:
        buy()
        timeout = time() + 5
    if time() > five_min:
        break

cps = driver.find_element(by=By.ID, value="cps")
print(cps.text)
