import os
import time
import shutil

def get_by_latest_file(num: int, download_path: str):
    lst= [file for file in os.listdir(download_path) if os.path.isfile(os.path.join(download_path, file)) and file.lower().endswith('.pdf')]
    sorted_files = sorted(lst, key=lambda x: os.path.getmtime(os.path.join(download_path, x)), reverse=True)
    return sorted_files[:num]

def change_id(id: int, root: str, ward: str,page: str) -> int:
    target = f"{root}\\\\{ward}\\\\{page}"
    while True:
        if os.path.exists(f"{target}\\\\{id}"):
            id+=1
        else:
            break
    return id

def move_to_des(root:str, ward: str, page: str, id: str, file: str):
    target = f"{root}\\\\{ward}"
    if not os.path.exists(target):
        os.makedirs(target)
        time.sleep(0.5)
    target = f"{target}\\\\{page}"
    if not os.path.exists(target):
        os.makedirs(target)
    target = f"{target}\\\\{id}"
    if not os.path.exists(target):
        os.makedirs(target)
        time.sleep(0.5)
    shutil.move(f"{root}\\\\{file}",target)