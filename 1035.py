list = input().split()
a = float(list[0])
b = float(list[1])
c = float(list[2])
d = float(list[3])

if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0 :
    print('Valores aceitos')
else:
    print("Valores nao aceitos")