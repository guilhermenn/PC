import turtle
t = turtle.Turtle()

descendente = int(input("Quantos degraus descendentes? "))
ascendente = int(input("Quantos degraus ascendentes? "))

descendente2 = descendente - 1
ascendente2 = ascendente - 1

if descendente >= 1 and ascendente >=1:
    t.begin_fill()
    t.color("blue")
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.end_fill()
    t.right(90)
    for count in range(int(descendente2)):
      t.begin_fill()
      t.color("blue")
      t.forward(10)
      t.left(90)
      t.forward(20)
      t.left(90)
      t.forward(10)
      t.left(90)
      t.forward(20)
      t.end_fill()
      t.left(90)
      t.forward(10)
      t.left(90)
      t.forward(10)
      t.right(90)
    t.left(90)
    t.forward(10)
    t.begin_fill()
    t.color("orange")
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.end_fill()
    t.backward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    for count in range(int(ascendente2)):
        t.begin_fill()
        t.color("orange")
        t.forward(10)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(20)
        t.end_fill()
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(10)
        t.left(90)

if descendente >= 1 and ascendente <= 0:
    t.begin_fill()
    t.color("blue")
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.end_fill()
    t.right(90)
    for count in range(int(descendente2)):
      t.begin_fill()
      t.color("blue")
      t.forward(10)
      t.left(90)
      t.forward(20)
      t.left(90)
      t.forward(10)
      t.left(90)
      t.forward(20)
      t.end_fill()
      t.left(90)
      t.forward(10)
      t.left(90)
      t.forward(10)
      t.right(90)

if descendente <= 0 and ascendente >= 1:
    t.begin_fill()
    t.color("orange")
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.end_fill()
    t.backward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    for count in range(int(ascendente2)):
        t.begin_fill()
        t.color("orange")
        t.forward(10)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(20)
        t.end_fill()
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(10)
        t.left(90)

if descendente <= 0 and ascendente <= 0:
    print("valor inválido :(")