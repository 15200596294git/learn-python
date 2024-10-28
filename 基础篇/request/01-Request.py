import requests
import os

if __name__ == "__main__":
  file_name = 'sogou.html'
  dir_name = os.path.dirname(__file__)
  file_path = os.path.join(dir_name, file_name)
  print(file_path)
  url = 'https://www.baidu.com/'
  response = requests.get(url=url)
  page_txt = response.text
  with open(file_path, 'w', encoding='utf-8') as fp:
    fp.write(page_txt)
  print('爬取数据结束!')
