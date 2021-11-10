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
            
    
    else:
        print(l)
        print("fin")
    return ""

print(syracuse(int(input("entre un nombre: "))))

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    
    for n in range (2,(n_max)):
        if syracuse(n)==1.0:
            continue
    return ""
        
            
print(testeConjecture(10000))
        
            
            
