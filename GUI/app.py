import os
import tkinter as tk

from GUI.load_web import load, run
from GUI.load_local import load_credential, close_application, \
    process_theme, select_save_path, disable_run

URL_PATH = "https://khh.mplis.gov.vn/dc/HoSoDiaChinh"
WEB_LIST = ["chrome","edge"]
WARD_LIST = ["thị trấn Vạn Giã","xã Vạn Bình","xã Vạn Hưng","xã Vạn Khánh","xã Vạn Phú","xã Vạn Phước",
            "xã Vạn Thạnh","xã Vạn Thắng","xã Vạn Thọ","xã Xuân Sơn","xã Đại Lãnh"]

def app():
    win = tk.Tk()
    win.title("Hồ Sơ Địa Chính")
    win.resizable(width=False, height=False)
    if os.path.exists("Images/icon.ico"):
        win.iconbitmap("Images/icon.ico")

    user_name, password, web, path, page, ward, time_delay, load_action, run_action = process_theme(win=win, web_list = WEB_LIST, ward_list = WARD_LIST)
    name_text, pw_text, url_text = load_credential()
    if name_text:
        select_save_path(item=user_name,value=name_text)
        select_save_path(item=password,value=pw_text)
        if url_text =="":
            url_text = URL_PATH

    cre = {
        "name": user_name.get(),
        "pw": password.get(),
        "url": url_text,
        "web": web.get(),
        "page": int(page.get()),
        "ward": ward.get(),
        "time_delay": int(time_delay.get())
    }

    load_action['command']= lambda: load(
        name=user_name.get(), pw = password.get(), 
        url=url_text, web= web.get(),
        path=path.get(),ward=ward.get(),
        time_delay=int(time_delay.get()),
        page=page, run_action=run_action
    )

    run_action['command'] = lambda: [
        run(
            path=path.get(),ward=ward.get(),
            time_delay=int(time_delay.get()),
            page=page
        ),
        disable_run(run_action)
    ]

    win.bind("<Control-KeyPress-q>", lambda event: close_application(win=win))
    win.bind("<Control-KeyPress-e>", lambda event: load(
            name=user_name.get(), pw = password.get(), 
            url=url_text, web= web.get(),
            path=path.get(),ward=ward.get(),
            time_delay=int(time_delay.get()),
            page=page, run_action=run_action
        )
    )
    win.bind("<Control-KeyPress-r>", lambda event: [
        run(
            path=path.get(),ward=ward.get(),
            time_delay=int(time_delay.get()),
            page=page
        ),
        disable_run(run_action)
    ])
    win.eval('tk::PlaceWindow . center')
    win.mainloop()