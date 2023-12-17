from selenium import webdriver


option = webdriver.FirefoxOptions()
driver=webdriver.Edge(options=option)
driver.maximize_window()
driver.get('https://www.selenium.dev/')