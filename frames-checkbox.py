import time
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/iframe')

time.sleep(3)

fr=driver.find_element(By.XPATH,"//iframe[@id='mce_0_ifr']")
driver.switch_to.frame(fr)

text=driver.find_element(By.ID,"tinymce")
text.clear()
time.sleep(3)
text.send_keys("Priyaranjan")

time.sleep(2)

