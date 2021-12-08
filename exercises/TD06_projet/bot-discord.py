import discord
from pokedex.py import 

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
        pokedex=['/raichu','/pikachu']
        if message.content.startswith('/'):
            list1.append(message.content)
            
            if (str(list1[0])) in pokedex:
                a=str(list1[0])
                a="https://www.pokepedia.fr"+a
                await message.channel.send(a.format(message))

        else:
            if message.content.startswith('!hello'):
                await message.channel.send('Hello {0.author.mention}'.format(message))
            if message.content.startswith('!sheesh'):
                await message.channel.send('SHHHHEEEEESHHHH {0.author.mention}'.format(message))
            
        

client = MyClient()
client.run("OTE4MTYwNDkxMjU0Mjc2MTM3.YbDNlw.IKy95_vhiyfCPHJ1pxw81WVKUgE")

