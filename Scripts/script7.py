from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import requests

def extract_pics(dir_path):            #dir path ou on va stocker les images 
    s=Service("D:/ENSIAS/S2/Web scraping/Driver/chromedriver-win64/chromedriver-win64/chromedriver.exe") ##chemin du web driver
    driver=webdriver.Chrome(service=s)
    driver.get("https://rh.com/us/en/")
    time.sleep(5)  ##wait the page to load
    height=driver.execute_script("return document.body.scrollHeight")
    while True:
        print("h = ",height)  ##height of tne window what we can see
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        print("new h= ",new_height)
        if height==new_height:
            break
        time.sleep(2)
        height=new_height

    # Récupérer les éléments img
    img_elements = driver.find_elements(By.TAG_NAME, "img")
    print("len = ",len(img_elements))

    # Créer un répertoire pour stocker les images
    os.makedirs(dir_path+"/images", exist_ok=True)

    # Parcourir les éléments img
    with open(dir_path+"/image_links.txt", "w") as file:
        for i, element in enumerate(img_elements):
            # Obtenir le lien de l'image
            img_url = element.get_attribute("src")
            if img_url:
                # Télécharger l'image
                img_path = f"{dir_path}/images/image_{i}.jpg"
                with open(img_path, "wb") as img_file:
                    img_file.write(requests.get(img_url).content)
                # Enregistrer le lien de l'image dans un fichier
                file.write(f"{img_url}\n")
                print(f"Image {i} téléchargée et enregistrée à {img_path}")

    # Fermer le navigateur
    driver.quit()
    
    
dir_path=r"D:\ENSIAS\S2\Web scraping\PFA2\StructurevF\https\rh.com\static"
extract_pics(dir_path)