import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_open_browser(driver):
    driver.get("https://www.example.com")
    heading = driver.find_element(By.TAG_NAME, 'h1').text
    time.sleep(3)
    assert heading == "Example Domain", 'тест не прошел'