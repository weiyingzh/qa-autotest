from selenium import webdriver

from time import sleep




driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

sleep(2)

# driver.save_screenshot('baidu.png')

# <img src='data:image/png,base64,

# img_str = driver.get_screenshot_as_base64()

# print(img_str)


test = driver.get_screenshot_as_png()
print(test)