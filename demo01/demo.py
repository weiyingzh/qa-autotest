# -*- coding: utf-8 -*-
# python 3.5.0

import re
import pytesseract
from selenium import webdriver
from PIL import Image, ImageEnhance
import requests

username = "xxxxxx"
password = "xxxxxx"

loginurl = 'https://passport.baidu.com/v2/?login'

# 截图或验证码图片保存地址
screenImg = "screenImg.png"

# 打开浏览器
driver = webdriver.Chrome()
driver.get(loginurl)
driver.implicitly_wait(1)

# cookie= driver.get_cookies()
assert "登录百度帐号" in driver.title

driver.find_element_by_id('TANGRAM__PSP_3__footerULoginBtn').click()

# 数据账号&密码(此处不提交)
driver.find_element_by_id("TANGRAM__PSP_3__userName").send_keys(username)
driver.find_element_by_id("TANGRAM__PSP_3__password").send_keys(password)

# 用于测试，此处可提前提交，让登录出错，页面出现验证码
driver.find_element_by_id("TANGRAM__PSP_3__submit").click()

# 获取验证码URL地址
imgsrc = driver.find_element_by_id("TANGRAM__PSP_3__verifyCodeImg").get_attribute('src')
print(imgsrc)
res = requests.get(imgsrc)

with open('test.png', 'wb') as f:
    f.write(res.content)

# 如果匹配验证码路径成功（说明有提示输入验证码），则需读取验证码！
# if re.match(r'https://passport.baidu.com/cgi-bin/genimage.*', imgsrc):
    # 浏览器页面截屏
# driver.get_screenshot_as_file(screenImg)
# 定位验证码位置及大小

# img = driver.find_element_by_id('TANGRAM__PSP_3__verifyCodeImg')
#
# url = img.get_attribute('href')



# location = driver.find_element_by_id('TANGRAM__PSP_3__verifyCodeImg').location
# size = driver.find_element_by_id('TANGRAM__PSP_3__verifyCodeImg').size
# left = location['x']
# top = location['y']
# right = location['x'] + size['width']
# bottom = location['y'] + size['height']
# # 从文件读取截图，截取验证码位置再次保存
# img = Image.open(screenImg).crop((left, top, right, bottom))
# img = img.convert('L')  # 转换模式：L | RGB
# img = ImageEnhance.Contrast(img)  # 增强对比度
# img = img.enhance(2.0)  # 增加饱和度
# img.save(screenImg)
# 再次读取识别验证码
img = Image.open('test.png')

code = pytesseract.image_to_string(img, lang='chi_sim+eng')
print('code:',code)
# code= pytesser.image_file_to_string(screenImg)
driver.find_element_by_id("TANGRAM__PSP_3__verifyCode").send_keys(code.strip())
print(code.strip())

# 提交登录
driver.find_element_by_id("TANGRAM__PSP_3__submit").click()

# driver.implicitly_wait(10)
# driver.quit()