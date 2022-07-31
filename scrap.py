import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def scrape_site(SAMPLE_URL):
    options = webdriver.ChromeOptions()
    #options.headless = True
    options.add_argument("window-size=1920x1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    # options.add_argument('--disable-dev-shm-usage') # Not used
    driver = webdriver.Chrome(options=options)
    driver.get(SAMPLE_URL)
    time.sleep(5)
    for t in range(10):
        driver.find_element(by=By.TAG_NAME,value='body').send_keys(Keys.PAGE_DOWN)
    # for t in range(10):
    #     time.sleep(1)
    #     driver.find_element(by=By.CSS_SELECTOR, value='.additional_data').click()
    src = driver.page_source
    parser = BeautifulSoup(src, "html.parser")
    driver.close()
    return src, parser

if __name__ == '__main__':
    #URL = 'https://www.google.com/search?gs_ssp=eJzj4tLP1TcwMjOssCgxYPTiy87MVchOLEpJLM7ITMwDAHIaCM0&q=kim+kardashian&oq=kim+&aqs=chrome.1.69i57j46i433i512j46i131i433i512l3j0i512j0i131i433i512j46i433i512l2j0i131i433i512.1735j0j7&sourceid=chrome&ie=UTF-8'
    URL = 'https://ryan47liao.github.io/Ryan-Portfolio/'
    src, parse = scrape_site(URL)
    print(src)
    #print(parse)