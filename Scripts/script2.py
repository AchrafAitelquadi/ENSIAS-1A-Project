from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

def url_dict():
    s=Service("D:/ENSIAS/S2/Web scraping/Driver/chromedriver-win64/chromedriver-win64/chromedriver.exe") ##chemin du web driver
    driver=webdriver.Chrome(service=s)
    url="https://rh.com/us/en/"
    driver.get(url)
    time.sleep(5)
    not_products=["All Living Sale","Seating Collections","All Dining Sale","All Dining Tables","All Dining Seating","All Bed Sale","Bedroom Collections","All Bath Sale","Bath Collections","All Outdoor Sale","Furniture Collections","All Lighting Sale","All Textiles Sale","Bedding Collections","All Rugs Sale","All Decor Sale","Drapery Collections"]
    my_dict={}
    sale=driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/header/div[1]/div/div[2]/ul/li[12]")
    sale.click()
    time.sleep(1)
    for i in range(1,10):
        products_dict={}
        categorie=driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/header/div[1]/div/div[2]/ul/div[12]/div/div/div/div/div[1]/ul/li["+str(i)+"]/span")
        categorie.click()
        categorie_name=categorie.text
        j=1
        while True:
            try:
                product=driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/header/div[1]/div/div[2]/ul/div[12]/div/div/div/div/div[2]/ul/a["+str(j)+"]")        
            except:
                try:
                    product=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/header/div[1]/div/div[2]/ul/div[12]/div/div/div/div/div[2]/ul/a["+str(j)+"]")
                except:
                    break
            product_name=product.text
            j=j+1
            if product_name in not_products:
                continue
            found = any(inner_dict.get(product_name) for inner_dict in my_dict.values())
            if found:
                continue   
            current_url=product.get_attribute('href')
            products_dict[product_name] = current_url
        my_dict[categorie_name]=products_dict
    driver.quit()
    return my_dict

