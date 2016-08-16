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
                gid = selector.xpath('//td[@class="gid"]/text()')[i]
                title = selector.xpath('//td[@class="title"]/text()')[i]
                price = selector.xpath('//td[@class="price"]/text()')[i]
                cls = selector.xpath('//td[@class="cls"]/text()')[i]
                release_date = selector.xpath('//td[@class="release_date"]/text()')[i]
                in_stock = selector.xpath('//td[@class="release_date"]/text()')[i]
                game = Game(gid, title, price, cls, release_date, in_stock)
                games.append(game)
                #print(title)
        return games

if __name__ == '__main__':
    t = MyTool()
    t.analyse()