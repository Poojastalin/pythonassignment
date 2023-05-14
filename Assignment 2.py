import turtle
colors = ['red', 'green', 'blue', 'black', 'orange', 'purple']
t = turtle.Pen()
turtle.bgcolor('white')
for x in range(270):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)
