from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://suninjuly.github.io/cats.html')

element = driver.find_element(By.XPATH, '//*[@class="card mb-4 box-shadow"]')
element.find_element(By.XPATH, '//button[text()="View"]').click()

time.sleep(3)
assert element