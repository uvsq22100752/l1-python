        if message.content.startswith('evo/'):   
            list1.append(message.content)
            nompoke9=list1[0][3:(len(list1[0]))]
            evo=""
            
            
            if nompoke9 in pokedex:
                nompoke10=nompoke9.lower()
                nompoke10=unidecode.unidecode(nompoke10)
                print(nompoke10)
                url = "https://www.pokepedia.fr/"+nompoke10

                response = requests.get(url)

                if response.ok:
                    soup=BeautifulSoup(response.text,"html.parser")
                    table = soup.findAll('table', class_="tableaustandard électrique")
                    carac1=[]
                    for img in table:
                        carac1.append(img.text.strip())
                    for i in range (0,(len(carac1))):
                        evo+=" "+carac1[i]
                        print(evo)
                    
                    print(evo)
                    await message.channel.send(evo.format(figurines))        

                else:
                    await message.channel.send("Erreur : Pokémon introuvable.".format(message))