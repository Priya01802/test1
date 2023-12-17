import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('https://automationexercise.com/contact_us')

time.sleep(3)

Name=driver.find_element(By.NAME,"name")
Name.send_keys("Priyaranjan")

Email=driver.find_element(By.NAME,"email")
Email.send_keys("lipunp1234@gmail.com")

Subject=driver.find_element(By.NAME,"subject")
Subject.send_keys("details")

yourmessage=driver.find_element(By.ID,"message")
yourmessage.send_keys("hey there")


submitbutton=driver.find_element(By.NAME,"submit")
submitbutton.click()



