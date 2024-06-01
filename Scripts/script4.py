from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

s=Service("D:/ENSIAS/S2/Web scraping/Driver/chromedriver-win64/chromedriver-win64/chromedriver.exe") ##chemin du web driver
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent}")    

def remove_duplicate_files(download_dir):
    for file_name in os.listdir(download_dir):
        #print(file_name)
        if file_name.endswith(" (1).otf"):
            file_path = os.path.join(download_dir, file_name)
            os.remove(file_path)
            #print(f"Fichier supprimé : {file_path}")

#\fonts22"
def fonts(dir_path):            # chemin ou on va creer le repertoire fonts pour enregistrer les fonts qui existent
    dir_path=dir_path+"/https/rh.com/fonts"
    #print(dir_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)  #cree le rep s'il n'existe pas 
    options.add_experimental_option("prefs", {
    "download.default_directory": os.path.normpath(dir_path),  # repertoire de telechargement par defaut
    "download.prompt_for_download": False  # Ne pas demander où enregistrer les fichiers
    })

    driver = webdriver.Chrome(service=s,options=options)

    driver.get("https://rh.com/us/en/")
    
    # Attendre que le logo du site soit visible
    time.sleep(10)
    elements = driver.find_elements(By.CSS_SELECTOR, "link[rel='preload']")
    # Filtrer les éléments pour ne garder que ceux avec as="font"
    font_elements = [element for element in elements if element.get_attribute("as") == "font"]
    
    for element in font_elements:
        #html_element=element.get_attribute("outerHTML")
        href = element.get_attribute("href")
        driver.get(href)
        #extraire le nom du font depuis href
        segments = href.split("/")
        font_name=segments[-1]   # le nom du fichier a enregistrer = nom du font
        
        file_path=dir_path+"/"+font_name
        driver.get(href)
        time.sleep(1)

    remove_duplicate_files(dir_path) # suppriemer les doublons
    driver.quit()

