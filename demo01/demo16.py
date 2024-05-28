from selenium import webdriver
from time import sleep



driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/formTest.htm')

sleep(3)

radio_list = driver.find_elements_by_name('r1')

for radio in radio_list:
    if radio.get_attribute('value') == 'rv2':
        radio.click()






sleep(4)