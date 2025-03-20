# Написать скрипт, который:
# Открывает в браузере Firefox https://itcareerhub.de/ru
# Переходит в раздел “Способы оплаты”
# Делает скриншот этой секции страницы

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image

driver = webdriver.Chrome()
driver.get("https://itcareerhub.de/ru")
about_link = driver.find_element(By.LINK_TEXT, 'Способы оплаты')
about_link.click()
time.sleep(5)
#driver.refresh()
driver.save_screenshot('scr/aaa1.png')
time.sleep(5)
driver.quit()