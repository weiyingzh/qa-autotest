from selenium import webdriver
from selenium.webdriver import ActionChains

from time import sleep

driver = webdriver.Chrome()
driver.get('https://jqueryui.com/droppable/')

driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))

sleep(3)

div1 = driver.find_element_by_id('draggable')

div2 = driver.find_element_by_id('droppable')

ActionChains(driver).drag_and_drop(div1, div2).perform()

sleep(3)

