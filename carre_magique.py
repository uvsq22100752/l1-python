carre_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
carre_pas_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,7,13]]

print(len(carre_mag))


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    
    for i in range (0,4):
        
        print(carre[i])
        
    
print("carré magique: ")
afficheCarre(carre_mag)
print("carré pas magique: ")
afficheCarre(carre_pas_mag)


def testLignesEgales(carre2):
    
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    a=sum(carre2[0])
    b=sum(carre2[1])
    c=sum(carre2[2])
    d=sum(carre2[3])
    z=a+b+c+d
    if a==b==c==d:
        return (z)
    else:
        return("-1")
    

print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))

