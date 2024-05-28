from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get(r'C:\Users\ghz\Desktop\selenium\demo01\index2.html')

sleep(3)

a = driver.find_element_by_tag_name('a')

ActionChains(driver).move_to_element(a).perform()

sleep(3)