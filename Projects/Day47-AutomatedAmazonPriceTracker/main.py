import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

PRODUCT_URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9,tr-TR;q=0.8,tr;q=0.7,en-US;q=0.6",
}
BUY_PRICE = 200
SMTP_ADDRESS = "your smtp address"
EMAIL_ADDRESS = "your email address"
PASSWORD = "your email password"

response = requests.get(PRODUCT_URL, headers=HEADER)
product_web_page = response.content

soup = BeautifulSoup(product_web_page, "lxml")
# print(soup.prettify())

price = soup.find(name="span", class_="a-offscreen").getText()
real_price = price.split("$")[1]
float_real_price = float(real_price)
title = soup.find("span", id="productTitle").get_text().strip()
# print(title)
# print(float_real_price)

if float_real_price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL_ADDRESS, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{PRODUCT_URL}"
        )
