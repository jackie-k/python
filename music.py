from selenium import webdriver
from bs4 import BeautifulSoup
import openpyxl
import urllib.request

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException



path = 'D:/chromedriver.exe'
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(path, options=options)
driver.implicitly_wait(5)
driver.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%AE%A4%EC%A7%81%ED%8E%98%EC%8A%A4%ED%8B%B0%EB%B2%8C&oquery=%EC%97%AC%EB%A6%84%EC%B6%95%EC%A0%9C&tqi=UCvoQsp0JXVssBQ5ZndssssstFR-050033')

for page in range(2,11):
    for i in range(1,3):
        for j in range(1,5):
            driver.find_element_by_xpath()