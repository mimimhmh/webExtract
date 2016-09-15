import cmd
import os
import webbrowser
from webExtract.url_tools import URLTool
from webExtract.game_html_display import DataTool
from webExtract.bar_generator import BarTool
from webExtract.pie_generator import PieTool


class CLI(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        print("Please type help first and decide what you need!")
        self.prompt = "> "  # define command prompt

    def do_build_game_data(self, arg):
        URLTool().serialize_data()
        DataTool().build_html()
        webbrowser.open('file://' + os.path.realpath('game_display.html'))

    def help_build_game_data(self):
        print("syntax: scrap data from urls "
              "and build an html to display what we got!")

    def do_show_bar(self, arg):
        bt = BarTool()
        bt.show_bar()

    def help_show_bar(self):
        print("syntax: scrap data from urls "
              " build an html to display what we got!")

    def do_show_pie(self, arg):
        pt = PieTool()
        pt.show_pie()

    def help_show_pie(self):
        print("syntax: scrap data from urls "
              "and build an html to display what we got!")

    def do_quit(self, arg):
        return True

    def help_quit(self):
        print("syntax: quit -- terminates the application")

if __name__ == "__main__":
    cli = CLI()
    cli.cmdloop()
