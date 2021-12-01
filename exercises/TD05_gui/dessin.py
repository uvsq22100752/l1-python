import tkinter as tk    
from tkinter import messagebox
import random as r 


#créartion de la fenêtre 
root = tk.Tk()
root.title("Mon dessin")
root.geometry("600x600")
canvas = tk.Canvas(root, width = 600, height = 600,bg="black",highlightbackground="red",selectborderwidth=5,relief="groove")
#fonction pour la couleur ! + globalisation de a
a="blue"
global objects
objects=[]

def undo():

    last=objects[-1]
    if canvas.type(last)=="line":
        last2=objects[-2]
        last=objects.pop(-1)
        canvas.delete(last)
        canvas.delete(last2)
    else:
        last=objects.pop(-1)
        canvas.delete(last)
    
    
       

def color():
    
    print("white, black, red, green, blue, cyan, yellow")
    global a
    a=str(input("Choisi une couleur parmis celle ci-dessus :"))
    
    return print("tu as choisi la couleur",a)
#création du cercle,carre et croix + coodonées 
                     
def cercle():
    x0 = r.randint(100,500)
    y0 = r.randint(100,500)
    objects.append(canvas.create_oval(y0, x0, y0 -100 , x0 -100, outline=a,fill=a))
    
def carre():
    x0 = r.randint(100,500)
    y0 = r.randint(100,500)
    objects.append(canvas.create_rectangle(y0, x0, y0 -100, x0 -100, outline=a,fill=a))
    
def croix():
    x0=r.randint(1,500)
    x1=x0+100
    y0=r.randint(1,500)
    y1=y0+100
    objects.append(canvas.create_line(x0+50,y0,x1-50,y1,fill=a))
    objects.append(canvas.create_line(x0,y0+50,x1,y1-50,fill=a))
   


#création des boutons

cercleBTN = tk.Button(root, text ="Cercle", command = cercle,fg="red")
cercleBTN.grid(row=2,column=0)

carreBTN = tk.Button(root, text ="Carré", command = carre,fg="red")
carreBTN.grid(row=3,column=0)

croixBTN = tk.Button(root, text ="Croix", command = croix,fg="red")
croixBTN.grid(row=4,column=0)

colorBTN = tk.Button(root, text ="Choisir une couleur", command = color,fg="red")
colorBTN.grid(row=1,column=2)

undoBTN = tk.Button(root, text="Undo", command = undo,fg="red")
undoBTN.grid(row=1,column=1)

#création du canvas
canvas.grid(row=2,column=1,rowspan=4,columnspan=4)

root.mainloop()

