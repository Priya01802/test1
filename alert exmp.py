import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('https://chercher.tech/practice/practice-pop-ups-selenium-webdriver')

simplealert=driver.find_element(By.XPATH,"//input[@name='alert']")
simplealert.click()

alt=driver.switch_to.alert
alt.accept()
time.sleep(3)

confirmationbox=driver.find_element(By.XPATH,"//input[@name='confirmation']")
confirmationbox.click()
conf=driver.switch_to.alert
conf.accept()

time.sleep(3)

prompt=driver.find_element(By.XPATH,"//input[@name='prompt']")
prompt.click()

pmp=driver.switch_to.alert
pmp.accept()

time.sleep(5)
driver.close()