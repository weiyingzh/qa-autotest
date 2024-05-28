from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get(r'C:\Users\ghz\Desktop\selenium\demo01\index.html')
sleep(3)

btn = driver.find_element_by_id('alert')

btn.click()

sleep(3)

a = driver.switch_to.alert
print(a.text)

a.accept()

sleep(3)

driver.quit()


