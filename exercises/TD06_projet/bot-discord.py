import discord
from pokedex1 import *
from scraping import *
import unidecode

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            
            return
        
    
        #Commande  ->  /NomDuPokémon
        global list1
        list1=[]
        if message.content.startswith('/'):
            list1.append(message.content)
            
            if (str(list1[0])) in pokedex:
                a=str(list1[0])
                a="https://www.pokepedia.fr"+a
                await message.channel.send(a.format(message))    
            else:
                await message.channel.send("Erreur : Pokémon introuvable.".format(message))
                
                
                
        #Commande  ->  shiny/NomDuPokémon    
        if message.content.startswith('shiny/'):
            list1.append(message.content)
            nompoke=list1[0][5:(len(list1[0]))]

            if nompoke in pokedex:
                b=pokedex.index(nompoke)
                b+=1
                b="https://pokestrat.io/images/gif-animes/shiny/"+str(b)+".gif"
                await message.channel.send(b.format(message))   
            
            
                    
            elif nompoke in megaliste:
                nompoke=list1[0][5:(len(list1[0]))]
                mega=megaliste.index(nompoke)+10001
                mega="https://pokestrat.io/images/gif-animes/shiny/"+str(mega)+".gif"
                await message.channel.send(mega.format(message))
            
            else:
                await message.channel.send("Erreur : Pokémon introuvable.".format(message))        
        
        #Commande  ->  gif/NomDuPokémon 
        if message.content.startswith('gif/'):
            list1.append(message.content)
            nompoke2=list1[0][3:(len(list1[0]))]

            if nompoke2 in pokedex:
                c=pokedex.index(nompoke2)
                c+=1
                c="https://pokestrat.io/images/gif-animes/"+str(c)+".gif"
                await message.channel.send(c.format(message))        
            
            elif nompoke2 in megaliste:
                mega=megaliste.index(nompoke2)+10001
                mega="https://pokestrat.io/images/gif-animes/"+str(mega)+".gif"
                await message.channel.send(mega.format(message))
                
            else:
                await message.channel.send("Erreur : Pokémon introuvable.".format(message))
                
                
        ##Commande  ->  stats/NomDuPokémon   
        if message.content.startswith('stats/'):
            list1.append(message.content)
            nompoke3=list1[0][5:(len(list1[0]))]

            if nompoke3 in pokedex:
                nompoke4=nompoke3.lower()
                nompoke4=unidecode.unidecode(nompoke4)
                print(nompoke4)
                url = "https://pokestrat.io/fiche-pokemon/"+nompoke4

                response = requests.get(url)

                if response.ok:
                    soup=BeautifulSoup(response.text,"html.parser")
                    table = soup.findAll('table', class_='tableau-stat')
                    carac=[]
                    for tr in table:
                        for td in tr:
                            carac.append(td.text.strip())
                    
                    pv=carac[1]
                    attaque=carac[3]
                    defense=carac[5]
                    attspe=carac[7]
                    defspe=carac[9]
                    vitesse=carac[11]
                    
                    stat=pv+"     "+attaque+"     "+defense+"     "+attspe+"     "+defspe+"     "+vitesse
                    stat='*'+":bar_chart:"+" "+stat+" "+':bar_chart:'+'*'
                    await message.channel.send(stat.format(message))        
            
            else:
                await message.channel.send("Erreur : Pokémon introuvable.".format(message))  
            
            
        #Commandes  ->  maps
        
        if message.content.startswith('map/Kanto'):
            kanto="https://www.pokepedia.fr/images/4/44/Kanto_LGPE.png"
            await message.channel.send(kanto.format(message))

        if message.content.startswith('map/Johto'):
            johto="https://www.pokepedia.fr/images/f/f2/Johto_HGSS.jpg"
            await message.channel.send(johto.format(message))

        if message.content.startswith('map/Hoenn'):
            hoenn="https://www.pokepedia.fr/images/4/4c/Carte_de_Hoenn_ROSA.png"
            await message.channel.send(hoenn.format(message))

        if message.content.startswith('map/Sinnoh'):
            sinnoh="https://www.pokepedia.fr/images/9/99/Sinnoh-DEPS.png"
            await message.channel.send(sinnoh.format(message))

        if message.content.startswith('map/Unys'):
            unys="https://www.pokepedia.fr/images/a/ae/Unys_-_NB2.png"
            await message.channel.send(unys.format(message))

        if message.content.startswith('map/Kalos'):
            kalos="https://www.pokepedia.fr/images/a/ae/Unys_-_NB2.png"
            await message.channel.send(kalos.format(message))

        if message.content.startswith('map/Alola'):
            alola="https://www.pokepedia.fr/images/4/4d/Alola_-_USUL.png"
            await message.channel.send(alola.format(message))

        if message.content.startswith('map/Galar'):
            galar="https://www.pokepedia.fr/images/b/bc/Galar_-_EB.png"
            await message.channel.send(galar.format(message))   
            
            
        #Commande  ->  teams/NomDuPokémon
        
        if message.content.startswith('teams/'):
            list1.append(message.content)
            nompoke5=list1[0][5:(len(list1[0]))]
        
            if nompoke5 in pokedex:
                nompoke6=nompoke5.lower()
                nompoke6=unidecode.unidecode(nompoke6)
                e=pokedex.index(nompoke5)
                e+=1
                url="https://pokestrat.io/equipe"+nompoke6
                await message.channel.send(url.format(message))        
        
            else:
                await message.channel.send("Erreur : Pokémon introuvable.".format(message))  

        #Commande  ->  sheesh
        if message.content.startswith('!sheesh'):
            await message.channel.send('*SHHHHEEEEESHHHH @everyone*'.format(message))
            
            
        #Commande  ->  vinted    
        if message.content.startswith('!Vinted'):
            vinted="https://www.vinted.fr/member/34595386-nathangeck"
            await message.channel.send(vinted.format(message))
            
        if message.content.startswith('!Youtube'):
            ytb1="https://www.youtube.com/watch?v=AZSNu-V8CQw"
            ytb2="https://www.youtube.com/watch?v=1qyq9TZA5cQ"
            await message.channel.send(ytb1.format(message))
            await message.channel.send(ytb2.format(message))
        
        
        #Liste des Commandes
        if message.content.startswith("!command"):    
            await message.channel.send('*voilà la liste des commandes ! Amuse toi bien ;)*', file=discord.File("/Users/bellou/Desktop/command.txt"))


client = MyClient()
client.run("OTE4MTYwNDkxMjU0Mjc2MTM3.YbDNlw.4S4pJhy4TdlLfJGLx6Z04kFVTK8")




