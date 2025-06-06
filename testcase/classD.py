import time
from selenium import webdriver
import pytest
import allure_pytest

# 指定 ChromeDriver 的路径
driver_path = '../venv/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

# 打开网页并进行操作
driver.get("https://www.example.com")

time.sleep(10)

print(driver.title)
driver.quit()
