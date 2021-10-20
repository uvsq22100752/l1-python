#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    jour=temps[0]*86400
    heure=temps[1]*3600
    minute=temps[2]*60
    sec=temps[3]
    tempsEnSeconde=jour+heure+minute+sec
    return tempsEnSeconde

    
temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))  

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jours=int(seconde//86400)
   
    heures=int((seconde%86400)//3600)
   
    minutes=int((seconde)%3600//60)
    
    sec=int(seconde%temps[2])
    
    return jours,heures,minutes,sec

temps = secondeEnTemps(100000)

print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")




def afficheTemps(temps):
    if temps[0]>1:
        print(temps[0],"jours",end=" ")
    elif temps[0]==1:
        print(temps[0],"jour",end=" ")
    else:
        print(end="")
    if temps[1]>1:
        print(temps[1],"heures",end=" ")
    elif temps[1]==1:
        print(temps[1],"heure",end=" ")
    else:
        print(end="")
    if temps[2]>1:
        print(temps[2],"minutes",end=" ")
    elif temps[2]==1:
        print(temps[2],"minute",end=" ")
    else:
        print(end="")
    if temps[3]>1:
        print(temps[3],"secondes",end=" ")
    elif temps[3]==1:
        print(temps[3],"seconde",end=" ")
    else:
        print(end="  ")
    return ""


temps = ((1,0,14,23))    
print(afficheTemps(temps))  

#demande temps

def demandeTemps(demande):
    while True:
        
        j=int(input("Entre un nb de jours : "))
        if j<=30 and j>=1:
            h=int(input("entre un nb d'heures : "))
        if h<=24 and h>=1:
            m=int(input("entre un nb de minutes : "))
        if m<=60 and m>=1:
            s=int(input("entre un nb de secondes : "))
        if s<=60 and s>=1:
            return print(j,"jour(s)",h,"heure(s)",m,"minute(s)",s,"seconde(s)")
        else:
            print("erreur")
            break
demandeTemps(print)


#somme temps


#proportion temps 

def proportionTemps(pourcentage):
    nombreDeSec=tempsEnSeconde(temps3)
    propDesSec=nombreDeSec*prop
    resultat=secondeEnTemps(propDesSec)
    return print(resultat)

prop=0.2
temps3=(2,0,36,0)
proportionTemps(print)



