lados = input().split()
a = float(lados[0]);
b = float(lados[1]);
c = float(lados[2]);

#se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo.
#Se a soma entre os dois lados é igual ao terceiro, esse triângulonão pode existir

if a < b + c and b < a + c and c < a + b:
    print('Perimetro = {:0.1f}'.format(a + b + c));
else:
    print('Area = {:0.1f}'.format( ((a + b)/2.0)*c) );
