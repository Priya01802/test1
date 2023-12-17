import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('https://www.saucedemo.com/v1//')

time.sleep(3)

username=driver.find_element(By.NAME,"user-name")
username.send_keys("standard_user")

password=driver.find_element(By.NAME,"password")
password.send_keys("secret_sauce")

loginbutton=driver.find_element(By.ID,"login-button")
loginbutton.click()



