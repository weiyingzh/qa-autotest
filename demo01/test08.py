from selenium import webdriver

from time import sleep

driver = webdriver.Chrome()
driver.get('http:/www.baidu.com')

e = driver.find_element_by_xpath('//*[@id="kw"]')


e.send_keys('hello')

sleep(2)

btn = driver.find_element_by_xpath('//*[@id="su"]').click()