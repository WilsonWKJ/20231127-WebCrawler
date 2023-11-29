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
# webpage_url = r'https://developer-console-tutkint.kalayservice.com'
driver = webdriver.Chrome(service=service, options=chrome_options)# chrome_options are deprecated

driver.get("https://www.goopi.co/products/%E2%80%9Ch-fuel01%E2%80%9D-human-fuel-aquastand-black")
driver.maximize_window()
time.sleep(5)
check_out = driver.find_element(By.XPATH, f"//button[@id='#btn-buy-now']").click()
time.sleep(2)

username_input = driver.find_element(By.XPATH, f"//input[@data-e2e-id='login-email_input']")
username_input = username_input.send_keys('yongshi99934@gmail.com')
password_input = driver.find_element(By.XPATH, f"//input[@data-e2e-id='login-password_input']")
password_input = password_input.send_keys("a3663450")
shop_start = driver.find_element(By.XPATH, f"//button[@id='sign-in-recaptcha']").click()
time.sleep(30)
goto_check = driver.find_element(By.XPATH, f"//a[@data-e2e-id='checkout_button']").click()
#goto_check = driver.find_element(By.CLASS_NAME, 'btn-checkout').click()
time.sleep(3)
customer_profile = driver.find_element(By.ID, "recipient-name")
customer_profile = customer_profile.send_keys("王暄誠")
customer_phone = driver.find_element(By.ID, "recipient-phone")
customer_phone = customer_phone.send_keys("0989130225")
time.sleep(3)
search_711 = driver.find_element(By.CLASS_NAME, "btn-pick-store").click()
time.sleep(3)
store_number = driver.find_element(By.ID, "byID").click()
time.sleep(2)

try:
#   driver.switch_to.default_content()
#   iframe_title = ""
#   iframe = driver.find_element(By.CSS_SELECTOR, f"iframe[id='frmMain']")
#   iframe = driver.find_element(By.CSS_SELECTOR, "iframe")
#   iframe = driver.find_element(By.XPATH, f"//iframe[@id='frmMain']")
#   logging.INFO("found iframe")
#   driver.switch_to.frame(iframe)
#   logging.INFO("switched iframe")
  driver.switch_to.frame(0)
  time.sleep(2)
except:
  print('An exception occurred iframe')
  time.sleep(3)

try:
  store_input_id = driver.find_element(By.XPATH ,f"//input[@id='storeIDKey']")
  time.sleep(1)
except:
  print('An exception occurred')

time.sleep(3)
store_input_id = store_input_id.send_keys("197803")
enter_search = driver.find_element(By.XPATH, f"//button[@id='send']").click()
time.sleep(5)

chooes_store = driver.find_element(By.XPATH, f"//li[@onclick='showMap(197803)']").click()
check_store = driver.find_element(By.ID, "sevenDataBtn").click()
agree = driver.find_element(By.ID, "AcceptBtn").click()
agree = driver.find_element(By.ID, "submit_butn").click()