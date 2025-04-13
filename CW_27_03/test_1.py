from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://suninjuly.github.io/cats.html')

element = driver.find_element(By.XPATH, '//*[@id="bullet"]')
time.sleep(3)
assert element

element2 = driver.find_element(By.XPATH, '//button[text()="View"]')
time.sleep(1)
element2.click()