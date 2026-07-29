from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeXEMQwgH96j0xVIvmox18Siq0opZxNPcniqeCHcyMYkfg_YQ/viewform?usp=publish-editor"
WAIT_TIME = 5


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class DataStoringBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, WAIT_TIME)

    def add_data(self, address, price, url):
        self.driver.get(url=GOOGLE_FORM_URL)
        address_input = self.wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        price_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

        address_input.send_keys(address)
        price_input.send_keys(price)
        link_input.send_keys(url)

        submit_button = self.driver.find_element(By.CSS_SELECTOR, "div[role='button'][aria-label='Submit']")
        submit_button.click()

