import tkinter as tk
global a,b
a, b = 256, 256
root = tk.Tk()
root.title("couleurs")
root.geometry("374x256")
canvas = tk.Canvas(root, width = a, height = b,bg="black")


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    r=r.randint(0,250)
    g=r.randint(0,250)
    b=r.randint(0,250)
    
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
color="white"

def draw_pixel(i,j,color):
    canvas.create_rectangle( (i, j)*2,fill=color,outline="" )
    
    
draw_pixel(256/2,256/2,"white")  
    

randomBTN = tk.Button(root, text ="Aléatoire", command = draw_pixel,fg="blue")
randomBTN.grid(row=1,column=0)
degradgrisBTN = tk.Button(root, text ="Dégradé gris", command = root.destroy,fg="blue")
degradgrisBTN.grid(row=2,column=0)
degrad2dBTN = tk.Button(root, text ="Dégradé 2D", command = root.destroy,fg="blue")
degrad2dBTN.grid(row=3,column=0)

canvas.grid(row=1,column=3,rowspan=4,columnspan=4) 
root.mainloop()
