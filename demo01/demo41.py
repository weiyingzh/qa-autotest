import csv

# with open(r'C:\Users\ghz\Desktop\demo.csv', encoding='utf-8') as f:
#     data = csv.reader(f)
#     for line in data:
#         print(line[0], line[1])

from selenium import webdriver

from time import sleep

# ddt

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

input = driver.find_element_by_id('kw')

btn = driver.find_element_by_id('su')

with open(r'C:\Users\ghz\Desktop\keys.csv', encoding='utf-8') as f:
    data = csv.reader(f)
    for line in data:
        key = line[0]
        input.send_keys(key)
        btn.click()
        sleep(2)
        input.clear()
        sleep(3)



