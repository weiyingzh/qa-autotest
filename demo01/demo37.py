from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/php/fileUpload.htm')

sleep(3)

file = driver.find_element_by_id('file')
file.send_keys(r'C:\Users\ghz\Desktop\test.png')

# print(file.get_attribute('value'))
sleep(3)

driver.find_element_by_xpath('/html/body/form[1]/input[3]').click()

sleep(3)