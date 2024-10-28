import requests

if __name__ == "__main__":
  url = 'https://www.baidu.com/'
  response = requests.get(url=url)
  page_txt = response.text
  with open('./sogou.html', 'w', encoding='utf-8') as fp:
    fp.write(page_txt)
  print('爬取数据结束!')
