from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get(r'C:\Users\ghz\Desktop\selenium\demo01\index.html')

sleep(3)

driver.find_element_by_id('prompt').click()

sleep(3)

prompt = driver.switch_to.alert

prompt.send_keys('20')

prompt.accept()

sleep(3)