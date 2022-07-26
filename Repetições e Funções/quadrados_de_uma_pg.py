import turtle
t = turtle.Turtle()

a1 = int(input("Digite o primeiro termo da PG "))
r = int(input("Digite a razão da PG "))
cont = 0
while True:
    an = a1 * r
    a1 = an
    cont += 1
    t.forward(a1)
    t.left(90)
    t.forward(a1)
    t.left(90)
    t.forward(a1)
    t.left(90)
    t.forward(a1)
    t.left(90)
    if cont == 5:
        break