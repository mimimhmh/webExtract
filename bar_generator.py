import plotly.plotly as py
import plotly.graph_objs as go
from collections import Counter
from webExtract.games import Classification
from webExtract.game_html_display import DataTool


py.sign_in('mimimhmh@gmail.com', '8tapwyxkuv')


class BarTool(object):

    def show_bar(self):
        mt = DataTool()
        games = mt.get_games()
        c = Counter()
        g_in = 0
        pg_in = 0
        m_in = 0
        r13_in = 0
        r16_in = 0
        r18_in = 0
        tbc_in = 0
        un_in = 0
        for game in games:
            c[game.classification] = c[game.classification] + 1
            try:
                if (game.classification == Classification.G.value) \
                        and (game.in_stock):
                    g_in += 1
                if (game.classification == Classification.PG.value) \
                        and (game.in_stock):
                    pg_in += 1
                if (game.classification == Classification.M.value) \
                        and (game.in_stock):
                    m_in += 1
                if (game.classification == Classification.R13.value) \
                        and (game.in_stock):
                    r13_in += 1
                if (game.classification == Classification.R16.value) \
                        and (game.in_stock):
                    r16_in += 1
                if (game.classification == Classification.R18.value) \
                        and (game.in_stock):
                    r18_in += 1
                if (game.classification == Classification.TBC.value) \
                        and (game.in_stock):
                    tbc_in += 1
                if (game.classification == Classification.UNDEFINED.value) \
                        and (game.in_stock):
                    un_in += 1
            except TypeError:
                print("Oops!  That was no valid type.  Try again...")

        count_G = c[Classification.G.value]
        count_PG = c[Classification.PG.value]
        count_M = c[Classification.M.value]
        count_R13 = c[Classification.R13.value]
        count_R16 = c[Classification.R16.value]
        count_R18 = c[Classification.R18.value]
        count_TBC = c[Classification.TBC.value]
        count_UNDEFINED = c[Classification.UNDEFINED.value]

        trace1 = go.Bar(
            x=['G', 'PG', 'M', 'R13', 'R16', 'R18', 'TBC', 'UNDEFINED'],
            y=[count_G, count_PG, count_M, count_R13, count_R16,
               count_R18, count_TBC, count_UNDEFINED],
            name='Total'
        )

        trace2 = go.Bar(
            x=['G', 'PG', 'M', 'R13', 'R16', 'R18', 'TBC', 'UNDEFINED'],
            y=[g_in, pg_in, m_in, r13_in, r16_in, r18_in, tbc_in, un_in],
            name='In Stock'
        )

        data = [trace1, trace2]
        layout = go.Layout(
            barmode='group'
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='grouped-bar')


# if __name__ == '__main__':
#     bt = BarTool()
#     bt.show_bar()
