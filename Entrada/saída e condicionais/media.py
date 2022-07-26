#perguntar quais os valores
valor1 = int(input("Qual o primeiro valor?"))
valor2 = int(input("Qual o segundo valor?"))
valor3 = int(input("Qual o terceiro valor?"))
#calcular a média
media = ((valor1 + valor2 + valor3) / 3)
print ("Valor 1: " + str(valor1))
print ("Valor 2: " + str(valor2))
print ("Valor 3: " + str(valor3))
print ("Média: " + str(media))
#importar o turtle
import turtle
t = turtle.Turtle()
t.pensize(10)
#fazer os desenhos 
t.penup()
t.color("red")
t.goto(0,5)
t.pendown()
t.forward(media)

t.penup()
t.color("black")
t.goto(0,-10)
t.pendown()
t.forward(valor1)

t.penup()
t.color("black")
t.goto(0,-25)
t.pendown()
t.forward(valor2)

t.penup()
t.color("black")
t.goto(0,-40)
t.pendown()
t.forward(valor2)












