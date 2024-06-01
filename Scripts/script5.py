from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

s=Service("D:/ENSIAS/S2/Web scraping/Driver/chromedriver-win64/chromedriver-win64/chromedriver.exe") ##chemin du web driver
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent}")   

def extract_files(hrefs,dir_path,driver):   # les fichiers exterieurs
    i=0
    for href in hrefs:
        dirs = href.split("/")
        # Supprimer le deuxième élément vide 
        dirs.pop(1)
        dirs[0]="https"     #not https:
        #print(dirs)
        
        # Construire le chemin du fichier 
        file_path = dir_path+"\\"+os.path.join(*dirs)   ##  pour creer les repertoires parents s'ils manquent
        print("file path = ",file_path)
        # Créer les répertoires parents si nécessaire
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        driver.get(href)
        
        # Récupérer le contenu affiché à l'écran
        displayed_content = driver.find_element(By.TAG_NAME,'body').text
        # Enregistrer le contenu affiché dans un fichier
        try:
            with open(file_path.replace("\\", "/"), "w", encoding="utf-8") as file:
                file.write(displayed_content)    
        except:  # si le fichier a un nom non valide (probleme dans js fichiers) => on le donne un nom aleatoire
            dirs[-1]="jsi"+str(i)+".js"
            i=i+1    
            file_path=dir_path+"\\"+os.path.join(*dirs)
            with open(file_path.replace("\\", "/"), "w", encoding="utf-8") as file:
                file.write(displayed_content)
        print("file path vf =",file_path)
        
def extract_js(dir_path):
    ## extract Js files
    driver = webdriver.Chrome(service=s,options=options)
    driver.get("https://rh.com/us/en/")    
    elements = driver.find_elements(By.CSS_SELECTOR, "link[as='script']")
    print(len(elements))
    js_hrefs=[element.get_attribute("href") for element in elements]
    #print(js_hrefs)
    extract_files(js_hrefs,dir_path,driver)
    
    driver.get("https://rh.com/us/en/")
    
    js_elements = driver.find_elements(By.TAG_NAME, "script")
    
    # Séparer les éléments avec href des autres éléments
    elements_with_src = []      #ont un fichier source
    #elements_with_jsCode = []   #<script> code </script>
    for element in js_elements:
        if element.get_attribute("src"):
            elements_with_src.append(element)
        # else:
        #     elements_with_jsCode.append(element)         
    # print("Elements avec href :",len(elements_with_src))
    # print("\nAutres éléments :",len(elements_with_jsCode))

    js_srcs=[element.get_attribute("src") for element in elements_with_src]
    # elements_with_jsCode=[element.get_attribute("innerHTML") for element in elements_with_jsCode]
    extract_files(js_srcs,dir_path,driver)
    
    # file_name="jsCode.js"
    # file_path=os.path.normpath(dir_path+"/https/rh.com/static/js"+"\\"+file_name)
    # #print(file_path)
    # write_file(elements_with_jsCode,file_path) 
    driver.quit()