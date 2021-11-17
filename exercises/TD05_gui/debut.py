import tkinter as tk


CANVAS_WIDTH, CANVAS_HEIGHT = 600, 500


root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

    # Début de votre code
x0 = 100
x1 = 400
y = 300
canvas.create_line(y, x0, y, x1)
canvas.create_oval(y - 50, y+100 , y + 50, y )
canvas.create_oval( y-50, y , y+50, y-x0 )
canvas.create_oval(y-50, y-x0 , y + 50, y-2*x0)
    
    # Fin de votre code

canvas.grid()
root.mainloop()
