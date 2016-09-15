import requests
import configparser
import pickle
from lxml import etree
from webExtract.games import Game


class URLTool(object):

    entire_url = ''
    target = ''
    game_id_xpath = ''
    subtitle_xpath = ''
    title_xpath = ''

    def conf_reader(self, config_file_path='info.conf'):
        cf = configparser.ConfigParser()
        cf.read(config_file_path)
        self.entire_url = cf.get("URL", "entire_url")
        self.target = cf.get("URL", "target")
        self.game_id_xpath = cf.get("URL", "game_id_xpath")
        self.subtitle_xpath = cf.get("URL", "subtitle_xpath")
        self.title_xpath = cf.get("URL", "title_xpath")

    def get_urls(self):
        urls = []
        self.conf_reader()
        for i in range(1, 4):
            url = self.entire_url + str(i)
            r = requests.get(url)
            selector = etree.HTML(r.text)
            # get records quantity
            count = len(selector.xpath('//div[@class="product"]'))
            for each in range(count):
                path = '//div[@class="product"][%d]/a/@href' % (each + 1)
                url = selector.xpath(path)
                real_path = self.target + url[0]
                urls.append(real_path)
        return urls

    def get_data_attr(self, selector, url):
        return selector.xpath(url)[0]

    def analyse_url(self):
        games = []
        urls = self.get_urls()
        for url in urls:
            result = requests.get(url)
            detail_selector = etree.HTML(result.text)
            in_stock = True

            game_id = self.get_data_attr(detail_selector, self.game_id_xpath)

            if len(detail_selector.xpath('//span[@class="nameSubtitle"]')) != 0 \
                    and self.get_data_attr(detail_selector, self.subtitle_xpath)[0].isupper():
                game_name = self.get_data_attr(detail_selector, self.subtitle_xpath)
            else:
                game_name = self.get_data_attr(detail_selector, self.title_xpath)
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

            if len(detail_selector.xpath('//div[@class="classification"]/img/@alt')) == 0:
                game_classification = 'Undefined'
            else:
                game_classification = detail_selector.xpath('//div[@class="classification"]/img/@alt')[0]

            status_str = detail_selector.xpath('//div[@class="status"]/text()')[0].strip()
            if status_str != 'In stock at':
                in_stock = False
            release_date = detail_selector.xpath('//div[@class="productDetails"]/div/div/div/text()')[0].strip()
            game = Game(game_id, game_name, game_price, game_classification, release_date, in_stock)
            games.append(game)
        print(str(len(games)) + ' in total')
        return games

    def serialize_data(self):
        games = self.analyse_url()
        try:
            with open('games.dat', 'wb') as f:
                f.write(pickle.dumps(games))
        except OSError as err:
            print("OS error: {0}".format(err))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
