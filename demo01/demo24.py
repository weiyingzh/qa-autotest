from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get('http://sahitest.com/demo/waitFor.htm')

driver.find_element_by_xpath('/html/body/form/input[2]').click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, 'id2')))

print(driver.find_element_by_name('t1').get_attribute('value'))
print(driver.find_element_by_id('id2').text)

# driver.current_url