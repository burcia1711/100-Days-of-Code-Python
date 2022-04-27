from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/burcualakus/Development/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# driver.get("https://www.amazon.com/dp/B07741S7Y8?pd_rd_w=o7un8&pf_rd_p=a1a3dfab-606d-4be0-8433-474635d71669&pf_rd_r=EGSGKW9669PMYNW4W8N4&pd_rd_r=e58158ad-94b0-44cc-ad8d-307595cb5142&pd_rd_wg=TSVCd")
# price = driver.find_element(by=By.CSS_SELECTOR, value="span.a-offscreen+span")
# print(price.text)

driver.get("https://www.python.org/")
search_bar = driver.find_element(by=By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")
print(logo.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)

link = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[1]/div/ul/li[1]/a')
print(link.text)

driver.quit() 