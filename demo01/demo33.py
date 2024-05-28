from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

driver.get(r'file:///Users/sylvia/Documents/demo01/index3.html')

# js = "alert('hello');"
#
# sleep(3)
#
# driver.execute_script(js)
#
# sleep(3)

sleep(3)

h1 = driver.find_element_by_tag_name('h1')

js = 'arguments[0].style.color="red"'

# driver.execute_script(js, h1)

js = 'alert(arguments[1])'

driver.execute_script(js, 'aaa', 'bbb')

sleep(3)



