import discord

from pokedex1 import *

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
        if message.content.startswith('shiny/'):
            list1.append(message.content)
            nompoke=list1[0][5:(len(list1[0]))]

        if nompoke in pokedex:
            b=pokedex.index(nompoke)
            b+=1
            b="https://pokestrat.io/images/gif-animes/shiny/"+str(b)+".gif"
            await message.channel.send(b.format(message))        
        if nompoke not in pokedex:
            await message.channel.send("Erreur : Pokémon introuvable.".format(message))        
        
        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
        if message.content.startswith('!sheesh'):
            await message.channel.send('SHHHHEEEEESHHHH {0.author.mention}'.format(message))
                
client = MyClient()
client.run("OTE4MTYwNDkxMjU0Mjc2MTM3.YbDNlw.2NGRbaZmvuxuS4Ju3zdIQc2nJHc")

