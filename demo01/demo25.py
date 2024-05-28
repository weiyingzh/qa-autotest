from selenium import webdriver

caps = {}
caps['platform'] = 'WINDOW'
caps['browserName'] = 'chrome'
driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=caps)

driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('hello')


