import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1348028')

time.sleep(5)

email=driver.find_element(By.XPATH,"//input[@id='email']")

act=ActionChains(driver)

act.click(email).key_down(Keys.SHIFT).send_keys("hello").perform()

time.sleep(3)
driver.quit()

