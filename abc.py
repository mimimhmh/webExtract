import cmd
from cbc import HTML_2_Game

class CLI(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)

        self.prompt = "> "  # define command prompt


    def do_build_game_data(self, arg):
        h2g = HTML_2_Game('https://www.mightyape.co.nz')
        entireUrl = 'https://www.mightyape.co.nz/Games/PS4/Adventure-RPG/All?page='
        urls = h2g.get_urls(entireUrl)
        games = h2g.get_games(urls)
        h2g.build_html(games)


    def help_build_game_data(self):
        print("syntax: scrap data from urls and build an html to display what we got!")


    def do_quit(self, arg):
        return True


    def help_quit(self):
        print("syntax: quit -- terminates the application")


if __name__ == "__main__":
    cli = CLI()

    cli.cmdloop()