opcao = input("Deseja qual opção? add, mul ou in? ")
if opcao == "add":
    a = input("Me dê uma palavra ")
    b = input("Me dê outra palavra ")
    c = a + b
    print ("O valor de " + a + " add " + b + " é " + c)
if opcao == "mul":
    a = input("Me dê uma palavra ")
    n = int(input("Me dê um número "))
    c = a * n
    print ("O valor de " + a + " mul " + str(n) + " é " + c)
if opcao == "in":
    a = input("Me dê uma palavra ")
    b = input("Me dê outra palavra ")
    c = a in b
    print ("O valor de " + a + " in " + b + " é " + str(c))