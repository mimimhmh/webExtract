import pickle
import requests
from lxml import etree
from games import Game

class HTML_2_Game(object):
    def __init__(self, url_prefix):
        self.url_prefix = url_prefix

    def get_urls(self, entireUrl):
        urls = []
        for i in range(1, 4):
            # url = 'https://www.mightyape.co.nz/Games/PS4/Adventure-RPG/All?page=' + str(i)
            url = entireUrl + str(i)
            r = requests.get(url)
            selector = etree.HTML(r.text)
            # get records quantity
            count = len(selector.xpath('//div[@class="product"]'))
            for each in range(count):
                path = '//div[@class="product"][%d]/a/@href' % (each + 1)
                url = selector.xpath(path)
                real_path = self.url_prefix + url[0]
                # print(real_path)
                urls.append(real_path)
        return urls

    def build_html(self, games):
        with open('game_display.html', 'w', encoding='UTF-8', errors='ignore') as f:
            f.write('<!DOCTYPE html>\n')
            f.write('<html>\n')
            f.write('<head>\n')
            f.write('<title>Games Data</title>\n')
            f.write('<link rel="stylesheet" type="text/css" href="stylesheet.css">')
            f.write('</head>\n')
            f.write('<body>\n')
            f.write('<h1>Game Data</h1>\n')
            f.write('<hr>\n')
            f.write('<div>\n')
            f.write('<table id="table-1">\n')
            f.write('<tr>\n')
            f.write('<th>game_ID</th>\n')
            f.write('<th>title</th>\n')
            f.write('<th>price</th>\n')
            f.write('<th>CLS</th>\n')
            f.write('<th>release_date</th>\n')
            f.write('<th>in_Stock</th>\n')
            f.write('</tr>\n')
            for each in games:
                f.write('<tr class="game">\n')
                f.write('<td class="gid">' + each.game_id + '</td>\n')
                f.write('<td class="title">' + each.name + '</td>\n')
                if each.price != 'TBC':
                    f.write('<td class="price">$' + each.price + '</td>\n')
                else:
                    f.write('<td class="price">' + each.price + '</td>\n')
                f.write('<td class="cls">' + each.classification + '</td>\n')
                f.write('<td class="release_date">' + each.release_date + '</td>\n')
                f.write('<td class="in_stock">' + str(each.inStock) + '</td>\n')
                f.write('</tr>\n')
            f.write('</table>\n')
            f.write('</div>\n')
            f.write('</body>\n')

    def serializing_game(self, urls):
        games = []
        print('loading....')
        for each in urls:
            result = requests.get(each)
            detail_selector = etree.HTML(result.text)
            inStock = True

            if len(detail_selector.xpath('//span[@class="nameSubtitle"]')) != 0:
                game_name = detail_selector.xpath('//span[@class="nameSubtitle"]/text()')[0]
            else:
                game_name = detail_selector.xpath('//span[@itemprop="name"]/text()')[0]
            print(game_name)
            if len(detail_selector.xpath('//div[@class="productDetails"]//span[@itemprop="identifier"]/text()')) == 1:
                game_id = detail_selector.xpath('//div[@class="productDetails"]//span[@itemprop="identifier"]/text()')[
                    0]
            else:
                game_id = detail_selector.xpath('//div[@class="productDetails"]//span[@itemprop="identifier"]/text()')[
                    1]

            if len(detail_selector.xpath('//div[@itemprop="price"]/@content')) == 0:
                game_price = 'TBC'
            else:
                game_price = detail_selector.xpath('//div[@itemprop="price"]/@content')[0]

            if len(detail_selector.xpath('//div[@class="classification"]/img/@alt')) == 0:
                game_classification = 'undefined'
            else:
                game_classification = detail_selector.xpath('//div[@class="classification"]/img/@alt')[0]

            status_str = detail_selector.xpath('//div[@class="status"]/text()')[0].strip()
            if status_str != 'In stock at':
                inStock = False
            release_date = detail_selector.xpath('//div[@class="productDetails"]/div/div/div/text()')[0].strip()
            game = Game(game_id, game_name, game_price, game_classification, release_date, inStock)
            games.append(game)
        with open('games.dat', 'wb') as f:
            f.write(pickle.dumps(games))

    def unserializing_game(self):
        games = []
        with open('games.dat', 'rb') as f:
            games = pickle.load(f)
        return games

if __name__ == '__main__':
    h2g = HTML_2_Game('https://www.mightyape.co.nz')
    entireUrl = 'https://www.mightyape.co.nz/Games/PS4/Adventure-RPG/All?page='
    urls = h2g.get_urls(entireUrl)
    games = h2g.unserializing_game()
    h2g.build_html(games)
