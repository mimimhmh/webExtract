import cmd
import os
import webbrowser
from game_displayer import HTML_2_Game
from bar_generator import BarTool
from pie_generator import PieTool

class CLI(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        print("Please type help first and decide what you need!")
        self.prompt = "> "  # define command prompt

    def do_build_game_data(self, arg):
        h2g = HTML_2_Game('https://www.mightyape.co.nz')
        entireUrl = 'https://www.mightyape.co.nz/Games/PS4/Adventure-RPG/All?page='
        urls = h2g.get_urls(entireUrl)
        h2g.serializing_game(urls)
        games = h2g.unserializing_game()
        h2g.build_html(games)
        webbrowser.open('file://' + os.path.realpath('game_display.html'))

    def help_build_game_data(self):
        print("syntax: scrap data from urls and build an html to display what we got!")

    def do_show_bar(self, arg):
        bt = BarTool()
        bt.show_bar()

    def help_show_bar(self):
        print("syntax: scrap data from urls and build an html to display what we got!")

    def do_show_pie(self, arg):
        pt = PieTool()
        pt.show_pie()

    def help_show_pie(self):
        print("syntax: scrap data from urls and build an html to display what we got!")

    def do_quit(self, arg):
        return True

    def help_quit(self):
        print("syntax: quit -- terminates the application")

if __name__ == "__main__":
    cli = CLI()
    cli.cmdloop()