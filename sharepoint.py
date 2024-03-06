import argparse
import configparser
import logging

import sharepy

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config',
        nargs = '+',
        help = 'Config file(s).',
    )
    args = parser.parse_args(argv)

    cp = configparser.ConfigParser()
    cp.read(args.config)

    logging.basicConfig(level=logging.DEBUG)

    site = cp['sharepoint']['site']
    username = cp['sharepoint']['username']
    password = cp['sharepoint']['password']

    conn = sharepy.connect(site, username, password)

if __name__ == '__main__':
    main()
