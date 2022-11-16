from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

import math
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)


input1 = browser.find_element(By.ID, "answer")

input1.send_keys(y)

option1=browser.find_element(By.CLASS_NAME,"form-check-input")
option1.click()

option2=browser.find_element(By.ID, "robotsRule")
option2.click()

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()

time.sleep(30)
browser.quit()