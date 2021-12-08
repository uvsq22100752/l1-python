import requests
from bs4 import *


url = "https://pokestrat.io/fiche-pokemon/pikachu"

response = requests.get(url)

if response.ok:
   soup=BeautifulSoup(response.text,"html.parser")
   table = soup.findAll('table', class_='tableau-stat')
   for i in range (5):
      for tr in table:
         vitesse= tr.td.text

         print(vitesse)

pv=carac[4]
    attaque=carac[5]
    defense=carac[6]
    attspe=carac[7]
    defspe=carac[8]
    vitesse=carac[9]
    
     for tr in table:
        for td in tr:
            carac.append(td.text)
    print(carac)
    