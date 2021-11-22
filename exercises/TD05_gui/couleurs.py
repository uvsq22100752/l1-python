import tkinter as tk
import random 

global a,b
a, b = 256, 256
root = tk.Tk()
root.title("couleurs")
root.geometry("374x256")
canvas = tk.Canvas(root, width = a, height = b,bg="black")


def get_color():
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)




def draw_pixel(i,j,color):
    canvas.create_rectangle( (i, j)*2,fill=color,outline="" )
 
draw_pixel(256/2,256/2,get_color())  

def ecran_aleatoire():
    draw_pixel(100,100,get_color)
    
    
    

randomBTN = tk.Button(root, text ="Aléatoire", command = ecran_aleatoire,fg="blue")
randomBTN.grid(row=1,column=0)
degradgrisBTN = tk.Button(root, text ="Dégradé gris", command = root.destroy,fg="blue")
degradgrisBTN.grid(row=2,column=0)
degrad2dBTN = tk.Button(root, text ="Dégradé 2D", command = root.destroy,fg="blue")
degrad2dBTN.grid(row=3,column=0)

canvas.grid(row=1,column=3,rowspan=4,columnspan=4) 
root.mainloop()
