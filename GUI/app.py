import tkinter as tk
from tkinter import ttk
from pathlib import Path
from typing import Tuple

DOWNLOAD_PATH = str(Path.home() / "Downloads")
WEBS_LIST = ["chrome","edge"]
WARDS_LIST = ["thị trấn Vạn Giã","xã Vạn Bình","xã Vạn Hưng","xã Vạn Khánh","xã Vạn Phú","xã Vạn Phước",
            "xã Vạn Thạnh","xã Vạn Thắng","xã Vạn Thọ","xã Xuân Sơn","xã Đại Lãnh"]

def load():
    print("ok")

def run():
    print("ok")

def process_theme(win: tk) -> Tuple[
        ttk.Entry, ttk.Entry, ttk.Combobox, 
        ttk.Entry, ttk.Combobox, ttk.Combobox, 
        tk.Button, tk.Button]:
    
    ## Header
    ttk.Label(win, text = "Hồ Sơ Địa Chính",
        font = ("Times New Roman", 20, "bold")).grid(column = 1, 
        row = 1, columnspan=4)

    # ## User- password
    ttk.Label(win, text = "User name:",
        font = ("Times New Roman", 14, "bold")).grid(column = 2, 
        row = 2, pady = 10, sticky="e")
    
    ttk.Label(win, text = "Password:",
        font = ("Times New Roman", 14, "bold")).grid(column = 2, 
        row = 3, pady = 10, sticky="e")
    
    user_name = ttk.Entry(win, font=("Times New Roman", 15), width=20).grid(
        column = 3, row = 2, sticky="w", columnspan= 2, padx=(10,0)
    )

    password = ttk.Entry(win, font=("Times New Roman", 15), width=20, show="*").grid(
        column = 3, row = 3, sticky="w", columnspan= 2, padx=(10,0)
    )


    ## Option local
    ttk.Label(win, text = "Web:",
        font = ("Times New Roman", 14, "bold")).grid(column = 1, 
        row = 4, padx = (10,0), pady = 10, sticky="e")
    
    web = ttk.Combobox(win, width = 6, font=25, justify= "center", textvariable = tk.Listbox(), state="readonly")
    web['values'] = WEBS_LIST
    web.grid(column = 2, row = 4, pady=10) 
    web.current(0)


    ttk.Label(win, text = "Save Path:",
        font = ("Times New Roman", 14, "bold")).grid(column = 3, 
        row = 4, pady = 10)
    
    path = ttk.Entry(win, width = 13, font=12).grid(
        column = 4, row = 4, padx = (0,10), pady = 10
    )
    

    ## Option download
    ttk.Label(win, text = "Page:",
        font = ("Times New Roman", 14, "bold")).grid(column = 1, 
        row = 5, padx = (10,0), pady = 10, sticky="e")

    PAGE_LIST = list(range(1,11))
    page = ttk.Combobox(win, width = 6, font=14, justify= "center", textvariable = tk.Listbox(), state="disable")
    page['values'] = PAGE_LIST
    page.grid(column = 2, row = 5, pady=10) 
    page.current(0)


    ttk.Label(win, text = "Ward:",
        font = ("Times New Roman", 14, "bold")).grid(column = 3, 
        row = 5, pady = 10)
    
    ward = ttk.Combobox(win, width = 14, justify= "center", font=("Times New Roman",13, "bold"), textvariable = tk.Listbox(), state="readonly")
    ward['values'] = WARDS_LIST
    ward.grid(column = 4, row = 5, padx = (0,10), pady=10) 
    ward.current(0)


    ## Button
    load_action = tk.Button(
        win, text = "Load", bg = "Yellow", font = "25", width = 7, cursor="hand2",
        command = lambda: load() 
    )
    load_action.grid(row=6, column=1, pady=10, columnspan= 3)

    run_action = tk.Button(
        win, text = "Start", bg = "Green", state= "disabled", font = "25", width = 7, cursor="hand2",
        command = lambda: run() 
    )
    run_action.grid(row=6, column=4, pady=10, sticky="w")

    return user_name, password, web, path, page, ward, load_action, run_action

def app():
    win = tk.Tk()
    win.resizable(width=False, height=False)

    user_name, password, web, path, page, ward, load_action, run_action = process_theme(win=win)

    win.eval('tk::PlaceWindow . center')
    win.mainloop()

app()