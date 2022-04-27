from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/burcualakus/Development/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
english_article_numbers = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(english_article_numbers.text)
# click_link = driver.find_element(by=By.LINK_TEXT, value="Wikibooks")
# click_link.click()

search_bar = driver.find_element(By.NAME, "search")
# go_button = driver.find_element(By.XPATH, "//*[@id='searchButton']")
search_bar.send_keys("Python")
# go_button.click()
search_bar.send_keys(Keys.ENTER)

