from datetime import datetime

entrada = input().split()
inicio = entrada[0]
fim = entrada[1]

print(inicio)
print(fim)

if int(inicio) == 0 and int(fim) == 0:
    duracao = 24;
else:
    print('tchau')
    fmt = '%H'
    duracao = datetime.strptime(fim, fmt) - datetime.strptime(inicio, fmt)

