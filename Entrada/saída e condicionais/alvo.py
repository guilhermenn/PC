x = int(input("Qual o x? "))
y = int(input("Qual o y? "))

import turtle
t = turtle.Turtle()

t.penup()
t.goto(0,-100)
t.pendown()
t.begin_fill()
t.color("black")
t.circle(100)
t.end_fill()

t.penup()
t.goto(0,-75)
t.pendown()
t.begin_fill()
t.color("blue")
t.circle(75)
t.end_fill()

t.penup()
t.goto(0,-50)
t.pendown()
t.begin_fill()
t.color("red")
t.circle(50)
t.end_fill()

t.penup()
t.goto(0,-25)
t.pendown()
t.begin_fill()
t.color("yellow")
t.circle(25)
t.end_fill()

t.penup()
t.goto(x,y)
t.pendown()
t.color("green")
t.dot(10)
t.hideturtle()

import math
d = math.sqrt((x ** 2) + (y ** 2))


if d >= 0 and d <= 25:
    print("100 pontos na faixa amarela")
if d > 25 and d <= 50:
    print("70 pontos na faixa vermelha")
if d > 50 and d <= 75:
    print("40 pontos na faixa azul")
if d > 75 and d <= 100:
    print("10 pontos na faixa preta")
if d > 100:
    print("Você errou o dardo :’(")