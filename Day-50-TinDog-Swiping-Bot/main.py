from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
WAIT_TIMEOUT = 2
URL=os.environ["URL"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

wait = WebDriverWait(driver, WAIT_TIMEOUT)
login_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[class*='login']")))
login_button.click()

wait.until(ec.visibility_of_element_located((By.ID, "login-modal")))
facebark_button = driver.find_element(By.CSS_SELECTOR, "button[class*='facebark']")
facebark_button.click()


base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email_input = wait.until(ec.presence_of_element_located((By.ID, "email")))
email_input.send_keys(EMAIL)

password_input = driver.find_element(By.ID, "pass")
password_input.send_keys(PASSWORD)

submit_button = driver.find_element(By.CSS_SELECTOR, "form button")
submit_button.click()

driver.switch_to.window(base_window)

location_button = wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/form/button")))
location_button.click()
notification_button = wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/form/button[2]")))
notification_button.click()
cookie_button = wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/form/button")))
cookie_button.click()

for _ in range(20):
    sleep(1)
    try:
        like_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[class='btn-like']")))
        like_button.click()
    except ElementClickInterceptedException:
        try:
            driver.find_element(By.CSS_SELECTOR, "a[class^='match-popup-']").click()
        except NoSuchElementException:
            sleep(2)
    except NoSuchElementException:
        sleep(2)

driver.quit()