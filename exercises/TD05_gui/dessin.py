import tkinter as tk    
from tkinter import messagebox
import random as r 

randomcolor=["yellow","black","blue","red"]
#créartion de la fenêtre 
root = tk.Tk()
root.title("Mon dessin")
root.geometry("600x600")
canvas = tk.Canvas(root, width = 600, height = 600,bg="black",highlightbackground="red",selectborderwidth=5,relief="groove")
def color():
    while True:
        print("white, black, red, green, blue, cyan, yellow")
        a=input("Choisi une couleur parmis celle ci-dessus :")        
        if a=="white" or "black" or "red" or "green" or "blue" or "cyan" or "yellow":
            
            break
    return (a)
        
#création du cercle,carre et croix + coodonées 
                     
def cercle():
    x0 = r.randint(1,600)
    y0 = r.randint(1,600)
    canvas.create_oval(y0, x0, y0 -100 , x0 -100, outline=a,fill=a)
    
def carre():
    x0 = r.randint(1,600)
    y0 = r.randint(1,600)
    canvas.create_rectangle(y0, x0, y0 -100, x0 -100, outline=a,fill=a)
    
def croix():
    x0 = r.randint(1,600)
    y0 = r.randint(1,600)
    canvas.create_rectangle(y0, x0, y0 -100, x0 -100, outline=a,fill=a)
    canvas.create_line(y0, x0, y0-100 , x0-100,fill='yellow')
    canvas.create_line(y0 -100, x0, y0 , x0-100, fill="yellow")

#création des boutons

cercleBTN = tk.Button(root, text ="Cercle", command = cercle,fg="red")
cercleBTN.grid(row=2,column=0)

carreBTN = tk.Button(root, text ="Carré", command = carre,fg="red")
carreBTN.grid(row=3,column=0)

croixBTN = tk.Button(root, text ="Croix", command = croix,fg="red")
croixBTN.grid(row=4,column=0)

colorBTN = tk.Button(root, text ="Choisir une couleur", command = color,fg="red")
colorBTN.grid(row=1,column=2)


#création du canvas
canvas.grid(row=2,column=1,rowspan=4,columnspan=4)

root.mainloop()

