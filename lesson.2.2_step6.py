from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    y = calc(x)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    input1 = browser.find_element_by_xpath('//input[@id="answer"]')
    input1.send_keys(y)
    
    input2 = browser.find_element_by_xpath('//label[@for="robotCheckbox"]')
    input2.click()
    input3 = browser.find_element_by_xpath('//label[@for="robotsRule"]')
    input3.click()
    ...

    # Отправляем заполненную форму

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
