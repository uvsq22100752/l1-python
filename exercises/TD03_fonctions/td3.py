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
