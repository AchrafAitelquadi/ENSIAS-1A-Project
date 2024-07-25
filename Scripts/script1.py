import subprocess
import pyautogui
import time 
import pandas as pd
from pathlib import Path
import requests

def dernierRepertoire(df,index,j):
    return df.iloc[:index,j].dropna().tolist()[-1]
    
def convertToRepertory():
    excel_file_path = r"C:\Users\dell\Desktop\indexability.xls"
    base_download_path =  r"C:\Users\dell\Desktop\rh"
    df = pd.read_excel(excel_file_path)
    for index , row in df.iterrows():
        for col_name, value in row.items():
            if col_name == "URLs":
                break
            if pd.isnull(value): #If the case is empty
                continue
            indice_colonne = df.columns.get_loc(col_name)#gets the index of the current column
            chemin = []
            for j in range(indice_colonne):
                chemin.append(dernierRepertoire(df,index,j))#we append the last not nan value of the row index and column j
            if len(chemin) == 0 or value.endswith("/"):
                chemin.append(value)
                cheminACreer = base_download_path + "".join(chemin)
                Path(cheminACreer).mkdir(parents=True, exist_ok=True)
            else:
                url = "https://"+"".join(chemin[1:])+value #downloading the files
                chemin.append(value)
                cheminACreer = base_download_path+"".join(chemin)
                response = requests.get(url)
                with open(cheminACreer,"wb") as f:
                    f.write(response.content)
                    
def calculate_relative_coordinate(x,y):#adjust the coordinates for all resolutions
    screen_width, screen_height = pyautogui.size()
    return int(x/1920 * screen_width), int(y/1080 * screen_height)

subprocess.Popen(r"C:\Users\Public\Desktop\Screaming Frog SEO Spider.lnk", shell=True)
time.sleep(22)
pyautogui.click(calculate_relative_coordinate(456,87))
pyautogui.typewrite("rh.com/us/en/")
time.sleep(5)
pyautogui.press('enter', presses = 2)
time.sleep(12)
pyautogui.click(calculate_relative_coordinate(1484,128))
pyautogui.click(calculate_relative_coordinate(1331,159),clicks=10,interval=0.5)
pyautogui.click(calculate_relative_coordinate(1446,161))
time.sleep(0.5)
pyautogui.click(calculate_relative_coordinate(677,648))
time.sleep(1)
pyautogui.click(calculate_relative_coordinate(716,582))
time.sleep(1)
pyautogui.click(calculate_relative_coordinate(1335,895))
time.sleep(0.5)
pyautogui.click(calculate_relative_coordinate(997,525))
convertToRepertory()