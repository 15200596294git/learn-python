import requests
import re
from bs4 import BeautifulSoup
import json
from openpyxl import Workbook 
import os

wb = Workbook()
sheet = wb.create_sheet('demo_sheet', index=0)
def request__dandan(url):
  try:
    response = requests.get(url)
    if response.status_code == 200:
      return response.text
  except requests.RequestException:
    return None

def parse_result(html):
  # pattern = re.compile(,re.S)
  soup = BeautifulSoup(html, 'html.parser')
  items = soup.select('body > div.bang_wrapper > div.bang_content > div.bang_list_box > ul > li')

  # 排名 书名 图片地址 作者 推荐指数 五星评分数 价格
  for s in items:
    rank = s.select_one('div.list_num').text.split('.', 1)[0]
    book_name = s.select_one('div.name > a')['title']
    pic = s.select_one('div.pic > a > img')['src']
    author = s.select_one('div:nth-child(5) > a')
    
    # print(author)
    if author:
      author = author.text
    
    tuijian =  s.select_one('div.star > span.tuijian').text
    full_number = s.select_one('div.biaosheng > span').text
    price = s.select_one('div.price > p:nth-child(1) > span.price_n').text
    
    
    yield [rank,book_name,author,pic,tuijian,full_number,price]
    # yield {
    #   'rank': rank,
    #   'book_name': book_name,
    #   'pic': pic,
    #   'author': author,
    #   'tuijian': tuijian,
    #   'full_number': full_number,
    #   'price': price,
    # }

def write_item_to_file(item):
  # print('开始写入数据')
  with open('book.txt', 'a', encoding='utf-8') as fp:
    sheet.append(item)
    wb.save(os.path.join(os.path.dirname(__file__), '当当.xlsx'))
    
def main(page):
  url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
  html = request__dandan(url)
  items = parse_result(html)

  for item in items:
    print(item)
    write_item_to_file(item)

for i in range(1,3):
  main(i)

