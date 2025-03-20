from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://itcareerhub.de/ru")
driver.refresh()

driver.get("https://www.berlin.de")
driver.back()
time.sleep(5)

driver.quit()