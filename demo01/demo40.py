"""
# 移动到元素element对象的“顶端”与当前窗口的“顶部”对齐
driver.execute_script("arguments[0].scrollIntoView();", element);
driver.execute_script("arguments[0].scrollIntoView(true);", element);
# 移动到元素element对象的“底端”与当前窗口的“底部”对齐
driver.execute_script("arguments[0].scrollIntoView(false);", element);
# 移动到页面最底部
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)");
# 移动到指定的坐标(相对当前的坐标移动)
driver.execute_script("window.scrollBy(0, 700)");
# 结合上面的scrollBy语句，相当于移动到700+800=1500像素位置
driver.execute_script("window.scrollBy(0, 800)");
# 移动到窗口绝对位置坐标，如下移动到纵坐标1600像素位置
driver.execute_script("window.scrollTo(0, 1600)");
# 结合上面的scrollTo语句，仍然移动到纵坐标1200像素位置
driver.execute_script("window.scrollTo(0, 1200)");
"""

from selenium import webdriver

from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid=0xa7a7b7630006f677&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ib&rsv_sug3=9&rsv_sug1=12&rsv_sug7=101&rsv_t=e55cGrBRj1ABCjT%2BwBt822mLgO5IaC9hLEHIpHRpe%2FJxfDrJ0mkA%2BCYuifhT%2BSc%2F6nvb')

sleep(3)

element = driver.find_element_by_xpath('/html/body')

# driver.execute_script("arguments[0].scrollIntoView(false);", element);
# sleep(3)
# driver.execute_script("arguments[0].scrollIntoView(true);", element);

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)");

driver.execute_script("window.scrollBy(0, 700)");