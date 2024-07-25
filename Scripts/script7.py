from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import requests

def extract_pics(dir_path):
    s=Service("D:/ENSIAS/S2/Web scraping/Driver/chromedriver-win64/chromedriver-win64/chromedriver.exe") 
    driver=webdriver.Chrome(service=s)
    driver.get("https://rh.com/us/en/")
    time.sleep(5) 
    height=driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if height==new_height:
            break
        time.sleep(2)
        height=new_height
    img_elements = driver.find_elements(By.TAG_NAME, "img")
    os.makedirs(dir_path+"/images", exist_ok=True)
    with open(dir_path+"/image_links.txt", "w") as file:
        for i, element in enumerate(img_elements):

            img_url = element.get_attribute("src")
            if img_url:
                img_path = f"{dir_path}/images/image_{i}.jpg"
                with open(img_path, "wb") as img_file:
                    img_file.write(requests.get(img_url).content)
                file.write(f"{img_url}\n")
    driver.quit()
dir_path=r"D:\ENSIAS\S2\Web scraping\PFA2\StructurevF\https\rh.com\static"
extract_pics(dir_path)
