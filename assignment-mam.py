import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

time.sleep(5)

username=driver.find_element(By.NAME,"username")
username.send_keys("Admin")

password=driver.find_element(By.NAME,"password")
password.send_keys("admin123")

loginbutton=driver.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]")
loginbutton.click()
time.sleep(5)

time.sleep(2)
admin=driver.find_element(By.LINK_TEXT,"Admin")
admin.click()
time.sleep(3)

chk_list=driver.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]/i[1]")
for i in chk_list:
    time.sleep(2)
    i.click()
