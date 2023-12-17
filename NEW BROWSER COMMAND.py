from selenium import webdriver


option = webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()

driver.get('https://www.ossc.gov.in/Public/Pages/Login.aspx/')
#string
title =driver.title
print(title)

pagesource=driver.page_source
print(pagesource)

currenturl=driver.current_url
print(currenturl)

driver.close()