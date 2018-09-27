import argparse
import configparser
import core.messages
from sys import exit
from core.utils import empty_obj



class Config:

    token = None
    pages = []
    counts = []
    init = None
    #br = None
    br = '\n'

    def __init__(self):
        cmd = argparse.ArgumentParser(description='VK page wall dump')

        cmd.add_argument(
            '-f', '--file',
            dest = 'file',
            help = 'loads config from file (lower priority than explicit args)'
        )

        cmd.add_argument(
            '-t', '--token',
            dest = 'token',
            help = 'VK app\'s service token'
        )

        cmd.add_argument(
            '-p', '--page',
            dest = 'page',
            help = 'VK page\'s id or name'
        )

        cmd.add_argument(
            '-c', '--count',
            dest = 'count',
            type = int,
            help = 'number of posts to fetch, defaults to 1'
        )

        cmd.add_argument(
            '-i', '--init',
            dest = 'init',
            action = 'store_true',
            help = 'number of posts to fetch, defaults to 1'
        )

        from_cmd = cmd.parse_args()

        explicit = empty_obj() # явные параметры

        explicit.token = from_cmd.token
        explicit.page  = from_cmd.page
        explicit.count = from_cmd.count or 1
        self.init      = from_cmd.init

        if explicit.token and explicit.page:
            self.pages  = [explicit.page]
            self.counts = [explicit.count]
            self.token  = explicit.token

        elif from_cmd.file:
            try:
                from_ini = configparser.ConfigParser()
                from_ini.read(from_cmd.file)

                implicit = empty_obj()

                implicit.token  = from_ini['tokens']['access_token']
                implicit.pages  = list(from_ini['pages'].keys())
                implicit.counts = list(
                    map(
                        int,
                        from_ini['pages'].values()
                    )
                )

                self.token = explicit.token or implicit.token

                if not self.token:
                    exit(core.messages.ERR_INIFILE)
                else:
                    if explicit.page:
                        self.pages  = [explicit.page]
                        self.counts = [explicit.count]
                    elif implicit.pages:
                        self.pages  = implicit.pages
                        self.counts = implicit.counts
                    else:
                        exit(core.messages.ERR_INIFILE)

            except Exception as e:
                print(e)
                exit(core.messages.ERR_INIFILE)

        else:
            exit(core.messages.ERR_USAGE)

