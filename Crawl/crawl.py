import json
from crawling import open_web, login, access
from selenium.webdriver.remote.webdriver import WebDriver
URL = "https://khh.mplis.gov.vn/dc/HoSoDiaChinh"

def access_to_ward():
    driver, cre = open_web()
    login(driver=driver,cre=cre)

def crawl(driver: WebDriver, cre: json):
    files = access(driver=driver, cre= cre)
    print(files)
    driver.quit()