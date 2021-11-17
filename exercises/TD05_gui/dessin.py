import tkinter as tk    
from tkinter import messagebox

#créartion de la fenêtre 
root = tk.Tk()
root.title("Mon dessin")
root.geometry("600x600")
canvas = tk.Canvas(root, width = 600, height = 600,bg="#000000")


#création des boutons

cercleBTN = tk.Button(root, text ="Cercle", command = root.destroy)
cercleBTN.grid(row=2,column=0)

carreBTN = tk.Button(root, text ="Carré", command = root.destroy)
carreBTN.grid(row=3,column=0)

croixBTN = tk.Button(root, text ="Croix", command = root.destroy)
croixBTN.grid(row=4,column=0)

colorBTN = tk.Button(root, text ="Choisir une couleur", command = root.destroy)
colorBTN.grid(row=1,column=2)


#création du canvas
canvas.grid(row=2,column=1,rowspan=4,columnspan=4)


root.mainloop()
