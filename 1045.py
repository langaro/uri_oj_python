list = sorted(input().split(), key=float, reverse=True)

a = float(list[0])
b = float(list[1])
c = float(list[2])

if a >= b + c:
    print('NAO FORMA TRIANGULO');
else :
    if a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO');
    if a**2 > b**2 + c**2:
        print('TRIANGULO OBTUSANGULO');
    if a**2 < b**2 + c**2:
        print('TRIANGULO ACUTANGULO');
    if a == b == c:
        print('TRIANGULO EQUILATERO');
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES');

