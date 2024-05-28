from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()

driver.get(r'C:\Users\ghz\Desktop\selenium\demo01\index.html')

sleep(3)

driver.find_element_by_id('confirm').click()

sleep(3)

confirm = driver.switch_to.alert

print(confirm.text)

# confirm.dismiss()

confirm.accept()

print('accept')

sleep(3)

driver.quit()