import requests
from bs4 import *

url = "https://pokestrat.io/fiche-pokemon/pikachu"

response = requests.get(url)

if response.ok:
    soup=BeautifulSoup(response.text,"html.parser")
    table = soup.findAll('table', class_='tableau-stat')
    carac=[]
    for tr in table:
        for td in tr:
            carac.append(td.text)
    print(carac)
    pv=carac[1]
    attaque=carac[3]
    defense=carac[5]
    attspe=carac[7]
    defspe=carac[9]
    vitesse=carac[11]
    print(pv)
    print(attaque)
    print(defense)
    print(attspe)
    print(defspe)
    print(vitesse)
    
    
    
            
            



 