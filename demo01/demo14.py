from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/formTest.htm')

sleep(3)

e1 = driver.find_element_by_name('t1')
e1.send_keys('tom')

sleep(3)

e1.clear()

sleep(3)

e4 = driver.find_element_by_name('textreadonly')

print(e4.get_attribute('readonly'))

e2 = driver.find_element_by_name('textdisabled')

print(e2.is_enabled())

driver.quit()

