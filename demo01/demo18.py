from selenium import  webdriver
from selenium.webdriver.support.select import Select

from time import sleep

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/selectTest.htm')

# s1 = driver.find_element_by_id('s1Id')

# Select(s1).select_by_index(1)
# select = Select(s1)
# # select.select_by_value('o3')

# Select(s1).select_by_visible_text('o2')
# sleep(3)
#
# Select(s1).deselect_by_value('o2')
#
# sleep(3)

s2 = driver.find_element_by_id('s4Id')

Select(s2).select_by_value('o1val')
Select(s2).select_by_value('o2val')

sleep(3)

Select(s2).deselect_by_value('o1val')

sleep(3)

