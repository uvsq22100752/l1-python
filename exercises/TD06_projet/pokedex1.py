pokedex=[]

file = open("/Users/bellou/Desktop/unt.txt", "r")

lines = file.readlines()

file.close()

for line in lines:
   a='/'+line.strip()
   pokedex.append(a)
print(pokedex)