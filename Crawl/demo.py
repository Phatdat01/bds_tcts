import os
import json
import time
import shutil
from pathlib import Path
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

DOWNLOAD_PATH = str(Path.home() / "Downloads")

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

def load_chrome():
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def login(driver: WebDriver, cre: json):
    name = wait_element(driver=driver, timeout=10,key="username",by="name")
    name.send_keys(cre["name"])
    pw= driver.find_element(By.NAME, "password")
    pw.send_keys(cre["pw"])
    login = wait_element(driver=driver, timeout=10,key="login100-form-btn",by="class")
    login.click()

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
    

def open_web():
    cre= load_json()
    if cre["download_path"] == "" or "chrome" in cre["tool"].lower():
        driver = load_chrome()
        cre["download_path"] = DOWNLOAD_PATH
    else:
        driver = load_edge(download_path= cre["download_path"])
    driver.get(cre["url"])
    return driver, cre