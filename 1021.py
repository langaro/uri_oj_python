import math

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

valor = float(input())
valor += 0.001
#Então velho, faz o seguinte. Logo após você ter colocado valor = float(input('')) coloque valor +=0.001. Isso porque o python não consegue fazer a contagem do valor abaixo de 0.01, pois o resultado do calculo quando ele vai efetuar em 1 centavo ele fica a 0. Faça o teste antes de colocar o que te mandei digitando 20.11, 574.77 e observe que ele nao conta os centavos.

print("NOTAS:")
for nota in notas:
    qtd = math.floor(valor/nota)
    valor = valor % nota
    print('{:d} nota(s) de R$ {:0.2f}'.format(qtd, nota))

print("MOEDAS:")
for moeda in moedas:
    qtd = math.floor(valor/moeda)
    valor = valor % moeda
    print('{:d} moeda(s) de R$ {:0.2f}'.format(qtd, moeda))