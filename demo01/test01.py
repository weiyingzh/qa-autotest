from selenium import webdriver
from time import sleep

# driver = webdriver.Ie()
# driver = webdriver.Firefox()
driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
driver.get('http://www.baidu.com')
sleep(2)
driver.quit()