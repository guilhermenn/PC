#importar o turtle
import turtle
t = turtle.Turtle()
#perguntar o número
valor1 = int(input("Qual o número?"))
if valor1 % 2 == 1:
  print('impar')
  t.color("green")
  t.begin_fill()
  t.circle(valor1)
  t.end_fill()
else:
  print('par')
  t.color("red")
  t.begin_fill()
  t.circle(valor1)
  t.end_fill()
