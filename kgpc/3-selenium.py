from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
import json
from browsermobproxy import Server

# server = Server(r'D:\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat')
# server.start()
proxy = server.create_proxy()

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
# options.add_argument('--proxy-server-{0}'.format(proxy.proxy))
# proxy.new_har("douyin", options={'captureHeaders': True, 'captureContent': True})
driver = webdriver.Chrome(options=options)
driver.get("https://pre.luckyxp.cn/")
dingding = driver.find_element(By.CSS_SELECTOR, '#root > section > div > div > div > div > div.login_wrap_btn > button:nth-child(1)')
if dingding:
  dingding.click()

# result = proxy.har
# for entry in result['log']['entries']:
#   _url = entry['result']['url']
#   print(_url)

# cookies =  driver.get_cookies()
# print(cookies)

# driver.find_element_by_css_selector('#container > div > div.w-container.box.fill > div.w-left-menu > a.w-save-menu.w-values-menu.w-menu-selected')
# a =  driver.find_element(By.CSS_SELECTOR, '#container > div > div.w-container.box.fill > div.w-left-menu > a.w-save-menu.w-values-menu.w-menu-selected')
# print(a)
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
# time.sleep(10)

# data = {
#   'clientId': '1730343829922-16',
#   'name': 'cookie.json',
#   'value': 'aaaaaA',
#   'active': 'true',
#   'key': 'w-reactkey-2',
#   'changed': 'true',
#   'selected': 'true',
#   'hide': 'false'
# }

# requests.post('http://localhost:8899/cgi-bin/values/add', data=data)

