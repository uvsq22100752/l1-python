import tkinter as tk


root = tk.Tk()
root.title("Mon dessin")
root.geometry("500x500")
canvas = tk.Canvas(root, width = 500, height = 500,bg="black")
cord=[]


i=0
objects =[]
cercle=[]
def clic(event):
    global i
    global cercle
    global objects
    x,y=event.x,event.y
    if i <=8:
        print(i)
        
        cercle.append(canvas.create_oval(x +25, y +25, x -25, y-25 , fill="red"))
        i+=1
    elif i==9:
        i+=1
        for i in range (len(cercle)):
            canvas.itemconfigure(i, fill='yellow')
        
        print(i)
    else: 
        canvas.delete('all')
    i=0
        
        
        

canvas.bind("<Button-1>", clic)
canvas.grid(row=2,column=1,rowspan=4,columnspan=4)


root.mainloop()