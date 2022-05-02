from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/burcualakus/Development/chromedriver"
TWITTER_EMAIL = "YOUR TWITTER EMAIL"
TWITTER_PASSWORD = "YOUR TWITTER PASSWORD"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.down = 0
        self.up = 0
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        time.sleep(10)
        go_button = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        go_button.click()

        time.sleep(100)
        self.down = self.driver.find_element(By.CSS_SELECTOR, "#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left > span")
        self.up = self.driver.find_element(By.CSS_SELECTOR, "#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-left > div > div.result-data.u-align-left > span")
        print(self.up)
        print(self.down)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(5)
        enter_space = self.driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div > main > div > div > div > div.css-1dbjc4n.r-6koalj.r-16y2uox > div.css-1dbjc4n.r-16y2uox.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-8w3o46.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu.r-13qz1uu > label > div > div.css-1dbjc4n.r-18u37iz.r-1pi2tsx.r-1wtj0ep.r-u8s1d.r-13qz1uu")
        enter_space.click()
        email = self.driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div > main > div > div > div > div.css-1dbjc4n.r-6koalj.r-16y2uox > div.css-1dbjc4n.r-16y2uox.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-8w3o46.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu.r-13qz1uu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input")
        email.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div > main > div > div > div > div.css-1dbjc4n.r-6koalj.r-16y2uox > div.css-1dbjc4n.r-16y2uox.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-8w3o46.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div:nth-child(6) > div")
        next_button.click()
        password = self.driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div > main > div > div > div > div.css-1dbjc4n.r-6koalj.r-16y2uox > div.css-1dbjc4n.r-16y2uox.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-8w3o46.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-1dbjc4n.r-mk0yit.r-13qz1uu > div > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div.css-901oao.r-1awozwy.r-6koalj.r-37j5jr.r-1inkyih.r-16dba41.r-135wba7.r-bcqeeo.r-13qz1uu.r-qvutc0 > input")
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
