import math

d = int(input())

anos = math.floor(d/365)
restante = d % 365
meses = math.floor(restante/30)
dias = d-(anos*365+meses*30)

print('{:d} ano(s)'.format(anos))
print('{:d} mes(es)'.format(meses))
print('{:d} dia(s)'.format(dias))