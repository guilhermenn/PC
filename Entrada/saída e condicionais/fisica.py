d = int(input("Qual a distância em km? "))
v1 = int(input("Qual a velocidade média do primeiro veículo? "))
v2 = int(input("Qual a velocidade média do segundo veículo? "))

t = (d/(v1 + v2))

print("Tempo de encontro, em horas, é de: " + str(t))

t1 = (t * v1)
t2 = (t * v2)

import turtle
t = turtle.Turtle()

t.pensize(10)
t.color("blue")
t.forward(t1)
t.color("green")
t.forward(t2)
t.penup()
t.goto(t1,0)
t.pendown()
t.color("black")
t.dot(10)
t.hideturtle()

