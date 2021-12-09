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
    stat=pv+attaque+defense+attspe+defspe+vitesse
    print(stat)
    
    Liste des commandes du Bot-Pokémon:

#Tout les nom de Pokémon sont a écrires avec une majuscule !

Pour afficher des info sur un Pokémon:
	/NomDuPokémon
	exemple: /Piafabec

Pour afficher la version shiny d’un Pokémon:
	shiny/NomDuPokémon
	exemple: shiny /Grolem

Pour afficher un gif d’un Pokémon:
	gif/NomDuPokémon
	exemple: gif/Métamorph

Pour afficher les stats d’un Pokémon:
	stats/NomDuPokémon
	exemple: Magicarpe

Pour afficher la map d’une région:
	map/NomDeLaRégion
	exemple: map/Sinnoh

Pour afficher des équipes possibles avec un Pokémon:
	teams/NomDuPokémon
	exemple: teams/Flabébé

    
    
            
            



 