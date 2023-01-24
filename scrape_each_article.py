import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

def scrape(url):
    # del me
    print(UserAgent().random, '-------------------------------------------------------------------------')
    url = "https://www.npr.org/2023/01/20/1150270579/toadzilla-cane-toad-australia-record-largest"
    session = requests.session()
    session.proxies = {}
    session.proxies['http'] = 'socks5://localhost:9150' #9150 for browser; 9050 for TOR service
    session.proxies['https'] = 'socks5://localhost:9150'
    headers = {"User_Agent":UserAgent().random}
    res = session.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    story_text = soup.find_all('div',{'id':'storytext'})
    print(story_text.text)
scrape("")

