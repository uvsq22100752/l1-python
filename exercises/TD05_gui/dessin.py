import tkinter as tk    
from tkinter import messagebox
import random as r 

randomcolor=["yellow","black","blue","red"]
#créartion de la fenêtre 
root = tk.Tk()
root.title("Mon dessin")
root.geometry("600x600")
canvas = tk.Canvas(root, width = 600, height = 600,bg="black")

def selectRandom(randomcolor):
  return r.choice(randomcolor)

def changeColor():
    canvas.configure(bg = (selectRandom(randomcolor)))
    
#création des boutons

cercleBTN = tk.Button(root, text ="Cercle", command = root.destroy,fg="red")
cercleBTN.grid(row=2,column=0)

carreBTN = tk.Button(root, text ="Carré", command = root.destroy,fg="red")
carreBTN.grid(row=3,column=0)

croixBTN = tk.Button(root, text ="Croix", command = root.destroy,fg="red")
croixBTN.grid(row=4,column=0)

colorBTN = tk.Button(root, text ="Choisir une couleur", command = changeColor,fg="red")
colorBTN.grid(row=1,column=2)


#création du canvas
canvas.grid(row=2,column=1,rowspan=4,columnspan=4)


root.mainloop()
