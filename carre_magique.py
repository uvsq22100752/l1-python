carre_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
carre_pas_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,7,13]]

print(len(carre_mag))
print(carre_mag[0][1])


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

def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    transposed_carre = list(zip(*carre))
    return testLignesEgales(transposed_carre)
    
print("2")
print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))

def testDiagonalesEgales(carre3):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    diag1=carre3[0][0]+carre3[1][1]+carre3[2][2]+carre3[3][3]
    diag2=carre3[0][3]+carre3[1][2]+carre3[2][1]+carre3[3][0]
    sumdiag=diag1+diag2
    return (sumdiag)


print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))




def estCarreMagique(carre4):
    """ Renvoie True si c'est un carre magique et False sinon"""
    if testLignesEgales(carre4)==testColonnesEgales(carre4)==(testDiagonalesEgales(carre4)*2):
        print("True")
    else:
        print("False")
    return ""

print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))