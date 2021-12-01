import tkinter as tk
import random 

global a,b
a, b = 256, 256
root = tk.Tk()
root.title("couleurs")
root.geometry("374x256")
canvas = tk.Canvas(root, width = a, height = b,bg="black")


def get_colorrandom():
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def get_color(r,g,b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def draw_pixel(i,j,color):
    canvas.create_rectangle( (i, j)*2,fill=color,outline="" )
 
draw_pixel(256/2,256/2,get_colorrandom())  

def ecran_aleatoire():
    for i in range(1,256):
        for j in range(1,256):
            draw_pixel(i,j,get_colorrandom()) 
                      
            
def degrade_gris():
    r=1
    g=1
    b=1
    for i in range (1,256):
        r+=1
        g+=1
        b+=1
        for j in range(1,256):
            draw_pixel(i,j,get_color(r,g,b))
        
    
    
def degrade_2D():
    r=1
    g=1
    b=255
    for i in range (1,256):       
        
        b-=1
        r+=1
        for j in range(1,256):
            draw_pixel(i,j,get_color(r,b,b))
    

    
randomBTN = tk.Button(root, text ="Aléatoire", command = ecran_aleatoire,fg="blue")
randomBTN.grid(row=1,column=0)
degradgrisBTN = tk.Button(root, text ="Dégradé gris", command = degrade_gris,fg="blue")
degradgrisBTN.grid(row=2,column=0)
degrad2dBTN = tk.Button(root, text ="Dégradé 2D", command = degrade_2D,fg="blue")
degrad2dBTN.grid(row=3,column=0)


canvas.grid(row=1,column=3,rowspan=4,columnspan=4) 
root.mainloop()
