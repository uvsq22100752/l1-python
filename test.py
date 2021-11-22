import numpy
from pylab import imshow, show

def mandel(x, y, max_iters):
  """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.
  """
  c = complex(x, y)
  z = 0.0j
  for i in range(max_iters):
    z = z*z + c
    if (z.real*z.real + z.imag*z.imag) >= 4:
      return i
  return max_iters

def create_fractal(min_x, max_x, min_y, max_y, image, iters):
  height = image.shape[0]
  width = image.shape[1]
  pixel_size_x = (max_x - min_x) / width
  pixel_size_y = (max_y - min_y) / height
    
  for x in range(width):
    real = min_x + x * pixel_size_x
    for y in range(height):
      imag = min_y + y * pixel_size_y
      color = mandel(real, imag, iters)
      image[y, x] = color

image = numpy.zeros((1024, 1536), dtype = numpy.uint8)
create_fractal(-2.0, 1.0, -1.0, 1.0, image, 20) 

imshow(image)
show()






def Color():
    i=0
    while i<0:
        a=input("Choisi une couleur :")
        print("white, black, red, green, blue, cyan, yellow")
        if a=="white" or "black" or "red" or "green" or "blue" or "cyan" or "yellow":
            
            i+=1
    return
  


 def color():
    for i in range(1,600):
        global coloor
        
        coloor="blue" 
        y0=i
        x0=i
        y1=a-i
        x1=a-i
        for i in range(1,6):
            if i==1:
                coloor=="blue"
                canvas.create_oval(y0, x0, y1 , x1, outline=coloor,fill=coloor)
                print(i)
            elif i==2:
                coloor=="green"
                canvas.create_oval(y0, x0, y1 , x1, outline=coloor,fill=coloor)
            elif i==3:
                coloor=="black"
                canvas.create_oval(y0, x0, y1 , x1, outline=coloor,fill=coloor)
            elif i==4:
                coloor=="yellow"
                canvas.create_oval(y0, x0, y1 , x1, outline=coloor,fill=coloor)
            elif i==5:
                coloor=="magenta"
                canvas.create_oval(y0, x0, y1 , x1, outline=coloor,fill=coloor)
            elif i==6:
                coloor=="red"
                canvas.create_oval(y0, x0, y1 , x1, outline=coloor,fill=coloor)

cercleBTN = tk.Button(root, text ="Cercle", command = color,fg="red")
cercleBTN.grid(row=2,column=0)


canvas.create_oval(y0, x0, y1 , x1, outline=color[0],fill=color[0])
canvas.create_oval(y0+20, x0+20, y1-20 , x1-20, outline=color[1],fill=color[1])
canvas.create_oval(y0+40, x0+40, y1-40 , x1-40, outline=color[2],fill=color[2])
canvas.create_oval(y0+60, x0+60, y1-60 , x1-60, outline=color[3],fill=color[3])
canvas.create_oval(y0+80, x0+80, y1-80 , x1-80, outline=color[4],fill=color[4])
canvas.create_oval(y0+100, x0+100, y1-100 , x1-100, outline=color[5],fill=color[5])

canvas.create_oval(y0+120, x0+120, y1-120 , x1-120, outline=color[0],fill=color[0])
canvas.create_oval(y0+140, x0+140, y1-140 , x1-140, outline=color[1],fill=color[1])
canvas.create_oval(y0+160, x0+160, y1-160 , x1-160, outline=color[2],fill=color[2])
canvas.create_oval(y0+180, x0+180, y1-180 , x1-180, outline=color[3],fill=color[3])
canvas.create_oval(y0+200, x0+200, y1-200 , x1-200, outline=color[4],fill=color[4])
canvas.create_oval(y0+220, x0+220, y1-220 , x1-220, outline=color[5],fill=color[5])


for i in [1,15,20,25,30]:
    canvas.create_oval(y0+i, x0+i, y1+i , x1+i, outline=color[0],fill=color[0])
    canvas.create_oval(y0+5+i, x0+5+i, y1-(5+i) , x1-(5+i), outline=color[1],fill=color[1])
    canvas.create_oval(y0+10+i, x0+10+i, y1-(10+i) , x1-(10+i), outline=color[2],fill=color[2])
    canvas.create_oval(y0+15+i, x0+15+i, y1-(15+i) , x1-(15+i), outline=color[3],fill=color[3])
    canvas.create_oval(y0+20+i, x0+20+i, y1-(20+i) , x1-(20+i), outline=color[4],fill=color[4])
    canvas.create_oval(y0+25+i, x0+25+i, y1-(25+i) , x1-(25+i), outline=color[5],fill=color[5])

canvas.create_oval(y0+35, x0+35, y1-35 , x1-35, outline=color[0],fill=color[0])
canvas.create_oval(y0+40, x0+40, y1-40 , x1-40, outline=color[1],fill=color[1])
canvas.create_oval(y0+45, x0+45, y1-45 , x1-45, outline=color[2],fill=color[2])
canvas.create_oval(y0+50, x0+50, y1-50 , x1-50, outline=color[3],fill=color[3])
canvas.create_oval(y0+55, x0+55, y1-55 , x1-55, outline=color[4],fill=color[4])
canvas.create_oval(y0+60, x0+60, y1-60 , x1-60, outline=color[5],fill=color[5])