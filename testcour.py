if message.content.startswith('/'):
    list1.append(message.content)
            
    if (str(list1[0])) in pokedex:
            a=str(list1[0])
            a="https://www.pokepedia.fr"+a
            await message.channel.send(a.format(message))

if message.content.startswith('/shiny.'):
    list1.append(message.content)
    
    shiny=pokedex.index((str(list1[0])))
    shiny="https://pokestrat.io/images/gif-animes/shiny/"+shiny+".gif"
    await message.channel.send(shiny.format(message))