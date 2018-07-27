from turtle import *

speed(-1)
shape("turtle")

colors = ['red','blue','brown','yellow','grey']

color_pen = 0

for i in range(3,8):
    for j in range(i):
        # color("red")
        color(colors[color_pen])
        forward(100)
        left(360/i)
    color_pen += 1

mainloop()
        

