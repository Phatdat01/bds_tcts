import json
from typing import Union, List
from selenium.webdriver.remote.webdriver import WebDriver

from Crawl.crawling import open_web, login, load_pages, access

URL = "https://khh.mplis.gov.vn/dc/HoSoDiaChinh"

def access_to_ward(cre: json) -> List[Union[WebDriver, Union[int, str]]]:
    try:
        driver = open_web(cre=cre)
        login(driver=driver,cre=cre)
        page_number = load_pages(driver=driver, cre= cre)
        return driver, page_number
    except Exception as e:
        return driver, e
        

def crawl(driver: WebDriver, cre: json):
    files = access(driver=driver, cre= cre)
    print(files)
    driver.quit()