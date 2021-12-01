import tkinter as tk

root = tk.Tk()
root.title("Mon dessin")
root.geometry("500x500")
canvas = tk.Canvas(root, width = 500, height = 500,bg="black")
cord=[]

def draw_pixel(x,y,color):
    canvas.create_rectangle( (x, y)*2,fill=color,outline="" )


cord =[]
def clic(event):
    global cord
    if len(cord)!=4:
        x, y = event.x, event.y
        cord.append(x)
        cord.append(y)
        print(cord)
    
    if len(cord)==4:
        
        x=cord[0]
        y=cord[1]
        x1=cord[2]
        y1=cord[3]
        if (0<x<250) and (0<y<500):
            if (0<x1<250) and (0<y1<250):
                canvas.create_line(x, y, x1, y1,fill="blue")
        else:
            canvas.create_line(x, y, x1, y1,fill="red")
            
        cord = []
        
        
    



canvas.create_line(250,0,250,500,fill="white")
canvas.bind("<Button-1>", clic)
canvas.grid(row=2,column=1,rowspan=4,columnspan=4)


root.mainloop()