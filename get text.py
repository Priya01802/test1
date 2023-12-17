import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/notification_message_rendered')

time.sleep(5)

login=driver.find_element(By.XPATH,"//body[1]/div[2]/div[1]/div[1]/p[1]")
textvalue=login.text

print(textvalue)