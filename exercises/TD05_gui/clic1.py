import tkinter as tk

root = tk.Tk()
root.title("Mon dessin")
root.geometry("500x500")
canvas = tk.Canvas(root, width = 500, height = 500,bg="black")

def draw_pixel(x,y,color):
    canvas.create_rectangle( (x, y)*2,fill=color,outline="" )
    
    
def clic(event):
    x, y = event.x, event.y
    print(x, y)
    draw_pixel(x,y,"red")

def draw_pixel(x,y,color):
    canvas.create_rectangle( (x, y)*2,fill=color,outline="" )



canvas.bind("<Button-1>", clic)
canvas.grid(row=2,column=1,rowspan=4,columnspan=4)


root.mainloop()