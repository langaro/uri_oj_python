import math

valor = int(input())
cedulas = [100, 50, 20, 10, 5, 2 , 1]

print("{0:.0f}".format(valor))
for cedula in cedulas:
    qtd = math.floor(valor/cedula)
    valor = valor % cedula
    print('{:d} nota(s) de R$ {:0.2f}'.format(qtd, cedula).replace('.', ','))