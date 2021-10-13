
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