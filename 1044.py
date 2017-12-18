entrada = input().split()

if float(entrada[0]) > float(entrada[1]):
    dividendo = float(entrada[0]);
    divisor = float(entrada[1]);
else:
    dividendo = float(entrada[1]);
    divisor = float(entrada[0]);

if dividendo % divisor == 0:
    print('Sao Multiplos');
else:
    print('Nao sao Multiplos');