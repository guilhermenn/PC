fizeram = int(input("Quanto alunos fizeram a atividade? "))
nfizeram = int(input("Quanto alunos não fizeram a atividade? "))

total = fizeram + nfizeram

porcentfizeram = ((fizeram * 100) /total)
porcentnfizeram = ((nfizeram * 100) /total)

print(str(porcentfizeram) + "% fez a atividade e " + str(porcentnfizeram) + "% não fez.")

grau1= ((360 * porcentfizeram) /100)
grau2= ((360 * porcentnfizeram) /100)

import turtle
t = turtle.Turtle()
if porcentfizeram != 100:
    t.begin_fill()
    t.forward(60)
    t.left(90)
    t.color("green")
    t.circle(60, grau1)
    t.left(90)
    t.forward(60)
    t.end_fill()

    t.begin_fill()
    t.backward(60)
    t.right(90)
    t.color("red")
    t.circle(60, grau2)
    t.left(90)
    t.forward(60)
    t.end_fill()
if porcentfizeram == 100:
    t.begin_fill()
    t.forward(60)
    t.left(90)
    t.color("green")
    t.circle(60, grau1)
    t.left(90)
    t.forward(60)
    t.end_fill()
if porcentfizeram == 0:
    t.begin_fill()
    t.forward(60)
    t.left(90)
    t.color("red")
    t.circle(60, grau2)
    t.left(90)
    t.forward(60)
    t.end_fill()