import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import threading
from time import sleep


class scrapper:
    def __init__(self, path='./chromedriver.exe',
                 IP='127.0.0.1:9222', profile_name='ChromeProfile',
                 chrome_port='9222'):
        assert chrome_port[0] == '9', 'port must be 9xxx; e.g:9123,9432'
        self._ip = IP
        self.chrome_port = chrome_port
        #self.profile_path = f'../profile/{profile_name}'
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("window-size=1920x1080")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')  # Not used
        # options.add_experimental_option("debuggerAddress", self._ip)
        # s = Service(path)
        # print('Initializing Chrome Driver...')
        # self.Init_Remote_Driver()
        # sleep(5)
        self.driver = webdriver.Chrome(options=options)
        print('Driver established')

    # def Init_Remote_Driver(self):
    #     # if not os.path.exists(self.profile_path):
    #     #     # Create a new directory because it does not exist
    #     #     os.makedirs(self.profile_path)
    #     #     print(f"The new profile directory created @{self.profile_path}")
    #     # else:
    #     #     print(f"Existing Profile directory accessed @{self.profile_path}")
    #     print(f"Remote Server Established at PORT:{self.chrome_port}")
    #     cmd = f'cmd /k chrome.exe --remote-debugging-port={self.chrome_port}"'
    #     print(cmd)
    #     _t = threading.Thread(target=lambda: os.system(cmd))
    #     _t.start()

    def scrape_site(self, SAMPLE_URL):
        print('\tScrapping:',SAMPLE_URL)
        try:
            self.driver.get(SAMPLE_URL)
            src = self.driver.page_source
            parser = BeautifulSoup(src, "html.parser")
            return src, parser
        except Exception as e:
            error_msg = 'Selenium-Scrapper Error:\n\t' + str(e)
            print(error_msg)
            return error_msg, None


if __name__ == '__main__':
    # URL = 'https://www.google.com/search?gs_ssp=eJzj4tLP1TcwMjOssCgxYPTiy87MVchOLEpJLM7ITMwDAHIaCM0&q=kim+kardashian&oq=kim+&aqs=chrome.1.69i57j46i433i512j46i131i433i512l3j0i512j0i131i433i512j46i433i512l2j0i131i433i512.1735j0j7&sourceid=chrome&ie=UTF-8'
    URL = 'https://ryan47liao.github.io/Ryan-Portfolio/'
    bot = scrapper()
    src, parse = bot.scrape_site(URL)
    print(src)
    # print(parse)
