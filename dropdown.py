import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import select

option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/dropdown')

time.sleep(5)

dropdown=driver.find_element(By.XPATH,"//select[@id='dropdown']")

sel=Select(dropdown)


#SELECT BY VISIBLE TEXT
sel.Select_by_visible_text("option2")

#SELECT BY INDEX
sel.Select_by_index(1)

#SELECT BY VALUE
sel.Select_by_value("2")

