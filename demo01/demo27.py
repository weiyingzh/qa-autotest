from selenium import webdriver
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

action = ActionChains(driver)