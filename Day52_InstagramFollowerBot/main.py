from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time

SIMILAR_ACCOUNT = "chefsteps"
USERNAME = "lionel.messi020520251"
PASSWORD = "Instagram@123"

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)


    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4.2)

        username = self.driver.find_element(By.XPATH,
                                            value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        password = self.driver.find_element(By.XPATH,
                                            value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input')

        username.send_keys(USERNAME)
        time.sleep(2.1)
        password.send_keys(PASSWORD)
        time.sleep(2.2)
        password.send_keys(Keys.ENTER)

        time.sleep(4.3)
        # Click "Not now" and ignore Save-login info prompt
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()


    def find_follower(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        time.sleep(5.2)
        modal_xpath = '//*[@id="mount_0_0_O4"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a'
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        time.sleep(2)


    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_follower()
bot.follow()
