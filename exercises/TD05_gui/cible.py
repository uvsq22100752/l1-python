import tkinter as tk
global a,b
a, b = 600, 600
root = tk.Tk()
root.title("Mon dessin")
root.geometry("600x600")
canvas = tk.Canvas(root, width = a, height = b,bg="black")
color=["blue", "green", "black", "yellow", "magenta", "red"]
x0=1
y0=1
x1=b
y1=a
n=0

for i in range (1,7):
    if i==1:
        n=0
        print("i")
    else:
        n+=54
    canvas.create_oval(y0+n, x0+n, y1-n , x1-n, outline=color[0],fill=color[0])
    canvas.create_oval(y0+(9+n), x0+(9+n), y1-(9+n) , x1-(9+n), outline=color[1],fill=color[1])
    canvas.create_oval(y0+(18+n), x0+(18+n), y1-(18+n) , x1-(18+n), outline=color[2],fill=color[2])
    canvas.create_oval(y0+(27+n), x0+(27+n), y1-(27+n) , x1-(27+n), outline=color[3],fill=color[3])
    canvas.create_oval(y0+(36+n), x0+(36+n), y1-(36+n) , x1-(36+n), outline=color[4],fill=color[4])
    canvas.create_oval(y0+(45+n), x0+(45+n), y1-(45+n) , x1-(45+n), outline=color[5],fill=color[5])



canvas.grid(row=2,column=1,rowspan=4,columnspan=4)
root.mainloop()
