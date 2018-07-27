from turtle import *

shape("turtle")
speed(1)
colors = ['red','blue','brown','yellow','grey']
color_penfill = 0

for k in range(5):
    begin_fill()
    color(colors[color_penfill],colors[color_penfill])
    for i in range(2):        
        forward(30)
        left(90)
        forward(50)
        left(90)
    forward(30)
    color_penfill += 1
    end_fill()

mainloop()