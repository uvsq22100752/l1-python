import tkinter as tk


root = tk.Tk()
root.title("Mon dessin")
root.geometry("500x500")
canvas = tk.Canvas(root, width = 500, height = 500,bg="black")
cord=[]


i=0
objects =[]
def clic(event):
    global i
    global cercle
    global objects
    x,y=event.x,event.y
    if i <=8:
        print(i)
        i+=1
        canvas.create_oval(x +25, y +25, x -25, y-25 , fill="red")
    
    if i==9:
        for item in canvas.find_all():
            canvas.itemconfigure(item,outline="yellow", fill='yellow')
        
        print("oui")
        i+=1
    if i==10:
        canvas.delete('all')
        i=0
        
        
        

canvas.bind("<Button-1>", clic)
canvas.grid(row=2,column=1,rowspan=4,columnspan=4)


root.mainloop()