from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

import time 
import os 

input1 = browser.find_element(By.NAME, "firstname")
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME,"lastname")
input2.send_keys("Petrov")
input3 = browser.find_element(By.NAME,"email")
input3.send_keys("Smolensk")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt') 
element = browser.find_element(By.NAME,("file"))
element.send_keys(file_path) 
button = browser.find_element(By.CLASS_NAME, "btn")
button.click()


time.sleep(30)
browser.quit()