from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = " http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('//input/*[@name="first_name"]')
    input1.send_keys("a")
    input2 = browser.find_element_by_xpath('//input/*[@name="last_name"]')
    input2.send_keys("a")
    input3 = browser.find_element_by_xpath('//input/*[@class="city"]')
    input3.send_keys("a")
    input4 = browser.find_element_by_xpath('//input/*[@id="country"]')
    input4.send_keys("a")
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
