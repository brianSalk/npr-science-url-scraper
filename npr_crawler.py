import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
driver = webdriver.Firefox()
YEAR = ""
LIMIT = float('inf')
for i,each in enumerate(sys.argv):
    if each == '-y':
        YEAR= sys.argv[i+1]
    if each == '-l':
        LIMIT = int(sys.argv[i+1])
def get_all_articles_on_current_page(driver):
    all_articles = driver.find_elements(By.TAG_NAME, 'article')
    urls = []
    time.sleep(5)
    for article in all_articles:
        # fix me: not all have teaser, use title and try block
        try:
            title = article.find_element(By.CLASS_NAME,'title')
            first_a = title.find_elements(By.TAG_NAME, 'a')[0]
            url = first_a.get_attribute('href')
            urls.append(url)
        except Exception:
            continue
    return urls

def scrape_each_article():
     pass
all_urls = set()
def crawl_npr_science_archive_at_url(url):
    driver.get(url)
    # needs to go to bottom of page then up then back down to initiate infinit scrolling
    element = driver.find_elements(By.CLASS_NAME,'item')[-1]
    time.sleep(1)
    driver.execute_script('arguments[0].scrollIntoView();', element)
    time.sleep(1)
    element = driver.find_elements(By.CLASS_NAME,'item')[-3]
    driver.execute_script('arguments[0].scrollIntoView();', element)
    last_element = element
    while True:
        element = driver.find_elements(By.CLASS_NAME,'item')[-1]
        time.sleep(1)
        driver.execute_script('arguments[0].scrollIntoView();', element)

        urls = get_all_articles_on_current_page(driver)
        for each in urls:
            all_urls.add(each)
        print(len(all_urls))
        time.sleep(4)
        if len(all_urls) > LIMIT:
            break
        if element == last_element:
            # needs to go to bottom of page then up then back down to initiate infinit scrolling
            element = driver.find_elements(By.CLASS_NAME,'item')[-1]
            time.sleep(1)
            driver.execute_script('arguments[0].scrollIntoView();', element)
            time.sleep(1)
            element = driver.find_elements(By.CLASS_NAME,'item')[-3]
            driver.execute_script('arguments[0].scrollIntoView();', element)
            last_element = element

        last_element = element
    print(f'last article: {urls[-1]}')

def get_url_from_year(year):
    return f'https://www.npr.org/sections/science/archive?date=12-31-{year}'
def generate_urls(most_recent_date):
    urls = []
    for year in range(1998,most_recent_date+1):
        urls.append(get_url_from_year(year))
    return urls
url = get_url_from_year(YEAR)
crawl_npr_science_archive_at_url(url)
    

import pickle
with open(f'{YEAR}_urls','wb') as f:
    pickle.dump(all_urls,f)
