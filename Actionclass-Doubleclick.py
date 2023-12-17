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

addrem=driver.find_element(By.XPATH,"//a[contains(text(),'Add/Remove Elements')]")
time.sleep(10)

#DOUBLE_CLICK
act.double_click(addrem).perform()

time.sleep(3)


