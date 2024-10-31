from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from openpyxl import Workbook 
import os


def save_to_excel(html):
  wb = Workbook()
  sheet = wb.create_sheet('demo_sheet', index=0)
  sheet.append(['视频标题', '视频封面','视频地址'])
  bs = BeautifulSoup(html, 'html.parser')
  #i_cecream > div > div:nth-child(2) > div.search-content--gray.search-content > div > div > div > div.video.i_wrapper.search-all-list > div > div
  videos = bs.select('#i_cecream > div > div:nth-child(2) > div.search-content--gray.search-content > div > div > div > div.video.i_wrapper.search-all-list > div > div')
  # print(videos)
  for video in videos:
    title = video.select_one('div > div.bili-video-card__wrap.__scale-wrap > div > div > a > h3').text
    video_src = video.select_one('div > div.bili-video-card__wrap.__scale-wrap > a')['href']
    img = video.select_one('div > div.bili-video-card__wrap.__scale-wrap > a > div > div.bili-video-card__image--wrap > picture > img')['src']
    sheet.append([title, 'https://' + img ,'https://' + video_src])
  wb.save(os.path.join(os.path.dirname(__file__), 'cxk.xlsx'))
    
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

url = 'https://www.bilibili.com/'

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options)
wait = WebDriverWait(driver, 10)
driver.get(url)
input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#nav-searchform > div.nav-search-content > input')))
submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#nav-searchform > div.nav-search-btn')))

input.send_keys('蔡徐坤 篮球')
submit.click()

all_h = driver.window_handles
driver._switch_to.window(all_h[1])
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#i_cecream > div > div:nth-child(2) > div.search-content--gray.search-content > div > div > div > div.video.i_wrapper.search-all-list > div > div')))
html = driver.page_source
save_to_excel(html)




