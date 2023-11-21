from turtle import *

speed('slowest')
pensize(2)

colors = ['red','blue','yellow','black', 'green', 'purple']

for i in range(6):
    write(colors[i], font=('Arial', 16, 'bold'))
    pencolor(colors[i])
    fd(100)
    lt(360/3)

hideturtle()
mainloop()  