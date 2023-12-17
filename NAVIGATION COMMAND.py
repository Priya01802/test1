import time

from selenium import webdriver


option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('https://www.selenium.dev/')

time.sleep(10)

#DRIVER.BACK()
driver.back()
time.sleep(3)

#DRIVER.FORWARD
driver.forward()

time.sleep(10)

#DRIVER.REFRESH
driver.refresh()
driver.close()