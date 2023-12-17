import time

from selenium import webdriver
from selenium.webdriver.common.by import By


option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/tables')

time.sleep(5)

table=driver.find_element(By.XPATH,"//table[@id='table1']")

rows=driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr")

print(rows)

cols=driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr/td")

print(rows)

celldata=driver.find_element(By.XPATH,"//table[@id='table1']/tbody/tr[2]/td[3]")

text=celldata.text

print(text)
