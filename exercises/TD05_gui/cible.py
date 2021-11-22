import tkinter as tk

root = tk.Tk()
root.title("Mon dessin")
root.geometry("600x600")
canvas = tk.Canvas(root, width = 600, height = 600,bg="black")


def cerclecolor():
    
    for i in range(1,300):
        global couleur
        couleur="blue"
        x0 = i
        y0 = i
        if i % 1==0:
            couleur="blue"
        elif i % 2==0:
            couleur="green"
        elif i % 3==0:
            couleur="black"
        elif i % 4==0:
            couleur="yellow"
        elif i % 5==0:
            couleur="magenta"
        elif i % 6==0:
            couleur="red"
                       
        canvas.create_oval(y0, x0, y0 +600 , x0 +600, outline=couleur,fill=couleur)
        

canvas.grid(row=2,column=1,rowspan=4,columnspan=4)
root.mainloop()