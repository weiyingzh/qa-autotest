from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                          desired_capabilities=DesiredCapabilities.FIREFOX)

driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('hello')
