from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

s=Service("D:/ENSIAS/S2/Web scraping/Driver/chromedriver-win64/chromedriver-win64/chromedriver.exe")
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent}")   

def extract_files(hrefs,dir_path,driver):
    i=0
    for href in hrefs:
        dirs = href.split("/") 
        dirs.pop(1)
        dirs[0]="https"
        # Construire le chemin du fichier 
        file_path = dir_path+"\\"+os.path.join(*dirs)
        print("file path = ",file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        driver.get(href)
        displayed_content = driver.find_element(By.TAG_NAME,'body').text
        try:
            with open(file_path.replace("\\", "/"), "w", encoding="utf-8") as file:
                file.write(displayed_content)    
        except:
            dirs[-1]="jsi"+str(i)+".js"
            i=i+1    
            file_path=dir_path+"\\"+os.path.join(*dirs)
            with open(file_path.replace("\\", "/"), "w", encoding="utf-8") as file:
                file.write(displayed_content)
        print("file path vf =",file_path)
        
def extract_js(dir_path):
    driver = webdriver.Chrome(service=s,options=options)
    driver.get("https://rh.com/us/en/")    
    elements = driver.find_elements(By.CSS_SELECTOR, "link[as='script']")
    print(len(elements))
    js_hrefs=[element.get_attribute("href") for element in elements]
    extract_files(js_hrefs,dir_path,driver)
    driver.get("https://rh.com/us/en/")
    js_elements = driver.find_elements(By.TAG_NAME, "script")
    elements_with_src = []
    for element in js_elements:
        if element.get_attribute("src"):
            elements_with_src.append(element)
    js_srcs=[element.get_attribute("src") for element in elements_with_src]
    extract_files(js_srcs,dir_path,driver)
    driver.quit()
