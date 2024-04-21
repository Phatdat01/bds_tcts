import os
import json
from pathlib import Path
from typing import Union, List
from selenium.webdriver.remote.webdriver import WebDriver

from Crawl.crawling import open_web, login, load_pages, access

URL = "https://khh.mplis.gov.vn/dc/HoSoDiaChinh"
DOWNLOAD_PATH = str(Path.home() / "Downloads")

def access_to_ward(cre: json, reload: bool = False, driver: WebDriver = None) -> List[Union[WebDriver, Union[int, str]]]:
    try:
        if not reload:
            driver = open_web(cre=cre)
            driver.maximize_window()
            login(driver=driver,cre=cre)
        else:
            pass   
        page_number = load_pages(driver=driver, cre= cre)
        return driver, page_number
    except Exception as e:
        return driver, e
        

def crawl(driver: WebDriver, cre: json):
    if cre["path"] == "" or not os.path.exists(cre["path"]):
        cre["path"] = DOWNLOAD_PATH
    files = access(driver=driver, cre= cre)
    print(files)
    driver.quit()