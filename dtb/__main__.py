from argparse import ArgumentParser
import importlib
import runpy
from urllib import request
from .message import TextMessage


parser = ArgumentParser(description='A DingTalk bot.')
parser.add_argument('--config-file', type=str, nargs='?',
                    default='config.py',
                    help='configuration file')
parser.add_argument('--config', type=str, nargs='?',
                    default='config',
                    help='configuration object')

args = parser.parse_args()


def main():
    config = runpy.run_path(args.config_file)[args.config]
    url = config.url()

    msg = TextMessage('这是text', '这是content')
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    req = request.Request(url, msg.dump(), headers)
    with request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))


if __name__ == '__main__':
    main()
