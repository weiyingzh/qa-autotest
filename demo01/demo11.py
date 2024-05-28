from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

input = driver.find_element_by_id('kw')
input.send_keys('hello')

sleep(3)

btn = driver.find_element_by_id('su')

btn.click()
sleep(3)

driver.refresh()

sleep(3)

driver.back()

sleep(3)

# driver.switch_to.

driver.quit()

