import plotly.plotly as py
from webExtract.game_html_display import DataTool


class PieTool(object):

    def show_pie(self):
        mt = DataTool()
        games = mt.get_games()
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
            elif 40 <= price < 70:
                price_40_70 += 1
            elif 70 <= price < 100:
                price_70_100 += 1
            elif 100 <= price < 170:
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

