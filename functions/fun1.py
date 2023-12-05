from turtle import*


def square():
    for i in range(4):
        fd(120)
        lt(90)

speed('fastest')
pencolor('red')
square() #square function - call/use
goto(-100, 100)
square()
goto(100, -100)
square()

hideturtle()
mainloop()