import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/checkboxes')

driver.get_screenshot_as_file("C:\\Users\\lipun\\PycharmProjects\\seleniumproject2\\screenshot\\file.png")
