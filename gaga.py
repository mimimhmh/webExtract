import plotly.plotly as py
import plotly.graph_objs as go
from collections import Counter
from cbc import HTML_2_Game
from games import Classification

py.sign_in('mimimhmh@gmail.com', '8tapwyxkuv')


h2g = HTML_2_Game('https://www.mightyape.co.nz')
entireUrl = 'https://www.mightyape.co.nz/Games/PS4/Adventure-RPG/All?page='
urls = h2g.get_urls(entireUrl)
games = h2g.get_games(urls)
c = Counter()
for game in games:
    print(game.name)
    c[game.classification] = c[game.classification] + 1

count_G = c[Classification.G.value]
count_PG = c[Classification.PG.value]
count_M = c[Classification.M.value]
count_R13 = c[Classification.R13.value]
count_R16 = c[Classification.R16.value]
count_R18 = c[Classification.R18.value]
count_TBC = c[Classification.TBC.value]
count_UNDEFINED = c[Classification.UNDEFINED.value]

data = [go.Bar(
    x=['G', 'PG', 'M', 'R13', 'R16', 'R18', 'TBC', 'UNDEFINED'],
    y=[count_G, count_PG, count_M, count_R13, count_R16, count_R18, count_TBC, count_UNDEFINED]
)]

py.plot(data, filename='basic-bar')