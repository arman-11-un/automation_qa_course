
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://demoqa.com/checkbox')

# Находим первый элемент
element1 = driver.find_element(By.CSS_SELECTOR,'svg[class="rct-icon rct-icon-check"]')

# Ищем вложенный элемент внутри element1
element = element1.find_element_by_xpath('.//ancestor::span[@class="rct-title"]')