import requests
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool

url_prefix = 'https://www.mightyape.co.nz'
http_url = 'https://www.mightyape.co.nz/Games/PS4/Adventure-RPG/All'
page = '?page=1'


def get_source(self, url):
    res = requests.get(url)
    return res

urls = []
for i in range(3):
    http_url = http_url + '?page=%d' % (i+1)
    urls.append(http_url)

r = requests.get(http_url)
selector = etree.HTML(r.text)
url_list = []

# 找出有多少条记录
count = len(selector.xpath('//div[@class="product"]'))
for i in range(count):
    path = '//div[@class="product"][%d]/a/@href' % (i + 1)
    url = selector.xpath(path)
    real_path = url_prefix + url[0]
    url_list.append(real_path)

print(url_list[0])

result = requests.get(url_list[0])
detail_selector = etree.HTML(result.text)
game_name = detail_selector.xpath('//span[@itemprop="name"]/text()')
game_price = detail_selector.xpath('//div[@itemprop="price"]/@content')
game_classification = detail_selector.xpath('//div[@class="classification"]/img/@alt')

print(game_classification[0])

