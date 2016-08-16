from lxml import etree
from games import Game

class MyTool(object):

    def analyse(self):
        games = []
        with open('game_display.html', 'r', encoding='UTF-8') as f:
            selector = etree.HTML(f.read())
            #got how many games in the content
            count = len(selector.xpath('//tr[@class="game"]'))
            for i in range(count):
                gid = selector.xpath('//td[@class="gid"]/text()')[0]
                title = selector.xpath('//td[@class="title"]/text()')[0]
                price = selector.xpath('//td[@class="price"]/text()')[0]
                cls = selector.xpath('//td[@class="cls"]/text()')[0]
                release_date = selector.xpath('//td[@class="release_date"]/text()')[0]
                in_stock = selector.xpath('//td[@class="release_date"]/text()')[0]
                game = Game(gid, title, price, cls, release_date, in_stock)
                games.append(game)
        return games

if __name__ == '__main__':
    t = MyTool()
    t.analyse()