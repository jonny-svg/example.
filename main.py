import turtle
import random

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()



t.penup()
t.goto(-400, -100)
t.color("limegreen")
t.begin_fill()
t.goto(400, -100)
t.goto(400, -300)
t.goto(-400, -300)
t.goto(-400, -100)
t.end_fill()


t.penup()
t.goto(250, 150)
t.color("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()


t.penup()
t.goto(-300, -100)
t.color("sienna")
t.begin_fill()
t.goto(-280, -100)
t.goto(-280, -160)
t.goto(-300, -160)
t.goto(-300, -100)
t.end_fill()

t.penup()
t.goto(-290, -40)
t.color("forestgreen")
t.begin_fill()
t.circle(40)
t.end_fill()


t.penup()
t.goto(200, -100)
t.color("sienna")
t.begin_fill()
t.goto(220, -100)
t.goto(220, -160)
t.goto(200, -160)
t.goto(200, -100)
t.end_fill()

t.penup()
t.goto(210, -40)
t.color("forestgreen")
t.begin_fill()
t.circle(40)
t.end_fill()


t.penup()
t.goto(-50, -100)
t.color("saddlebrown")
t.begin_fill()
t.goto(50, -100)
t.goto(50, -110)
t.goto(-50, -110)
t.goto(-50, -100)
t.end_fill()


t.penup()
t.goto(-50, -110)
t.begin_fill()
t.goto(-50, -140)
t.goto(-45, -140)
t.goto(-45, -110)
t.goto(-50, -110)
t.end_fill()


t.penup()
t.goto(45, -110)
t.begin_fill()
t.goto(45, -140)
t.goto(50, -140)
t.goto(50, -110)
t.goto(45, -110)
t.end_fill()


flower_colors = ["red", "magenta", "orange", "purple", "pink"]
for _ in range(20):
    x = random.randint(-350, 350)
    y = random.randint(-90, -20)
    color = random.choice(flower_colors)

    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color(color)
    for _ in range(6):
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.left(60)


    t.penup()
    t.goto(x, y)
    t.color("yellow")
    t.begin_fill()
    t.circle(5)
    t.end_fill()


screen.mainloop()
