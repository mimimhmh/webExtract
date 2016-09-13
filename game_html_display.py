import pickle


class DataTool(object):

    def get_games(self, path):
        games = []
        try:
            with open(path + 'games.dat', 'rb') as f:
                games = pickle.load(f)
        except OSError as err:
            print("OS error: {0}".format(err))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        return games

    def build_html(self):
        games = self.get_games('')
        print(len(games))
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
                    f.write('<td class="in_stock">' + str(each.in_stock) + '</td>\n')
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

if __name__ == '__main__':
    tool = DataTool()
    tool.build_html()
