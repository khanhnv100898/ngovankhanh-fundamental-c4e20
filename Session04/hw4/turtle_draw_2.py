from turtle import *

speed(-1)
# shape("turtle")
color("blue")

length = 0
for k in range(47):
    for i in range(4):
        forward(5 + length)
        left(90)
    left(10)
    length += 5


mainloop()