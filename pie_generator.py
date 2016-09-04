import plotly.plotly as py
from html_analyse_tool import MyTool


class PieTool(object):

    def show_pie(self):
        mt = MyTool()
        games = mt.analyse()
        price_40_below = 0
        price_40_70 = 0
        price_70_100 = 0
        price_100_170 = 0
        price_170_plus = 0
        price_tbc = 0
        for game in games:
            if game.price == 'TBC':
                price_tbc += 1
            else:
                price = float(game.price)
            if price < 40:
                price_40_below += 1
            elif price >= 40 and price < 70:
                price_40_70 += 1
            elif price >= 70 and price < 100:
                price_70_100 += 1
            elif price >= 100 and price < 170:
                price_100_170 += 1
            elif price >= 170:
                price_170_plus += 1

        fig = {
            'data': [{'labels': ['$40-', '$40~$70', '$70~ $100',
                                 '$100~ $170', '$170+', 'TBC'],
                      'values': [price_40_below, price_40_70, price_70_100,
                                 price_100_170, price_170_plus, price_tbc],
                      'type': 'pie'}],
            'layout': {'title': 'Game Price Consist'}
        }

        py.plot(fig)

'''

'''
if __name__ == '__main__':
    pt = PieTool()
    pt.show_pie()
