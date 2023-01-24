import requests
from scrape_each_article import scrape
from bs4 import BeautifulSoup
import os
import pickle
path = '/home/brian/Documents/ai/science/pickle/'
for file in os.listdir(path):
    with open(f'{path}{file}', 'rb') as f:
        s = pickle.load(f)
        for url in s:
            # scrape(url)
            print(url)
