'''
send_keys()
clear()
click()
get_attribute()
is_selected()
is_enabled()
is_displayed()
value_of_css_property()
'''

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

input = driver.find_element_by_id('kw')

print(input.get_attribute('maxlength'))

print(input.is_displayed())
print(input.is_enabled())
print(input.is_selected())

print(input.value_of_css_property('color'))
print(input.value_of_css_property('font'))

input.send_keys('你好')

sleep(3)

btn = driver.find_element_by_id('su')
btn.click()

sleep(3)

input.clear()

sleep(3)

driver.quit()



