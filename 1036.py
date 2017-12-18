import math

list = input().split()
a = float(list[0])
b = float(list[1])
c = float(list[2])

bhaskara_divisor = 2*a;
if (bhaskara_divisor == 0):
    print('Impossivel calcular');
else:
    bhaskara_antes_sinal = -(b);
    delta = (b ** 2) - 4 * a * c
    if (delta < 0):
        print('Impossivel calcular');
    else :
        bhaskara_depois_sinal = math.sqrt(delta);

        R1 = (bhaskara_antes_sinal+bhaskara_depois_sinal)/bhaskara_divisor;
        R2 = (bhaskara_antes_sinal-bhaskara_depois_sinal)/bhaskara_divisor;

        print("R1 = {0:.5f}".format(R1))
        print("R2 = {0:.5f}".format(R2))