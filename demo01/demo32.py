from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://jqueryui.com/selectable/')

driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))

sleep(3)

item1 = driver.find_element_by_xpath('//*[@id="selectable"]/li[1]')
item4 = driver.find_element_by_xpath('//*[@id="selectable"]/li[4]')


ActionChains(driver).key_down(Keys.CONTROL).click(item1).perform()
ActionChains(driver).key_down(Keys.CONTROL).click(item4).perform()

sleep(3)