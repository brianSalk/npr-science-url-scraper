import requests
import sys
import argparse
from scrape_each_article import scrape
from bs4 import BeautifulSoup
import os
import pickle
from_path = '/home/brian/Documents/ai/science/pickle/'
to_path = '/home/brian/Documents/ai/science/science_articles/'
all_articles = {}
all_urls = set()
# argparse stuff
parser = argparse.ArgumentParser(description='scrape text form each url, store in pickle file')
parser.add_argument('-l','--limit', default=float('inf'), help='set limit on number of urls to scrape')
args = parser.parse_args()
file_count = 1
count= 0
for file in os.listdir(from_path):
    with open(f'{from_path}{file}', 'rb') as f:
        s = pickle.load(f)
        for url in s:
            all_urls.add(url)
for url in all_urls:
    text = scrape(url)
    all_articles[url] = text
    print(url)
    count +=1 
    if count >= int(args.limit):
        print(f'writing file #{file_count}')
        count = 0
        with open(f'{to_path}/file_{file_count}', 'wb') as f:
            pickle.dump(all_articles, f)
        all_articles = {}

with open(f'{to_path}/file_{file_count}', 'wb') as f:
    pickle.dump(all_articles, f)
        
    
