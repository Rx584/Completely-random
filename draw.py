import turtle
import random
turtle.colormode(255)

pen = turtle.Pen()
pen.speed(0)
tims = int(input('作画次数'))
pen.pensize(int(input("粗度")))
o = input("是否跳过过程？")
if o == "是":
    turtle.tracer(False)
random.seed(tims)
for i in range(tims):
    r,g,b = random.randint(1,255),random.randint(1,255),random.randint(1,255)
    pen.forward(random.randint(1, 100))
    pen.left(random.randint(1,100))
    pen.pencolor(r,g,b)
turtle.done()


