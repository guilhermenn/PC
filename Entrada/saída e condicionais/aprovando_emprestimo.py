casa = float(input("Qual o valor da casa? "))
comprador = float(input("Qual o salário do comprador? "))
anos = int(input("Quantos anos de financiamento? "))
mensal = casa // (anos * 12)
prestacaomax = comprador * 0.3
print ("O valor máximo para prestação (margem de 30%) é R$" + str(prestacaomax))
print ("Para pagar uma casa de R$" + str(casa) + " em " + str(anos) + " anos a prestação será de R$" + str(mensal))
if prestacaomax >= mensal:
    print ("Empréstimo pode ser CONCEDIDO!")
else:
    print ("Empréstimo NEGADO!")