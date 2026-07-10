import requests
from twilio.rest import Client
import os


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

 
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(url= STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]
data_list = list(data.values())

yesterday_closing_price = float(data_list[0]["4. close"])
day_before_yesterday_closing_price = float(data_list[1]["4. close"])

price_change = yesterday_closing_price - day_before_yesterday_closing_price
if price_change>=0:
    symbol = "🔺"
else:
    symbol = "🔻"

percentage_change = round((abs(price_change)/day_before_yesterday_closing_price)*100)


if percentage_change>=5:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "language": "en",
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(url= NEWS_ENDPOINT, params= news_params)
    news_response.raise_for_status()
    news = news_response.json()["articles"][:3]
    news_data = [f"{STOCK_NAME}: {symbol}{percentage_change}%\nHeadline: {info['title']}. \nBrief: {str(info['description'])[:40]}."
                  for info in news]



    account_sid = os.environ["ACCOUNT_SID"]
    auth_token = os.environ["AUTH_TOKEN"]


    client = Client(account_sid, auth_token)
    for article in news_data:
        message = client.messages.create(
            body=article,
            from_="+16812756849",
            to=os.environ.get("MY_PHONE_NUMBER"),
        )
        print(message.status)