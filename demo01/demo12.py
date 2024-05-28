from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://sahitest.com/demo/headingsTest.htm')

h1 = driver.find_element_by_tag_name('h1')

print(h1.size)
print(h1.tag_name)
print(h1.text)

# print(type(h1))

driver.quit()