from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

PROMISED_DOWN = 1000
PROMISED_UP = 1000
Y_EMAIL = os.environ["Y_EMAIL"]
Y_PASSWORD = os.environ["Y_PASSWORD"]
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 60)
        self.down = None
        self.up = None

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        go_button = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label^='start speed test']")
        go_button.click()

        
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//span[normalize-space()='Result ID']/following-sibling::a")))
        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3').text)
        self.up = float(self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3').text)
        

    def tweet_at_provider(self):
        self.driver.get(url=Y_LOGIN_URL)
        #login
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        email_input.clear()
        email_input.send_keys(Y_EMAIL)
        password_input.clear()
        password_input.send_keys(Y_PASSWORD)
        login_button = self.driver.find_element(By.CSS_SELECTOR, "form button")
        login_button.click()

        #sending tweet
        tweet_input = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "div[id='tweet-compose']")))
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?!"
        tweet_input.clear()
        tweet_input.send_keys(tweet)
        post_button = self.driver.find_element(By.ID, "post-btn")
        post_button.click()

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
print(f"down: {bot.down}")
print(f"up: {bot.up}")
if bot.down<PROMISED_DOWN or bot.up<PROMISED_UP:
    bot.tweet_at_provider()

bot.driver.quit()