from selenium import webdriver


driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# input = driver.find_element_by_css_selector('#kw')

input = driver.find_element_by_css_selector('.s_ipt')

input.send_keys('hello')

btn = driver.find_element_by_css_selector('#su')
btn.click()