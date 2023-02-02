import requests
#from scrape_each_article import scrape
from bs4 import BeautifulSoup
import os
import pickle
path = '/home/brian/Documents/ai/science/pickle/'
all_urls = set()
for file in os.listdir(path):
    print('FILE IS:',file,'-'*20)
    with open(f'{path}{file}', 'rb') as f:
        s = pickle.load(f)
        for url in s:
            all_urls.add(url)
print(all_urls)
print(len(all_urls))
