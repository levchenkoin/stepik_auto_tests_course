from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button = browser.find_element(By.ID, "book")    
    button.click()


    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_xpath('//input[@id="answer"]')
    input1.send_keys(y)
    
    ...

    # Отправляем заполненную форму
    button1 = browser.find_element(By.ID, "solve")
    button1.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    
    print(browser.switch_to.alert.text)
    
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла
