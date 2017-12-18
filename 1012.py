pi = 3.14159
list = input().split()
a = float(list[0])
b = float(list[1])
c = float(list[2])

print("TRIANGULO: {0:.3f}".format((a*c)/2))
print("CIRCULO: {0:.3f}".format(pi*c**2))
print("TRAPEZIO: {0:.3f}".format((c*(a+b))/2))
print("QUADRADO: {0:.3f}".format(b**2))
print("RETANGULO: {0:.3f}".format(a*b))