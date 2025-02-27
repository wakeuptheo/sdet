from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice-automation.com/form-fields/")
driver.quit()
