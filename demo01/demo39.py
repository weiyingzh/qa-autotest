from selenium import webdriver


options = webdriver.ChromeOptions()

options.add_argument('--proxy-server=https://60.13.42.176:9999')

driver = webdriver.Chrome(options=options)

driver.get('http://www.baidu.com')

print(driver.title)