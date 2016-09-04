import sys
import pickle
import requests
import os
from lxml import etree
from webExtract.games import Game


class HTML2Game(object):

    def __init__(self, url_prefix):
        self.url_prefix = url_prefix

    def get_urls(self, entireUrl):
        urls = []
        for i in range(1, 4):
            url = entireUrl + str(i)
            r = requests.get(url)
            selector = etree.HTML(r.text)
            # get records quantity
            count = len(selector.xpath('//div[@class="product"]'))
            for each in range(count):
                path = '//div[@class="product"][%d]/a/@href' % (each + 1)
                url = selector.xpath(path)
                real_path = self.url_prefix + url[0]
                urls.append(real_path)
        return urls

    def build_html(self, games):
        css_link = '<link rel="stylesheet" ' \
                   'type="text/css" href="stylesheet.css">'
        try:
            with open('game_display.html', 'w',
                      encoding='UTF-8', errors='ignore') as f:
                f.write('<!DOCTYPE html>\n')
                f.write('<html>\n')
                f.write('<head>\n')
                f.write('<title>Games Data</title>\n')
                f.write(css_link)
                f.write('</head>\n')
                f.write('<body>\n')
                f.write('<h1>Game Data</h1>\n')
                f.write('<hr>\n')
                f.write('<div>\n')
                f.write('<table id="table-1">\n')
                f.write('<tr>\n')
                f.write('<th>No.</th>\n')
                f.write('<th>game_ID</th>\n')
                f.write('<th>title</th>\n')
                f.write('<th>price</th>\n')
                f.write('<th>CLS</th>\n')
                f.write('<th>release_date</th>\n')
                f.write('<th>in_Stock</th>\n')
                f.write('</tr>\n')
                for each in games:
                    f.write('<tr class="game">\n')
                    f.write('<td class="NO.">' + str(games.index(each) + 1) + '</td>')
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
        except OSError as err:
            print("OS error: {0}".format(err))
        except TypeError as err:
            print('Type Error: ', err)
            raise
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    def serializing_game(self, urls):
        games = []
        print('loading....')
        for url in urls:
            result = requests.get(url)
            detail_selector = etree.HTML(result.text)
            inStock = True

            game_id = detail_selector.xpath('//div[@class="productDetails"]/div/div[last()]/div/text()')[0]

            if len(detail_selector.xpath('//span[@class="nameSubtitle"]')) != 0 \
                    and detail_selector.xpath('//span[@class="nameSubtitle"]/text()')[0][0].isupper():
                game_name = detail_selector.xpath('//span[@class="nameSubtitle"]/text()')[0]
            else:
                game_name = detail_selector.xpath('//header/h1/text()')[0]
            print(game_name)
            print(game_id)
            print(url)

            if len(detail_selector.xpath('//div[@class="stock-status unavailable"]')) == 1:
                game_price = 'TBC'
            else:
                dollars = detail_selector.xpath('//span[@class="dollar"]/text()')[0]
                if dollars == 'TBC':
                    game_price = dollars
                else:
                    cents = detail_selector.xpath('//span[@class="cents"]/text()')[0]
                    game_price = dollars + '.' + cents
            print(game_price)
            print("------------------")

            # if len(detail_selector.xpath('//div[@itemprop="price"]/@content')) == 0:
            #     game_price = 'TBC'
            # else:
            #     game_price = detail_selector.xpath('//div[@itemprop="price"]/@content')[0]

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
        try:
            with open('games.dat', 'wb') as f:
                f.write(pickle.dumps(games))
        except OSError as err:
            print("OS error: {0}".format(err))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    def unserializing_game(self, path):
        games = []
        try:
            with open(path + '/games.dat', 'rb') as f:
                games = pickle.load(f)
        except OSError as err:
            print("OS error: {0}".format(err))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        return games

if __name__ == '__main__':
    h2g = HTML2Game('https://www.mightyape.co.nz')
    entireUrl = 'https://www.mightyape.co.nz/games/ps4/adventure-rpg/All?page='
    urls = h2g.get_urls(entireUrl)
    h2g.serializing_game(urls)
    games = h2g.unserializing_game(os.getcwd())
    h2g.build_html(games)
    # print(len(h2g.get_urls(entireUrl)))
