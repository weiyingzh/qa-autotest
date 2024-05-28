from selenium import webdriver
from selenium.webdriver import ActionChains

from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

input_element = driver.find_element_by_id('kw')

input_element.send_keys('玩转pycharm 郭宏志 csdn')

btn_element = driver.find_element_by_id('su')

ActionChains(driver).click(btn_element).perform()

sleep(3)

driver.find_element_by_partial_link_text('玩转Pycharm-2-Pycharm').click()

sleep(3)

driver.quit()