import sys
import argparse
# start argparse
parser = argparse.ArgumentParser(description='craw npr archives and scrape urls into a pickle file')
parser.add_argument('-y', '--year', help='enter a year to start scaping from')
parser.add_argument('-l', '--limit',default=100, help='limit each pickled set t N elements')
parser.add_argument('-d','--date', help='enter date in format D[D]-M[M]-YYYY')
parser.add_argument('-t','--topic',required=True, help='what topic do you want to scrape?')
args = parser.parse_args()
if args.year:
    args.date = f'12-31-{args.year}'
# end argparse
# make sure that f'pickle_{args.topic}' exists, if not display message and exit

import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
driver = webdriver.Firefox()
def get_date_converted(date):
    """takes date as formated on npr article page
    converts it to format used in url"""
    date_parts = date.split()
    month = date_parts[0] 
    day = date_parts[1][:-1]
    year = date_parts[2]
    new_date = ''
    if month == 'January':
        new_date = '1'
    elif month == 'February':
        new_date = '2'
    elif month == 'March':
        new_date = '3'
    elif month == 'April':
        new_date = '4'
    elif month == 'May':
        new_date = '5'
    elif month == 'June':
        new_date = '6'
    elif month == 'July':
        new_date = '7'
    elif month == 'August':
        new_date = '8'
    elif month == 'September':
        new_date = '9' 
    elif month == 'October':
        new_date = '10'
    elif month == 'November':
        new_date = '11'
    elif month == 'December':
        new_date = '12'
    else:
        print('MONTH ERROR------------------------------')
    new_date += f'-{day}-{year}' 
    return new_date

def get_all_articles_on_current_page(driver):
    all_articles = driver.find_elements(By.TAG_NAME, 'article')
    urls = []
    time.sleep(5)
    date= ""
    for article in all_articles:
        # fix me: not all have teaser, use title and try block
        try:
            date = article.find_element(By.CLASS_NAME, 'date').text
            date = get_date_converted(date)
            print('date is', date)
            title = article.find_element(By.CLASS_NAME,'title')
            first_a = title.find_elements(By.TAG_NAME, 'a')[0]
            url = first_a.get_attribute('href')
            urls.append(url)
        except Exception:
            print('exception')
            continue
    return urls, date

def scrape_each_article():
     pass
def crawl_npr_science_archive_at_url(url,all_urls):
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

        urls,last_date = get_all_articles_on_current_page(driver)
        for each in urls:
            all_urls.add(each)
        print(len(all_urls))
        time.sleep(4)
        if len(all_urls) > args.limit:
            break
        if element == last_element:
            break

        last_element = element
    print(f'last article: {urls[-1]}')
    return last_date

def get_url_from_date(date,topic):
    """convert date into url of that date"""
    return f'https://www.npr.org/sections/{topic}/archive?date={date}'
def rec(url):
    all_urls = set()
    date = crawl_npr_science_archive_at_url(url,all_urls)
        

    import pickle
    with open(f'pickle_{args.topic}/{date}_urls','wb') as f:
        pickle.dump(all_urls,f)
    rec(get_url_from_date(date,args.topic))
rec(get_url_from_date(args.date,args.topic))
