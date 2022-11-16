from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/execute_script.html"
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
browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
option1.click()

option2=browser.find_element(By.ID, "robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
option2.click()

button = browser.find_element(By.CLASS_NAME, "btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(30)
browser.quit()