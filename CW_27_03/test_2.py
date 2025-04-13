from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://suninjuly.github.io/cats.html')
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@class="card mb-4 box-shadow"]')
assert element
buttons = element.find_elements(By.XPATH, '//button[text()="View"]')
for button in buttons:
    time.sleep(1)
    button.click()
driver.quit()