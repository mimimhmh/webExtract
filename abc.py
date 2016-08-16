import cmd

import os

import sys

class CLI(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)

        self.prompt = "> "  # define command prompt


    def do_dir(self, arg):
        if not arg:

            self.help_dir()

        elif os.path.exists(arg):
            try:
                print("\n".join(os.listdir(arg)))
            except NotADirectoryError as e:
                print('except:', e)
        else:
            print('no such file!')


    def help_dir(self):
        print("syntax: dir path -- display a list of files and directories")


    def do_quit(self, arg):
        return True


    def help_quit(self):
        print("syntax: quit -- terminates the application")


    # define the shortcuts

    do_q = do_quit

if __name__ == "__main__":
    cli = CLI()

    cli.cmdloop()