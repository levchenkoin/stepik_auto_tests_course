from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_value = browser.find_element_by_xpath('//img[@id="treasure"]')
    x = x_value.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element_by_xpath('//input[@id="answer"]')
    input1.send_keys(y)
    
    input2 = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
    input2.click()
    input3 = browser.find_element_by_xpath('//input[@id="robotsRule"]')
    input3.click()
    ...

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # dreams come truth 
