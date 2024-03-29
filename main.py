import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

s = Service(executable_path='C:\\Users\\toxidxd\\PycharmProjects\\selenium_vk\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
load_dotenv()

try:
    driver.maximize_window()
    driver.get('https://vk.com')
    time.sleep(5)

    email_input = driver.find_element(By.ID, 'index_email')
    email_input.clear()
    email_input.send_keys(os.getenv('PHONE'))
    email_input.send_keys(Keys.ENTER)
    time.sleep(10)


except Exception as exc:
    print(exc)

finally:
    driver.close()
    driver.quit()
