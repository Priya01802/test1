import time

from selenium import webdriver
from selenium.webdriver.common.by import By


option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('http://www.dummypoint.com/Windows.html')

time.sleep(5)

#GET THE WINDOW HANDLE OF THE PARENT WINDOW
window_name=driver.current_window_handle
print(window_name)

time.sleep(3)

ele=driver.find_element(By.XPATH,"//input[@value='Open a Popup Window']")

ele.click()

#GET THE WINDOW HANDLE OF BOTH THE WINDOWS
windows=driver.window_handles
for window in windows:
    print(window)

driver.switch_to.window(windows[1])
driver.maximize_window()

fr=driver.find_element(By.ID,"f2")
driver.switch_to.frame(fr)

prmt=driver.find_element(By.XPATH,"//button[@name='promtalert']")

prmt.click()

time.sleep(3)