
print('Bienvenido Usuario')
print('El dia de hoy estamos vendiendo leche al por mayor.')
print('Por la compra de más de 3 docenas estamos ofreciendo descuento del 15%')
print('De caso contrario solo el 10% \nY a partir de la 4ta docena regalamos una unidad')

numunidades=(int(input('Ahora, cuantás unidades vas a querer llevar. \n ')))

UniLeche=3000


valorcompra=numunidades*UniLeche

valordescuento1=0.10
valordescuento2=0.15

montobasico=valorcompra*valordescuento1
montoamplio=valorcompra*valordescuento2

if numunidades < 12 and numunidades >24:
    print('Has llevado', numunidades, 'unidades equivalentes a una docena.')
    print('Obtienes descuento del 10%, \nLo que quiere decir que tienes que pagar un total de:', montobasico,'pesos')

