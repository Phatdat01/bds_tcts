import json
import time
from typing import List, Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Crawl.storing import change_id, get_by_latest_file, move_to_des

def load_json() -> json:
    fi = open("credential.json",encoding="UTF-8")
    cre = json.load(fi)
    return cre

def load_edge(download_path: str):
    prefs = {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True
    }
    options = webdriver.EdgeOptions()
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    return driver

def load_chrome(download_path: str):
    service = Service()
    options = webdriver.ChromeOptions()

    prefs = {
        'download.default_directory': download_path,
        'download.prompt_for_download': False,
        'download.directory_upgrade': True
    }
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def wait_element(driver: WebDriver, timeout: int, key: str, by: str) -> WebElement:
    if by.lower() == "id":
        condition = EC.presence_of_element_located((By.ID, key))
    elif by.lower() == "class":
        condition = EC.visibility_of_element_located((By.CLASS_NAME, key))
    elif by.lower() == "name":
        condition = EC.element_to_be_clickable((By.NAME, key))
    elif by.lower() == "tag":
        condition = EC.element_to_be_clickable((By.TAG_NAME, key))
    elif by.lower() == "css":
        condition = EC.element_to_be_clickable((By.CSS_SELECTOR, key))
    else:
        return []

    try:
        element = WebDriverWait(driver, timeout).until(condition)
        return element
    except:
        return []
    

def open_web(cre: json):
    if "chrome" in cre["web"].lower():
        driver = load_chrome(download_path= cre["path"])
    else:
        driver = load_edge(download_path= cre["path"])
    driver.get(cre["url"])
    return driver

def login(driver: WebDriver, cre: json):
    name = wait_element(driver=driver, timeout=10,key="username",by="name")
    name.send_keys(cre["name"])
    pw= driver.find_element(By.NAME, "password")
    pw.send_keys(cre["pw"])
    login = wait_element(driver=driver, timeout=10,key="login100-form-btn",by="class")
    login.click()

def choose_ward(driver: WebDriver):
    print()

def load_pages(driver: WebDriver, cre: json) -> int:
    num = 0
    while True:
        try:
            time.sleep(6.7)
            pages = wait_element(driver=driver,timeout=30,key="total",by="name")
            pages = driver.find_element(By.NAME, value="total").text
            return int(pages)
        except:
            num+=1
            if num>5:
                return int(pages)

def close_file(driver: WebDriver, id: int = -1):
    try:
        driver.switch_to.window(driver.window_handles[id])
        driver.execute_script("window.close();")
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print(f"Error in process_file: {e}")


def download_file(args: List[Tuple[int, WebElement]], driver: WebDriver):
    handle_index, file = args
    try:
        try:
            driver.switch_to.window(driver.window_handles[handle_index])
        except:
            driver.switch_to.window(driver.window_handles[1])
        save = wait_element(driver=driver,timeout=20,key="body",by="tag")
        save.send_keys(Keys.CONTROL + 's')
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print(f"Error in process_file: {e}")


def open_file(args, driver: WebDriver):
    handle_index, file = args
    try:
        link = file.get_attribute("nodeid")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[handle_index])
        driver.get(f"https://khh.mplis.gov.vn/dc/PdfViewer?fileId={link}")
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print(f"Error in process_file: {e}")
        

def access(driver: WebDriver, cre: json):
    ## Click to each content
    root = cre["path"].replace("\\", "\\\\")
    ward = cre["ward"]
    page = cre["page"]
    items = wait_element(driver=driver, timeout= 30, key="item-hosodiachinh", by="class")
    items = driver.find_elements(By.CLASS_NAME, value="item-hosodiachinh")

    start = change_id(id=0,root=root, ward=ward, page=page)
    for id in range(start, len(items)):
        items[id].find_element(By.CLASS_NAME, value="title").click()
        time.sleep(2.7)
        try:
            ## Click to each file
            files = wait_element(driver=driver, timeout= 10, key="list-group-item.file-hosoquet", by="class")
            if files:
                try:
                    files = driver.find_elements(By.CLASS_NAME, value="list-group-item.file-hosoquet")
                    files_with_handles = list(enumerate(files, start=1))

                    ## Open
                    for files_with_handle in files_with_handles:
                        open_file(args=files_with_handle,driver=driver)
                    time.sleep(cre['time_delay'])
                    
                    ## Download
                    for files_with_handle in files_with_handles:
                        download_file(args=files_with_handle,driver=driver)
                    time.sleep(1)

                    # close web
                    for files_with_handle in files_with_handles:   
                        close_file(driver=driver)
                    time.sleep(2)


                    srcs = get_by_latest_file(num=len(files), download_path=cre["path"])

                    id = change_id(id=id, root=root, ward=ward,page=page)
                    # move
                    for src in srcs:
                    
                        move_to_des(
                            root=root,
                            ward=ward,
                            page= page,
                            id=str(id),
                            file=src
                        )
                    if  len(driver.window_handles) >1:
                        for window_handle in range (1, len(driver.window_handles)):
                            close_file(driver=driver, id=window_handle)
                    driver.window_handles = [driver.window_handles[0]]
                    
                except:
                    pass
        except:
            pass
        back = driver.find_element(By.ID, value="btnCloseViewDetail")
        back.click()
        item = wait_element(driver=driver, timeout= 15, key="item-hosodiachinh", by="class")
        

    return "ok"