import turtle
t = turtle.Turtle()

Atividade = int(input("Submetidas? "))
Completa = int(input("Completas? "))

NotaA = ((Atividade - Completa) * ((4/60)/2))
NotaC = (Completa * (4/60))

Total = NotaC + NotaA

print("Nota = " + str(Total))

t.penup()
t.goto(0,0)
t.pendown()
t.pensize(10)
t.color("orange")
t.forward(Atividade)
t.penup()
t.goto(0,0)
t.pendown()
t.pensize(10)
t.color("green")
t.forward(Completa)
