from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()
MY_EMAIL = os.environ["EMAIL_ADDRESS"]
MY_PASSWORD = os.environ["EMAIL_PASSWORD"]

PRODUCT_URL = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",

}


response = requests.get(url=PRODUCT_URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

price = soup.find(name="span", class_="aok-offscreen").getText()
price_as_float = float(price.split("INR")[1].strip().replace(",",""))
product_title = " ".join(soup.find(name="span", id="productTitle").getText().split())

BUY_PRICE = 15000

if price_as_float < BUY_PRICE:
    message = f"{product_title} is on sale for {price}"

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Amazon Price Drop Alert\n\n{message}\n{PRODUCT_URL}".encode("utf-8")
        )
        print("mail sent")
else:
    print(f"Price is not less than {BUY_PRICE}")
