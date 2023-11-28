from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging
import os

logging.basicConfig(level=logging.INFO)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", False)

chrome_options.binary_location = os.path.join(os.getcwd(), r"chrome-win64\chrome.exe")
# print(chrome_options.binary_location)
service = Service(executable_path=os.path.join(os.getcwd(), r"chromedriver-win64\chromedriver.exe")) 
# Webpage URL
webpage_url = r'https://developer-console-tutkint.kalayservice.com'
driver = webdriver.Chrome(service=service, options=chrome_options)# chrome_options are deprecated

driver.get("https://www.goopi.co/")

icon = driver.find_element(By.XPATH, f"//button[@type='submit']")
logging.info("Found icon")

actions = ActionChains(driver)
actions.move_to_element(icon).perform()

try:
    # comment: 
    search_input = driver.find_element(By.XPATH, f"//input[@placeholder='找商品']")
    logging.info("Found search input")
    search_input.send_keys("ABCD")
except Exception as e:
    logging.info("Can't locate search input")
    raise e
# end try

time.sleep(5)


# search_input = driver.find_element(By.XPATH, f'//*[@id="SearchPanel"]/div/input')
# print(search_input)
# search_icon = driver.find_element_by_xpath(//*[@id="shopline-section-header"]/nav[1]/div/div[1]/ul[1]/li[3]/div/form/button/svg/use).click()
# search_button = driver.find_element(By.TAG_NAME, '')
# search_input= driver.find_element(By.TAG_NAME, 'input')
# search_input = search_form.find_element(By.TAG_NAME, 'input')
# search_input.send_keys("G7-TB Type-7 Logo Bomber - Shadow")
# search_input.send_keys(Keys.RETURN)

#search_button.click()

time.sleep(0)