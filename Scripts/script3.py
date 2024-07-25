from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import json

website_links = {  "Living" : {
                            "Sofas" : "https://rh.com/us/en/catalog/category/products.jsp?categoryId=cat24730069&pgterm=Sofas&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&sale=true&topCatId=cat3890154&parentCatId=cat160024",
                            "Sectionals" : "https://rh.com/us/en/catalog/category/products.jsp?cellBackground=false&categoryId=cat28710017&cm_vc=sale&sale=true&filter=sale&clientrender=true&topCatId=cat160024&parentCatId=cat8750009&pgterm=category%3Acat28710017&topCatId=cat3890154&parentCatId=cat160024",
                            "Fabric Chairs" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Fabric+Chairs&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat10210007&sale=true&topCatId=cat3890154&parentCatId=cat160024",
                            "Leather Chairs" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Leather+Chairs&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat10210015&sale=true&topCatId=cat3890154&parentCatId=cat160024",
                            "Coffee Tables" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Coffee+Tables&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&sale=true&categoryId=cat10180118&topCatId=cat3890154&parentCatId=cat160024",
                            "Side Tables" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Side+Tables&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat10180100&sale=true&topCatId=cat3890154&parentCatId=cat160024",
                            "Console Tables" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Console+Tables&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat10180123&sale=true&topCatId=cat3890154&parentCatId=cat160024",
                            "Sideboards" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Sideboards&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat16820001&topCatId=cat3890154&parentCatId=cat160024",
                            "Media Consoles" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Media+Consoles&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat16840016&sale=true&topCatId=cat3890154&parentCatId=cat160024",
                            "Cabinets" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Cabinets&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat10180087&topCatId=cat3890154&parentCatId=cat160024",
                            "Desks" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Desks&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat10180124&sale=true&topCatId=cat3890154&parentCatId=cat160024"
                },
                "Dining" : {
                            "Bar & Counter Stools" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Bar+and+Counter+Stools&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat10220057&topCatId=cat3890154&parentCatId=cat1840042",
                            "Sideboards" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Sideboards&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat16820001&topCatId=cat3890154&parentCatId=cat1840042",
                            "Sideboard & Hutches" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Sideboard+andShelving+Hutches&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat10180110&topCatId=cat3890154&parentCatId=cat1840042",
                            "Cabinets" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Cabinets&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat10180087&topCatId=cat3890154&parentCatId=cat1840042",
                            "Shelving" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Open+Shelving&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat10180094&topCatId=cat3890154&parentCatId=cat1840042"
            },
                 "Bed" : {
                            "Beds" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+All+Beds&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat26780018&topCatId=cat3890154&parentCatId=cat780002",
                            "Nightstands" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Nightstands&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat10240093&topCatId=cat3890154&parentCatId=cat780002",
                            "Bedside Tables" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Bedside+Tables&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat14310001&topCatId=cat3890154&parentCatId=cat780002",
                            "Dressers" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Dressers&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat10240094&topCatId=cat3890154&parentCatId=cat780002",
                            "Armoires" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Armoires&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat16610010&topCatId=cat3890154&parentCatId=cat780002",
                            "Benches" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Benches&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat15600003&topCatId=cat3890154&parentCatId=cat780002",
                            "Stools" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Stools&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat16570006&topCatId=cat3890154&parentCatId=cat780002"  
            },
                "Bath" : {
                            "Vanities" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+All+Vanities&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat24970030&sale=true&topCatId=cat3890154&parentCatId=cat160092",
                            "Washstands" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+All+Washstands&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat25110037&sale=true&topCatId=cat3890154&parentCatId=cat160092",
                            "Cabinets" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Bath+Cabinets&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat10250051&sale=true&topCatId=cat3890154&parentCatId=cat160092",
                            "Mirrors & Medicine Cabinets" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=category%3Acat11580013&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&sale=true&categoryId=cat11580013&topCatId=cat3890154&parentCatId=cat160092",
                            "Stools" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Stools&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat16570006&topCatId=cat3890154&parentCatId=cat160092",
                            "Bath Lighting" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+All+Bath+Lighting&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat4980014&sale=true&topCatId=cat3890154&parentCatId=cat160092",
                            "Bath Towels" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=category%3Acat30290005&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat30290005&topCatId=cat3890154&parentCatId=cat160092",
                            "Sink Faucets" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Sink+Faucet+Sets&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat1520015&sale=true&topCatId=cat3890154&parentCatId=cat160092",
                            "Tub Fills" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Bath+Tub+Fill+Sets&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat12330001&sale=true&topCatId=cat3890154&parentCatId=cat160092",
                            "Shower Systems" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Shower+Systems+and+Door+Pulls&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat3850062&sale=true&topCatId=cat3890154&parentCatId=cat160092",
                            "Mounted Hardware" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Mounted+Hardware+and+Shelves&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat780011&sale=true&topCatId=cat3890154&parentCatId=cat160092",
                            "Bath Accessories" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Bath+Accessories&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat1679022&sale=true&topCatId=cat3890154&parentCatId=cat160092",
                            "Cabinet Hardware" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+All+Cabinet+Hardware+and+Hooks&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat10710164&sale=true&topCatId=cat3890154&parentCatId=cat160092"
            },
                "Outdoor" : {
                            "Sofas" : "https://rh.com/us/en/outdoor/catalog/category/products.jsp?pgterm=outdoor+sofas&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat25900016&topCatId=cat3890154&parentCatId=cat180003",
                            "Chairs" : "https://rh.com/us/en/outdoor/catalog/category/products.jsp?pgterm=RH+Outdoor+Chairs&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat16250001&topCatId=cat3890154&parentCatId=cat180003",
                            "Coffee Tables" : "https://rh.com/us/en/outdoor/catalog/category/products.jsp?pgterm=RH+Outdoor+Coffee+Tables&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat3090004&topCatId=cat3890154&parentCatId=cat180003",
                            "Side Tables" : "https://rh.com/us/en/outdoor/catalog/category/products.jsp?pgterm=RH+Outdoor+Side+and+Console+Tables&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat14650097&topCatId=cat3890154&parentCatId=cat180003",
                            "Dining Tables" : "https://rh.com/us/en/outdoor/catalog/category/products.jsp?pgterm=RH+Outdoor+Dining+Tables&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat6610131&topCatId=cat3890154&parentCatId=cat180003",
                            "Dining Chairs" : "https://rh.com/us/en/outdoor/catalog/category/products.jsp?pgterm=RH+Outdoor+Dining+Chairs&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat10880022&topCatId=cat3890154&parentCatId=cat180003",
                            "Bar & Counter" : "https://rh.com/us/en/outdoor/catalog/category/products.jsp?pgterm=RH+Outdoor+Bar+and+Counter&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat11110001&topCatId=cat3890154&parentCatId=cat180003",
                            "Chaises" : "https://rh.com/us/en/search/results.jsp?Ntt=outdoor%20chaises&N={!tag%3Dsku_showOnly}sku_showOnly:(%22Sale%22)&Ns=&topCatId=cat3890154&parentCatId=cat180003",
                            "Daybeds" : "https://rh.com/us/en/search/results.jsp?Ntt=outdoor%20daybed&N={!tag%3Dsku_showOnly}sku_shttps://rh.com/us/en/outdoor/catalog/category/products.jsp?pgterm=RH+All+Outdoor+Pillows&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat17870001&topCatId=cat3890154&parentCatId=cat180003howOnly:(%22Sale%22)&Ns=&topCatId=cat3890154&parentCatId=cat180003",
                            "Ottomans" : "https://rh.com/us/en/search/results.jsp?Ntt=outdoor%20ottomans&N={!tag%3Dsku_showOnly}sku_showOnly:(%22Sale%22)&Ns=&topCatId=cat3890154&parentCatId=cat180003",
                            "Mirrors" : "https://rh.com/us/en/outdoor/catalog/category/products.jsp?pgterm=OD+Mirrors&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat26010005&topCatId=cat3890154&parentCatId=cat180003",
                            "Outdoor Pillows" : "https://rh.com/us/en/outdoor/catalog/category/products.jsp?pgterm=RH+All+Outdoor+Pillows&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat17870001&topCatId=cat3890154&parentCatId=cat180003",
                            "Outdoor Towels" : "https://rh.com/us/en/outdoor/catalog/category/products.jsp?pgterm=RH+Outdoor+Beach+and+Pool+Towels&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat2340004&topCatId=cat3890154&parentCatId=cat180003"
            },
                "Lighting" : {
                            "Ceiling Lighting" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Ceiling+Lighting&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat3850076&topCatId=cat3890154&parentCatId=cat160075",
                            "Wall Lighting" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+All+Wall+Lighting&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat3900062&topCatId=cat3890154&parentCatId=cat160075",
                            "Table Lighting" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+All+Table+Lighting&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat3860007&topCatId=cat3890154&parentCatId=cat160075",
                            "Floor Lighting" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+All+Floor+Lighting&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat3900063&topCatId=cat3890154&parentCatId=cat160075",
                            "Bath Lighting" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+All+Bath+Lighting&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat4980014&topCatId=cat3890154&parentCatId=cat160075",
                            "Outdoor Lighting" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=Interiors+All+Outdoor+Lighting&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=&categoryId=cat10230003&topCatId=cat3890154&parentCatId=cat160075"
            },
                "Bedding" : {
                            "Duvet Covers & Shams" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Duvet+Covers+and+Shams&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat1860011&sale=true&topCatId=cat3890154&parentCatId=cat9750013",
                            "Sheets & Pillowcases" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Sheets+and+Pillowcases&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat90041&sale=true&topCatId=cat3890154&parentCatId=cat9750013",
                            "Quilts & Coverlets" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=All+Quilts+and+Coverlets&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat26360016&sale=true&topCatId=cat3890154&parentCatId=cat9750013"
            },
                "Rugs" : {
                            "Neutral Rugs" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Natural+Rugs&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat27580024&sale=true&topCatId=cat3890154&parentCatId=cat1535014",
                            "Grey Rugs" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Grey+Rugs&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat27580026&sale=true&topCatId=cat3890154&parentCatId=cat1535014",
                            "Ivory Rugs" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Ivory+Rugs&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat27580025&sale=true&topCatId=cat3890154&parentCatId=cat1535014",
                            "Brown Rugs" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Brown+Rugs&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat27580029&sale=true&topCatId=cat3890154&parentCatId=cat1535014",
                            "Black Rugs" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Black+Rugs&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat27580028&sale=true&topCatId=cat3890154&parentCatId=cat1535014",
                            "Blue Rugs" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Blue+Rugs&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat27580027&sale=true&topCatId=cat3890154&parentCatId=cat1535014"
            },
                "Décor" : {
                            "Mirrors" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+All+Mirrors&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat10180012&sale=true&topCatId=cat3890154&parentCatId=cat1630014",
                            "Wall Art" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Decor+All+Wall+Art&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat26600072&sale=true&topCatId=cat3890154&parentCatId=cat1630014",
                            "Decorative Accents" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+All+Decorative+Accents&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat10180024&sale=true&topCatId=cat3890154&parentCatId=cat1630014",
                            "Cabinet Hardware" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+All+Cabinet+Hardware+and+Hooks&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat10710164&sale=true&topCatId=cat3890154&parentCatId=cat1630014",
                            "Throws & Blankets" : "https://rh.com/us/en/search/results.jsp?Ntt=throws&N={!tag%3Dsku_showOnly}sku_showOnly:(%22Sale%22)&Ns=product.sale%7C1&topCatId=cat3890154&parentCatId=cat1630014",
                            "Pillows" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Pillows&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat16900100&sale=true&topCatId=cat3890154&parentCatId=cat1630014",
                            "Bar Cabinets & Carts" : "https://rh.com/us/en/catalog/category/products.jsp?pgterm=RH+Bar+Carts+and+Cabinets&N=%7B%21tag%3Dsku_showOnly%7Dsku_showOnly%3A%28%22Sale%22%29&Ns=product.sale%7C1&categoryId=cat10180046&sale=true&topCatId=cat3890154&parentCatId=cat1630014"
            }
}
s = Service("C:/Users/dell/Desktop/chromedriver-win64/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",
                                    True)
