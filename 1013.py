list = input().split()
a = float(list[0])
b = float(list[1])
c = float(list[2])

#maior1 = (a+b+abs(a-b))/2
#maior2 = (maior1+c+abs(maior1-c))/2

#print("{0:.0f} eh o maior".format(maior2))

def maiorAB(a, b):
    return (a+b+abs(a-b))/2

print("{0:.0f} eh o maior".format(maiorAB(maiorAB(a, b),c)))


