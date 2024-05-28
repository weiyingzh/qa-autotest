from selenium import webdriver
from time import sleep
webdriver = webdriver.Chrome()

webdriver.get('https://github.com/login')

sleep(2)

username_input = webdriver.find_element_by_id('login_field')
pwd_input = webdriver.find_element_by_id('password')

btn = webdriver.find_element_by_name('commit')

username_input.send_keys('524060020@qq.com')
pwd_input.send_keys('guohongzhi123')

sleep(2)

btn.click()





