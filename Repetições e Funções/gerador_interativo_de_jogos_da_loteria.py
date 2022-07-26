import random
loop = 1
while True: 
    print ("Escolha o tipo de jogo:")
    print("1 - 6 dezenas")
    print("2 - 7 dezenas")
    print("3 - 8 dezenas")
    print("4 - sair")
    op = int(input("Desejá utilizar qual operação? "))
    if op == 1:
        modo = int(input("Jogo aleatório (1) ou manual (2)? "))
        if modo == 1:
            n1 = random.randint(1,60)
            n2 = random.randint(1,60)
            n3 = random.randint(1,60)
            n4 = random.randint(1,60)
            n5 = random.randint(1,60)
            n6 = random.randint(1,60)
            print("jogo " + "{}, {}, {}, {}, {}, {}".format(n1, n2, n3, n4, n5, n6))
            print("Jogo confirmado")
        if modo == 2:
            n1, n2, n3, n4, n5, n6 = input("digite os valores de n1, n2, n3, n4, n5 e n6 ").split()
            print("jogo " + "{}, {}, {}, {}, {}, {}".format(n1, n2, n3, n4, n5, n6))
            print("Jogo confirmado")
    if op == 2:
        modo = int(input("Jogo aleatório (1) ou manual (2)? "))
        if modo == 1:
            n1 = random.randint(1,60)
            n2 = random.randint(1,60)
            n3 = random.randint(1,60)
            n4 = random.randint(1,60)
            n5 = random.randint(1,60)
            n6 = random.randint(1,60)
            n7 = random.randint(1,60)
            print("jogo " + "{}, {}, {}, {}, {}, {}, {}".format(n1, n2, n3, n4, n5, n6, n7))
            print("Jogo confirmado")
        if modo == 2:
            n1, n2, n3, n4, n5, n6, n7 = input("digite os valores de n1, n2, n3, n4, n5, n6 e n7 ").split()
            print("jogo " + "{}, {}, {}, {}, {}, {}, {}".format(n1, n2, n3, n4, n5, n6, n7))
            print("Jogo confirmado")
    if op == 3:
        modo = int(input("Jogo aleatório (1) ou manual (2)? "))
        if modo == 1:
            n1 = random.randint(1,60)
            n2 = random.randint(1,60)
            n3 = random.randint(1,60)
            n4 = random.randint(1,60)
            n5 = random.randint(1,60)
            n6 = random.randint(1,60)
            n7 = random.randint(1,60)
            n8 = random.randint(1,60)
            print("jogo " + "{}, {}, {}, {}, {}, {}, {}, {}".format(n1, n2, n3, n4, n5, n6, n7, n8))
            print("Jogo confirmado")
        if modo == 2:
            n1, n2, n3, n4, n5, n6, n7, n8 = input("digite os valores de n1, n2, n3, n4, n5, n6, n7 e n8 ").split()
            print("jogo " + "{}, {}, {}, {}, {}, {}, {}, {}".format(n1, n2, n3, n4, n5, n6, n7, n8))
            print("Jogo confirmado")
    if op == 4:
        print("Saindo...")
        break





