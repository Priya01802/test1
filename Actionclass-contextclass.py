import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/')

time.sleep(5)
act=ActionChains(driver)
checkbox=driver.find_element(By.LINK_TEXT,"Context Menu")
act.context_click(checkbox).perform()
time.sleep(3)