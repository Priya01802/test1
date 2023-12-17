import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

time.sleep(5)

username=driver.find_element(By.NAME,"username")
username.send_keys("Admin")

password=driver.find_element(By.NAME,"password")
password.send_keys("admin123")

loginbutton=driver.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]")
loginbutton.click()

time.sleep(5)

chk_list=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]")
time.sleep(3)

for i in chk_list:
    i.click()

time.sleep(3)
driver.close()