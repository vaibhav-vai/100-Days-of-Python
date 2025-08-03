from click import NoSuchOption
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep,time

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://ozh.github.io/cookieclicker/")

#Maximizing the window
driver.maximize_window()

# Wait for page to load just in case
sleep(3)

# Handle initial popups (cookies consent does not have to be clicked, but language does)
print("Looking for Language Selection...")
try:
    language_button = driver.find_element(By.ID, value="langSelect-EN")
    print("Language button found, clicking")
    language_button.click()
    sleep(3)
except NoSuchElementException:
    print("Language selection not found")

# Wait for everything to settle
sleep(2)

# Find the big cookie to click
cookie = driver.find_element(By.ID, value="bigCookie")

# Get all store items (products 0-19)
item_ids = [f"product{i}" for i in range(20)]

# Set timers
wait_time = 10
timeout = time() + wait_time #check for purchases every 5 sec
five_min = time() + 5 * 60 # run for 5 min

while True:
    cookie.click()

    # Every 5 seconds, try to buy the most expensive item we can afford
    if time() > timeout:
        try:
            # Get current cookie count
            cookies_element = driver.find_element(By.ID, value="cookies")
            cookie_text = cookies_element.text

            # Extract number from text like "123 cookies"
            cookie_count = int(cookie_text.split(" ")[0].replace(",",""))

            # Find all available products in the store
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")
            # Find the most expensive item we can afford
            best_item = None
            for product in reversed(products): #Start from most expensive (bottom of list)
                # Check if item is available and affordable (enabled class)
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            # Buy the best item if found
            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute("id")}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie value or items")

        #Reset Timer
        timeout = time() + wait_time

    if time() > five_min:
        try:
            cookies_element = driver.find_element(By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        #break
