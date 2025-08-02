from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

headers =  {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
  }

static_url = "https://appbrewery.github.io/instant_pot/"
active_url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
response = requests.get(active_url, headers=headers)
amazon_webpage = response.text

soup = BeautifulSoup(amazon_webpage, "html.parser")

price = soup.find( class_="a-offscreen").getText()

price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").getText().strip()
print(title)

BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}"
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"]) as connection:
        connection.starttls()
        connection.login(user=os.environ["MY_EMAIL"], password=os.environ["MY_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["MY_EMAIL"],
            to_addrs=os.environ["MY_EMAIL"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{active_url}".encode("utf-8")
        )