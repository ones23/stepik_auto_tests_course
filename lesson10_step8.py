from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

import time

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
button = browser.find_element(By.ID, "book")
button.click()

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

btn = browser.find_element(By.ID, "solve")
btn.click()

time.sleep(30)
browser.quit()