from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from time import sleep

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/selectTest.htm')

s1 = driver.find_element_by_id('s4Id')

option1 = Select(s1).options[1]
option2 = Select(s1).options[2]
option3 = Select(s1).options[3]

ActionChains(driver).key_down(Keys.CONTROL).click(option1).key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).click(option2).key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).click(option3).key_up(Keys.CONTROL).perform()

sleep(3)
driver.quit()