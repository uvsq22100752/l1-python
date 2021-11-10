def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    l=[]
    while n!=1:
        if n%2==0:
            n=n/2
            l.append(n)
            
        else:
            n=(n*3)+1
            l.append(n)
        
    return (l)
print(syracuse(int(input("entre un nombre: "))))

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    
    for n in range (1,(n_max)):
       syracuse(n)
    return (True)

            
print(testeConjecture(10000))


def tempsVol(n):
    """ Retourne le temps de vol de n """
    tps=len(syracuse(n))
    return(tps)
    
print("Le temps de vol de", 3, "est", tempsVol(3))


def tempsVolListe(n_max2):
    a=[tempsVol(i) for i in range (1,n_max2)]
    return (a)

   

print(tempsVolListe(10000))



        

