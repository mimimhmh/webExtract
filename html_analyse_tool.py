import pickle


class MyTool(object):

    def analyse(self):
        games = []
        with open('games.dat', 'rb') as f:
            games = pickle.load(f)
        return games

if __name__ == '__main__':
    t = MyTool()
    games = t.analyse()
    try:
        for game in games:
            print(game.classification + ', ' + game.inStock)
    except TypeError:
        print('Type error!')
