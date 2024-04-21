import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from typing import Tuple, List

def load_credential() -> List[str]:
    list_txt = []
    for file in os.listdir("."):
        if file.endswith(".txt") and os.path.isfile(os.path.join(".", file)):
            list_txt.append(file)
    if "requirements.txt" in list_txt:
        list_txt.remove("requirements.txt")
    for file_path in list_txt:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines if line.strip()]
            lines = [line.replace('\n', '') for line in lines]
            if len(lines)>1 and (len(lines)<4):
                name_text, pw_text = lines[:2]
                url_text = lines[2] if len(lines) > 2 else ""
                return name_text, pw_text, url_text
    return "","",""

def close_application(win: tk.Tk):
    win.destroy()

def select_save_path(item: ttk.Entry, value: str = None):
    if value:
        save_path = value
    else:
        save_path = filedialog.askdirectory()
    item.delete(0, tk.END)
    item.insert(tk.END, save_path)

def process_theme(win: tk.Tk,
                  web_list: List[str],
                  ward_list: List[str]
                  ) -> Tuple[
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
    
    user_name = ttk.Entry(win, font=("Times New Roman", 15), width=20)
    user_name.grid(
        column = 3, row = 2, sticky="w", columnspan= 2, padx=(10,0)
    )

    password = ttk.Entry(win, font=("Times New Roman", 15), width=20, show="*")
    password.grid(
        column = 3, row = 3, sticky="w", columnspan= 2, padx=(10,0)
    )


    ## Option local
    ttk.Label(win, text = "Web:",
        font = ("Times New Roman", 14, "bold")).grid(column = 1, 
        row = 4, padx = (10,0), pady = 10, sticky="e")
    
    web = ttk.Combobox(win, width = 6, font=25, justify= "center", textvariable = tk.Listbox(), state="readonly")
    web['values'] = web_list
    web.grid(column = 2, row = 4, pady=10) 
    web.current(0)


    ttk.Label(win, text = "Save Path:",
        font = ("Times New Roman", 14, "bold")).grid(column = 3, 
        row = 4, pady = 10)

    path = ttk.Entry(win, font=("Times New Roman", 13), width = 13)
    path.grid(
        column = 4, row = 4, pady = 10, sticky="w"
    )
    browse_button = ttk.Button(win, text="...", width=5, command=lambda: select_save_path(item=path))
    browse_button.grid(column=4, row=4, padx=(0, 10), sticky="e")


    ## Option download
    ttk.Label(win, text = "Page:",
        font = ("Times New Roman", 14, "bold")).grid(column = 1, 
        row = 6, padx = (10,0), pady = 10, sticky="e")

    PAGE_LIST = list(range(1,11))
    page = ttk.Combobox(win, width = 6, font=14, justify= "center", textvariable = tk.Listbox(), state="disable")
    page['values'] = PAGE_LIST
    page.grid(column = 2, row = 6, pady=10) 
    page.current(0)


    ttk.Label(win, text = "Ward:",
        font = ("Times New Roman", 14, "bold")).grid(column = 3, 
        row = 6, pady = 10)
    
    ward = ttk.Combobox(win, width = 14, justify= "center", font=("Times New Roman",13, "bold"), textvariable = tk.Listbox(), state="readonly")
    ward['values'] = ward_list
    ward.grid(column = 4, row = 6, padx = (0,10), pady=10) 
    ward.current(0)

    ## Time_delay
    ttk.Label(win, text = "Time_delay:",
        font = ("Times New Roman", 12, "bold")).grid(column = 1, 
        row = 7, pady = 10, columnspan= 2, sticky="w", padx=(10,0))
    time_delay = ttk.Entry(win, font=("Times New Roman", 13), width = 4)
    time_delay.grid(row=7, column=1, sticky="e", columnspan= 2, padx=(0,10))
    time_delay.insert(0, "10")

    ## Button
    load_action = tk.Button(
        win, text = "Load", bg = "Yellow", font = "25", width = 7, cursor="hand2"
    )
    load_action.grid(row=7, column=3, pady=10)

    run_action = tk.Button(
        win, text = "Start", bg = "Red", state= "disabled", font = "25", width = 7
    )
    run_action.grid(row=7, column=4, pady=10)

    return user_name, password, web, path, page, ward, time_delay, load_action, run_action