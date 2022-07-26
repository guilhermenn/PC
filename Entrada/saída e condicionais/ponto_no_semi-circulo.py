import turtle
t = turtle.Turtle()

x = float(input("Qual o x?"))
y = float(input("Qual o y?"))

xx = (x * x)
yy = (y * y)

if x >= 0 and y >= 0 and x ** 2 + y ** 2 <= 1:
  print('pertence')
else:
  print('não pertence')

t.penup()
t.goto(-10,0)
t.pendown()
t.forward(120)
t.penup()
t.goto(0,-10)
t.pendown()
t.left(90)
t.forward(120)
t.penup()
t.goto(90,0)
t.pendown()

t.penup()
t.goto(60,0)
t.right(90)
t.begin_fill()
t.left(90)
t.color("blue")
t.circle(60, 90)
t.left(90)
t.forward(60)
t.end_fill()

t.penup()
t.color("black")
t.goto(xx,yy)
t.pendown()
t.dot(10)
t.hideturtle()