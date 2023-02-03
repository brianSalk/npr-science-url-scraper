import requests
from time import sleep
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

def scrape(url):
    """rotate user-agent to avoid rate limit
    check to make sure each page contains storytext div
    scrape each p tag that is a direct child of the storytext"""
    sleep(1)
    ua = UserAgent()
    print('HERE,',url)
    header = {'User-Agent': ua.random}
    try:
        response = requests.get(url, headers=header,timeout=10)
    except Exception:
        print('took too long, no scrape')
    soup = BeautifulSoup(response.text, 'html.parser')
    storytext = soup.find('div',{'id': 'storytext'}) 
    if not storytext:
        return []
    text = []
    for each in storytext.findAll('p'):
        parent = each.parent
        if parent.has_attr('id') and parent['id'] == 'storytext':
            text.append(each.text)
    return " ".join(text)
