from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

elem = driver.find_element_by_id('kw')
e = driver.find_element_by_tag_name('input')

news = driver.find_element_by_link_text('新闻')
print(news.text)

# e = driver.find_element(By.LINK_TEXT, 'kw')

# print(e.get_attribute('name'))
# print(type(elem)) # WebElement

# print(type(driver)) WebDriver

inputs = driver.find_elements_by_tag_name('input')

print(len(inputs))