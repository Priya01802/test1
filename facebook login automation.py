import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('https://www.facebook.com/')

time.sleep(5)

Name=driver.find_element(By.NAME,"email")
Name.send_keys(7008897587)

Password=driver.find_element(By.NAME,"pass")
Password.send_keys("Priya@7377")

Loginbutton=driver.find_element(By.NAME,"login")
Loginbutton.click()

time.sleep(10)
driver.close()