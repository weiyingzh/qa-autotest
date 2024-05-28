from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/formTest.htm')

sleep(3)

input_list = driver.find_elements_by_tag_name('input')

for input in input_list:
    if input.get_attribute('type') == 'checkbox':
        print(input.is_selected())
        if input.get_attribute('value') == 'cv1' or input.get_attribute('value')=='cv3':
            input.click()

sleep(3)

driver.quit()
