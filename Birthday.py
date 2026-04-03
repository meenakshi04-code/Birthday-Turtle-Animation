import turtle
import time
import random

# Screen setup
screen = turtle.Screen()
screen.setup(900, 600)
screen.bgcolor("#f8e1e7")
screen.title("Happy Birthday")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# -------- Background --------
def background():
    for _ in range(40):
        pen.penup()
        x = random.randint(-430, 430)
        y = random.randint(-280, 280)
        pen.goto(x, y)
        pen.dot(random.randint(5, 10), "#e1bee7")

# -------- Teddy --------
def draw_teddy(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    pen.color("#6d4c41")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()

    for dx in [-30, 30]:
        pen.penup()
        pen.goto(x + dx, y + 60)
        pen.pendown()
        pen.begin_fill()
        pen.circle(18)
        pen.end_fill()

    pen.color("#bcaaa4")
    for dx in [-30, 30]:
        pen.penup()
        pen.goto(x + dx, y + 60)
        pen.pendown()
        pen.begin_fill()
        pen.circle(10)
        pen.end_fill()

    pen.penup()
    pen.goto(x - 18, y + 25)
    pen.dot(10, "black")
    pen.goto(x + 18, y + 25)
    pen.dot(10, "black")
    pen.goto(x, y + 5)
    pen.dot(12, "black")

# -------- Chocolate --------
def draw_chocolate(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    pen.color("#3e2723")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(120)
        pen.left(90)
        pen.forward(70)
        pen.left(90)
    pen.end_fill()

    pen.color("#a1887f")
    for i in range(2):
        for j in range(4):
            pen.penup()
            pen.goto(x + 20 + j*25, y + 15 + i*25)
            pen.pendown()
            pen.begin_fill()
            pen.circle(8)
            pen.end_fill()

# -------- Draw Static Scene --------
background()
draw_teddy(-250, -50)
draw_teddy(250, -50)
draw_chocolate(-60, -150)

# -------- Smooth Text Writing --------
writer = turtle.Turtle()
writer.hideturtle()
writer.color("#4a148c")
writer.penup()
writer.goto(-250, 120)
writer.pendown()
writer.pensize(3)

text = "HAPPY BIRTHDAY"

# Draw each character manually (stroke-like effect)
for char in text:
    writer.write(char, font=("Verdana", 36, "bold"))
    x, y = writer.position()
    writer.penup()
    writer.goto(x + 30, y)  # move forward for next letter
    writer.pendown()
    time.sleep(0.25)

# Sub message
writer.penup()
writer.goto(0, 60)
writer.color("#1a237e")
writer.write("Wishing you joy, love, and lots of chocolates",
             align="center", font=("Arial", 16, "normal"))

turtle.done()
