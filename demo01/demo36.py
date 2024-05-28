from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get('https://jqueryui.com/droppable/')

sleep(3)

driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="content"]/iframe'))

div1 = driver.find_element_by_id('draggable')
div2 = driver.find_element_by_id('droppable')

ActionChains(driver).drag_and_drop(div1, div2).perform()

sleep(3)