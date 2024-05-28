from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="/Users/sylvia/Documents/drivers")
driver.get('http://sahitest.com/demo/clicks.htm')

sleep(3)

# btn = driver.find_element_by_xpath('/html/body/form/input[2]')
# ActionChains(driver).double_click(btn).perform()

# btn = driver.find_element_by_xpath('/html/body/form/input[3]')

# ActionChains(driver).click(btn).perform()
# driver.find_element_by_xpath('/html/body/form/input[3]').click()

btn = driver.find_element_by_xpath('/html/body/form/input[4]')

ActionChains(driver).context_click(btn).perform()

sleep(3)

driver.quit()