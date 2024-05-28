from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

ActionChains(driver).key_up(Keys.CONTROL)
ActionChains(driver).key_down(Keys.SHIFT)
