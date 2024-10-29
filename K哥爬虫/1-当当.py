import requests
import re

def request__dandan(url):
  try:
    response = requests.get(url)
    if response.status_code == 200:
      return response.text
  except requests.RequestException:
    return None

def parse_result(html):
  pattern = re.compile(,re.S)
  items = re.findall(pattern, html)
  print(items)
  for item in items:

    yield {
      'range': item[0],
      'iamge': item[1],
      'title': item[2],
      'recommend': item[3],
      'author': item[4],
      'times': item[5],
      'price': item[6]
    }

def main(page):
  url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
  html = request__dandan(url)
  items = parse_result(html)

  for item in items:
    print(item)
    # write_item_to_file(item)

main(1)

