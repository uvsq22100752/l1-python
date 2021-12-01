import tkinter as tk

root = tk.Tk()
root.title("Mon dessin")
root.geometry("500x500")
canvas = tk.Canvas(root, width = 500, height = 500,bg="black")
cord=[]

def draw_pixel(x,y,color):
    canvas.create_rectangle( (x, y)*2,fill=color,outline="" )


        
    
def clic(event):
    x, y = event.x, event.y
    cord.append(x,y)
    
    if len(cord)==4:
        x=cord[1]
        y=cord[2]
        x1=cord[3]
        y1=cord[4]
        if (0<x<250) and (0<y<500) and (0<x1<250) and (0<y1<250):
            canvas.create_line(x, y, x1, y1,outline="blue")
        else:
            canvas.create_oval(x +25, y +25, x -25, y-25 , outline="red")
        
    



canvas.create_line(250,0,250,500,fill="white")
canvas.bind("<Button-1>", clic)
canvas.grid(row=2,column=1,rowspan=4,columnspan=4)


root.mainloop()