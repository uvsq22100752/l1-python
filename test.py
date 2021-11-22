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
  


 b=str(input("Choisi une couleur parmis celle ci-dessus :"))
    if a=="yellow" or "Yellow":
        print("tu as choisi la couleur",b)
        a=b
    elif a=="black":
        print("tu as choisi la couleur noire",b)
        a=b
    elif a=="red" or "Red":
        print("tu as choisi la couleur rouge",b)
        a=b
    elif a=="green" or "Green":
        print("tu as choisi la couleur verte",b)
        a=b
    elif a=="blue" or "Blue":
        print("tu as choisi la couleur bleue",b)
        a=b
    elif a=="cyan" or "Cyan":
        print("tu as choisi la couleur cyan",b)
        a=b
    elif a=="white" or "White":
        print("tu as choisi la couleur blanche",b)
        a=b
    else:
        print("erreur ! entre une vraie couleur")
        print(b,"ne correspond pas a la liste ci dessus.")