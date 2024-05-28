import pickle

from selenium import webdriver

driver = webdriver.Chrome()

driver.delete_all_cookies()

driver.get('https://github.com/login')


with open("cookies.pkl", "rb") as f:
    cookies = pickle.load(f)

# driver.add_cookie(cookies)

for cookie in cookies:
    print(cookie)
    if isinstance(cookie.get('expiry'), float):
        cookie['expiry'] = int(cookie['expiry'])
    # driver.add_cookie(cookie)

driver.refresh()



print('end...')