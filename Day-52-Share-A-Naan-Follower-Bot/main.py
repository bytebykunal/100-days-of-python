from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]   
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"
SIMILAR_ACCOUNT = "chefsteps"
WAIT_TIME = 5
SCROLL_COUNT = 6
SCROLL_DELAY = 1

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, WAIT_TIME)
        self.modal = None

    def login(self):
        self.driver.get(url=BASE_URL)
        email_input = self.driver.find_element(By.CSS_SELECTOR, "form input[name='username']")
        email_input.clear()
        email_input.send_keys(USERNAME)

        password_input = self.driver.find_element(By.CSS_SELECTOR, "form input[name='password']")
        password_input.clear()
        password_input.send_keys(PASSWORD)

        login_button = self.driver.find_element(By.CSS_SELECTOR, "form button[type='submit']")
        login_button.click()

        save_info = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button']")))
        save_info.click()

        notification = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[class='naan-popup-dismiss']")))
        notification.click()

    def find_followers(self):
        self.driver.get(f"{BASE_URL}/u/{SIMILAR_ACCOUNT}/followers")

        self.modal = self.driver.find_element(By.CSS_SELECTOR, '.followers-scroll')

        time.sleep(2)
        for _ in range(SCROLL_COUNT):
            self.driver.execute_script("arguments[0].scrollTop += arguments[0].scrollHeight;", self.modal)
            time.sleep(SCROLL_DELAY)

    def follow(self):
        rows = self.modal.find_elements(By.CSS_SELECTOR, 'div .naan-follower-row')
        for row in rows:
            try:
                row.find_element(By.TAG_NAME, "button").click()
                time.sleep(1)
            except ElementClickInterceptedException:
                unfollow_popup = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Unfollow']")))
                cancel_button = unfollow_popup.find_element(By.CSS_SELECTOR, "button[class='naan-unfollow-cancel']")
                cancel_button.click()
            except NoSuchElementException:
                pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

bot.driver.quit()
