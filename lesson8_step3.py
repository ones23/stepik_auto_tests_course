from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

link="http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)

import time 


x_element = browser.find_element(By.ID, "num1")
x = int(x_element.text)
y_element = browser.find_element(By.ID, "num2")
y = int(y_element.text)
z = (x+y)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(z))
submit = browser.find_element(by=By.CSS_SELECTOR, value=".btn.btn-default").click()

time.sleep(30)
browser.quit()