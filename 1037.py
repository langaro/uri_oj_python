valor = float(input())
intervalo = False
list = [[0,25], [25,50], [50,75], [75,100]]

for i in range(len(list)):
    if valor >= list[i][0] and valor <= list[i][1]:
        print("Intervalo {0}".format(list[i]))
        intervalo = True
        break

if intervalo == False:
    print("Fora de intervalo")
