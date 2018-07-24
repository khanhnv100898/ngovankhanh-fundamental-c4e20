from turtle import *

speed(-1)
shape("turtle")

for i in range(3,7):
    for j in range(i):
        if i == 3 or i == 5:
            color("blue")
        else:
            color("red")
        forward(100)
        left(360/i)

mainloop()