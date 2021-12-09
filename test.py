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
    
await message.channel.send(Liste des commandes du Bot-Pokémon:

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

	.format(message))