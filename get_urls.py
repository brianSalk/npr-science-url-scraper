import selenium                                                 
from selenium.webdriver.common.by import By                     
from selenium import webdriver                                  
from selenium.webdriver.common.action_chains import ActionChains
import time                                                     
# there is no need to extract each month, you can start at the last day of the year and infinit scroll down from there.
url = 'https://www.npr.org/sections/science/archive?'
driver = webdriver.Firefox()
driver.get(url)

years = driver.find_elements(By.CLASS_NAME, 'year')
for each in years:
    months = each.find_element(By.CLASS_NAME, 'months')
    a = months.find_elements(By.TAG_NAME, 'a')[0]
    print(a.get_attribute('href'))
    print('-'*10)

