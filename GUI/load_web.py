import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from selenium.webdriver.remote.webdriver import WebDriver

from Crawl.crawl import access_to_ward, crawl

def load(
        name: str, pw: str, 
        url: str, web: str,
        path: str,ward: str,
        page: ttk.Combobox,
        run_action: tk.Button
    ) -> WebDriver:

    global driver
    cre ={
        "name": name,
        "pw": pw,
        "url": url,
        "web": web,
        "path": path,
        "ward": ward
    }
    if cre["name"]== "" or cre == "":
        messagebox.showerror("showerror", "User Name or Password?")
    else:
        try:
            if driver:
                driver, info = access_to_ward(cre=cre, reload=True, driver=driver)
        except:
            driver, info = access_to_ward(cre = cre)
        try:
            page['values'] = list(range(1,info+1))
            page.current(0)
            page['state'] = 'normal'
            run_action['state'] = 'normal'
            run_action['bg'] = 'Green'
            run_action['cursor'] = 'hand2'
        except:
            messagebox.showerror("showerror", info)
            driver.quit()

def run(
        ward: str,
        time_delay: int,
        page: ttk.Combobox,
        path: str= None
    ):

    cre ={
        "path": path,
        "page": int(page.get()),
        "last_page": int(page['value'][-1]),
        "ward": ward,
        "time_delay": time_delay
    }
    try:
        crawl(
            driver=driver,
            cre=cre
        )
    except Exception as e:
        messagebox.showerror("showerror", e)
    