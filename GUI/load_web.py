import json
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from selenium.webdriver.remote.webdriver import WebDriver

from Crawl.crawl import access_to_ward

DOWNLOAD_PATH = str(Path.home() / "Downloads")

def load(
        name: str, pw: str, 
        url: str, web: str,
        path: str,ward: str,
        time_delay: int,
        page: ttk.Combobox, run_action: tk.Button
    ) -> WebDriver:

    global driver
    cre ={
        "name": name,
        "pw": pw,
        "url": url,
        "web": web,
        "path": path,
        "page": int(page.get()),
        "ward": ward,
        "time_delay": time_delay
    }

    driver, info = access_to_ward(cre = cre)
    try:
        page['values'] = list(range(1,info+1))
        page.current(0)
        page['state'] = 'normal'
        run_action['state'] = 'normal'
        run_action['bg'] = 'Green'
    except:
        messagebox.showerror("showerror", info)

def run():
    print("ok")