driver = webdriver.Chrome(options=options,
                            service=s)
data = {
        "Living" : {},
        "Dining": {},
        "Bed" : {},
        "Bath" : {},
        "Outdoor" : {},
        "Lighting" : {},
        "Bedding" : {},
        "Rugs" : {},
        "Décor" : {}
    }
def scrape_by_category(category):
    dicti = website_links[category]
    for key, url in dicti.items():
        driver.get(url)
        time.sleep(2)
        try :
            driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div[4]/div/div[2]/div/p[2]").click()
            driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/ul/li[4]").click()
        except :
            pass
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        html_list_element = driver.find_elements(By.CSS_SELECTOR, "a.relative") 
        name = {category : []}
        data[category][key] = []
        for item in html_list_element :
            item_split = item.text.split("\n")
            if "Available" not in item_split[0]:
                name_product = item_split[0]
                try : 
                    member_price = item_split[3]
                    regular_price = item_split[5]
                except : 
                    continue
            else:
                name_product = item_split[1]
                if name_product not in name[category]:
                    name[category].append(name_product)
                    try : 
                        member_price = item_split[4]
                        regular_price=item_split[6]
                    except : 
                        continue
                else:
                    continue
            data[category][key].append({
                "Name" : name_product,
                "Member Price" : member_price,
                "Regular Price " : regular_price
            })
def main():
    for category in website_links:
        scrape_by_category(category)
    with open("donnee.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
if __name__ == "__main__" :
    main()
    driver.quit()
