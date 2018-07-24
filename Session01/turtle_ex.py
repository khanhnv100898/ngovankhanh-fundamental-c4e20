from turtle import * 


speed(-1)
shape("turtle")
color("black")

# for i in range(4):
#     forward(100)
#     left(90)
#     forward(100)
#     left(90)
#     forward(100)
#     left(90)
#     forward(100)
#     left(90)
#     right(60)

n = int(input("Nhap so n? "))

for i in range(n):
    forward(100)
    left(360 / n)


    
    

mainloop()