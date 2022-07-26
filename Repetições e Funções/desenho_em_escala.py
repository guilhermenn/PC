import turtle
t = turtle.Turtle()

lado = int(input("Qual o valor do lado x do triângulo? "))
lado2 = lado * 2
lado3 = lado * 3
lado4 = lado * 4
lista = [lado, lado2, lado3, lado4]

for i in lista:
  t.forward(i)
  t.left(120)
  t.forward(i)
  t.left(120)
  t.forward(i)
  t.penup()
  t.left(120)
  t.forward(i + (i / 2))
  t.pendown()