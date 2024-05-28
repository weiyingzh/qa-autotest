from selenium import webdriver

from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

input = driver.find_element_by_id('kw')
btn = driver.find_element_by_id('su')

with open('keys.txt') as f:
    lines = f.readlines()
    for line in lines:
        input.send_keys(line)
        btn.click()

        sleep(3)
        input.clear()


