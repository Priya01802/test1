import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/checkboxes')

time.sleep(3)

checkbox2=driver.find_element(By.XPATH,"//body/div[@class='row']/div[@id='content']/div[@class='example']/form[@id='checkboxes']/input[2]")
checkbox2.click()

chk_list=driver.find_elements(By.XPATH,"//form[@id='checkboxes']")
time.sleep(3)
for i in chk_list:
    time.sleep(3)
    i.click()
driver.close()