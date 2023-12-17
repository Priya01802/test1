from selenium import webdriver


option = webdriver.EdgeOptions()
driver=webdriver.Edge(options=option)
driver.maximize_window()

#DRIVER.GET
driver.get('https://www.selenium.dev/')

#DRIVER.TITLE-STRING
title=driver.title
print(title)

#DRIVER.PAGESOURCE-STRING
pagesource=driver.page_source
print(pagesource)

#DRIVER.CURRENTURL-STRING
currenturl=driver.current_url
print(currenturl)

#DRIVER.CLOSE
driver.close()