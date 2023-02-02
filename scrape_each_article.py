import requests
from time import sleep
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

def scrape(url):
    sleep(1)
    ua = UserAgent()
    header = {'User-Agent': ua.random}
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    storytext = soup.find('div',{'id': 'storytext'}) 
    text = []
    for each in storytext.findAll('p'):
        text.append(each.text)
    return " ".join(text)
t = scrape('https://www.npr.org/2023/02/01/1153171109/tom-brady-retirement')
print(t)
