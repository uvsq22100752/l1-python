import tkinter as tk

root = tk.Tk()
root.title("Mon dessin")
root.geometry("500x500")
canvas = tk.Canvas(root, width = 500, height = 500,bg="black")

def draw_pixel(x,y,color):
    canvas.create_rectangle( (x, y)*2,fill=color,outline="" )
    
    
def clic(event):
    x, y = event.x, event.y
    if (0<event.x<250) and (0<event.y<500):
        canvas.create_oval(x +25, y +25, x -25, y-25 , outline="blue")
    else:
        canvas.create_oval(x +25, y +25, x -25, y-25 , outline="red")
        
    



canvas.create_line(250,0,250,500,fill="white")
canvas.bind("<Button-1>", clic)
canvas.grid(row=2,column=1,rowspan=4,columnspan=4)


root.mainloop()