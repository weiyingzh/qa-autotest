'''
1.driver.name
2.driver.current_url
3.driver.title
4.driver.page_source
5.driver.current_window_handle
6.driver.window_handles
'''

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
print(driver.name)
print(driver.title)
print(driver.page_source)
print(driver.current_url)
print(driver.current_window_handle)
print(driver.window_handles)