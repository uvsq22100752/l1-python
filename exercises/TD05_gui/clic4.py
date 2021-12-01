import tkinter as tk

root = tk.Tk()
root.title("Mon dessin")
root.geometry("500x500")
canvas = tk.Canvas(root, width = 500, height = 500,bg="black")
cord=[]

def draw_pixel(x,y,color):
    canvas.create_rectangle( (x, y)*2,fill=color,outline="" )

i=0
cord =[]
def clic(event):
    global i
    if i !=10:
        i+=1
        print(i)
        if i%2==0:
            canvas.create_rectangle(150,150,350,350,fill="red",outline="white")
            
        else:
            canvas.create_rectangle(150,150,350,350,fill="black",outline="white")
    else:
        root.destroy()
        
        




canvas.create_rectangle(150,150,350,350,fill="red",outline="white")
canvas.bind("<Button-1>", clic)
canvas.grid(row=2,column=1,rowspan=4,columnspan=4)


root.mainloop()