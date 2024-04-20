import tkinter as tk
from pathlib import Path

from load_web import load, run
from load_local import load_credential, close_application, process_theme, select_save_path

DOWNLOAD_PATH = str(Path.home() / "Downloads")
WEB_LIST = ["chrome","edge"]
WARD_LIST = ["thị trấn Vạn Giã","xã Vạn Bình","xã Vạn Hưng","xã Vạn Khánh","xã Vạn Phú","xã Vạn Phước",
            "xã Vạn Thạnh","xã Vạn Thắng","xã Vạn Thọ","xã Xuân Sơn","xã Đại Lãnh"]

def app():
    win = tk.Tk()
    win.resizable(width=False, height=False)

    user_name, password, web, path, page, ward, time_delay, load_action, run_action = process_theme(win=win, web_list = WEB_LIST, ward_list = WARD_LIST)
    name_text, pw_text, url_text = load_credential()
    if name_text:
        select_save_path(item=user_name,value=name_text)
        select_save_path(item=password,value=pw_text)
        if url_text =="":
            url_text = DOWNLOAD_PATH

    win.bind("<Control-KeyPress-q>", lambda event: close_application(win=win))
    win.eval('tk::PlaceWindow . center')
    win.mainloop()

app()