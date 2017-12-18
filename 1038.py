lista =  {1: 4.00,
          2: 4.50,
          3: 5.00,
          4: 2.00,
          5: 1.50}

pedido = input().split()
print('Total: R$ {:0.2f}'.format( lista.get(int(pedido[0]))*float(pedido[1]) ))