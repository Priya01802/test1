

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.implicitly_wait(3)

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

element=WebDriverWait(driver,10).until(EC.presence_of_element_located(By.XPATH,"//input[@name='username']"))
element.click()

username=driver.find_element(By.NAME,"username")
username.send_keys("Admin")

password=driver.find_element(By.NAME,"password")
password.send_keys("admin123")

loginbutton=driver.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]")
loginbutton.click()

