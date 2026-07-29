import requests
from bs4 import BeautifulSoup
from data_storing_bot import DataStoringBot

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeXEMQwgH96j0xVIvmox18Siq0opZxNPcniqeCHcyMYkfg_YQ/viewform?usp=publish-editor"
zillow_clone_url = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(url=zillow_clone_url)
content = response.text

soup = BeautifulSoup(content, 'html.parser')

link_list = soup.select(selector="a.property-card-link")
link_list = [link.get("href") for link in link_list]

price_list = soup.select(selector="span[data-test='property-card-price']")
price_list = [price.get_text().strip().split('+')[0].split('/')[0] for price in price_list ]

address_list = soup.find_all(name="address")
address_list = [address.get_text().strip().replace('|', ',') for address in address_list]

bot = DataStoringBot()

for i in range(len(link_list)):
    bot.add_data(address_list[i], price_list[i], link_list[i])

bot.driver.quit()
