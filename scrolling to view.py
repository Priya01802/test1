import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/')

time.sleep(5)

multiplewindow=driver.find_element(By.XPATH,"//a[contains(text(),'Multiple Windows')]")
time.sleep(3)

#SCROLL TILL THE ELEMENT INVISIBLE
#JAVA SCRIPT
#WE CREATE THE OBJECT OF CLASS & USE THE EXECUTE SCRIPT METHOD

driver.execute_script("arguments[0].scrollIntoView()",multiplewindow)

time.sleep(3)
multiplewindow.click()