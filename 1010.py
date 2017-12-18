a = input()
b = input()
#arr= [a.split(),b.split()]

la = a.split()
lb = b.split()

#i = 0
#while i < len(la):
#    print(la[i])
#    i = i + 1

print("VALOR A PAGAR: R$ {0:.2f}".format(float(la[1])*float(la[2])+float(lb[1])*float(lb[2])))