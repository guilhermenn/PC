import turtle
t = turtle.Turtle()

comprimento = float(input("Qual será o valor do comprimento da reta? "))
cor = input("Qual cor deseja entre azul, vermelho e verde? ")
 
t.pensize(10)
if cor == "azul":
    t.pencolor("blue")
    t.forward(comprimento)
elif cor == "vermelho":
    t.pencolor("red")
    t.forward(comprimento)
elif cor == "verde":
    t.pencolor("green")
    t.forward(comprimento)
else:
    print("Cor inválida.")