"""
brand_watch.py
@brad_anton

"""

from BrandWatch import Watcher
import argparse


api_key = None # Define your api key here or in config.json 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('brand')
    parser.add_argument('-e', '--exclude')
    args = parser.parse_args()

    if api_key is None:
        with open('config.json', 'rb') as f:
            from json import load
            config = load(f)
        api_key = config['investigate_api_key']
    
    if not args.exclude:
        w = Watcher(api_key=api_key, brand=args.brand, days=30)
    else:
        with open(args.exclude, 'rb') as f:
            exclude = f.read().splitlines()

        w = Watcher(api_key=api_key, brand=args.brand, exclude=exclude)

    w.search()
