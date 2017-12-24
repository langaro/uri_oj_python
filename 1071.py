x = int(input())
y = int(input())

#da pra melhorar umas 500 vezes

if (x > y):
    inicio = x;
    fim = y;
else:
    inicio = y;
    fim = x;

somaImpares = 0;
for i in range(fim+1, inicio):
    if i % 2 > 0:
        somaImpares += i;

print(somaImpares)