from selenium import webdriver

from time import sleep

# options = webdriver.ChromeOptions()

options = webdriver.FirefoxOptions()
options.add_argument('--headless')

# driver = webdriver.Chrome(options=options)

driver = webdriver.Firefox(options=options)

driver.get('http://www.baidu.com')

print(driver.title)
print(driver.page_source)