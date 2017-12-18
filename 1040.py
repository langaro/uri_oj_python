notas = input().split()
n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])
p1 = 2
p2 = 3
p3 = 4
p4 = 1

media = (n1*p1+n2*p2+n3*p3+n4*p4)/(p1+p2+p3+p4)
print('Media: {:0.1f}'.format(media))
if media >= 7:
    print('Aluno aprovado.')
elif media < 5 :
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    ne = float(input())
    print('Nota do exame: {:0.1f}'.format(ne))
    mf = (media+ne)/2
    if mf >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:0.1f}'.format(mf))