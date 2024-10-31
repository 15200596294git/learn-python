import requests
from bs4 import BeautifulSoup
import os
from openpyxl import Workbook

if __name__ == '__main__':
  current_dir = os.path.dirname(__file__)
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
  }
  wb = Workbook()
  sheet = wb.create_sheet('豆瓣电影', 0)
  sheet.append(['电影名称','电影图片','电影排名','电影评分','电影作者','电影简介'])
  for i in range(5):
    # print(i)

    url = 'https://movie.douban.com/top250?start=' + str(i * 25) + '&filter='
    response = requests.get(url, headers=headers)
    page_text = response.text
    soup = BeautifulSoup(page_text, 'html.parser')
    movie_nodes = soup.select('#content > div > div.article > ol > li')
    for movie_node in movie_nodes:
      print(movie_node)
      # 电影名称
      moview_name = movie_node.select_one('div > div.info > div.hd > a > span:nth-child(1)').text
      # 电影图片
      moview_pic = movie_node.select_one('div > div.pic > em').text
      # 电影排名
      moview_rank = movie_node.select_one('div > div.pic > em').text


      # 电影评分
      moview_rate = movie_node.select_one('div > div.info > div.bd > div > span.rating_num').text

      # 电影作者
      # movie_node.select_one('div > div.pic > em')

      # 电影简介
      moview_brief = movie_node.select_one('div > div.info > div.bd > p.quote > span')
      if moview_brief:
        moview_brief = moview_brief.text

      row = [moview_name,moview_pic,moview_rank,moview_rate, '' ,moview_brief]
      sheet.append(row)
  wb.save(os.path.join(current_dir, 'douban.xlsx'))

