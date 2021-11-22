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
for i in range (1,8):
    if i==1:
        n=0
        print("i")
    else:
        n+=30
    canvas.create_oval(y0+n, x0+n, y1-n , x1-n, outline=color[0],fill=color[0])
    canvas.create_oval(y0+(5+n), x0+(5+n), y1-(5+n) , x1-(5+n), outline=color[1],fill=color[1])
    canvas.create_oval(y0+(10+n), x0+(10+n), y1-(10+n) , x1-(10+n), outline=color[2],fill=color[2])
    canvas.create_oval(y0+(15+n), x0+(15+n), y1-(15+n) , x1-(15+n), outline=color[3],fill=color[3])
    canvas.create_oval(y0+(20+n), x0+(20+n), y1-(20+n) , x1-(20+n), outline=color[4],fill=color[4])
    canvas.create_oval(y0+(25+n), x0+(25+n), y1-(25+n) , x1-(25+n), outline=color[5],fill=color[5])





canvas.grid(row=2,column=1,rowspan=4,columnspan=4)
root.mainloop()
