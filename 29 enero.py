
print('Bienvenido a tu tienda, estos son los productos disponibles:')
print ('1. Guanabana\n2.Pollo\n3.Carne\n4.Leche')

producto=int(input('Cúal vas a querer llevar?\n'))

cantidad=int(input('Ahora cuàntos vas a querer llevar:\n'))
             
guanabana=800
Pollo=1500
Carne=2000
Leche=3600    

if producto ==1:
   guanabana=guanabana*cantidad
   print('Listo, serìa un total de:',guanabana,'$')
elif producto ==2:
  Pollo=Pollo+cantidad
  print('Listo, serìa un total de:',Pollo,'$')
elif producto ==3:
  Carne=Carne*cantidad
  print('Listo, serìa un total de:',Carne,'$')
elif producto ==4:
  Leche=Leche*cantidad
  print('Listo, serìa un total de:',Leche, '$')
else:
  print('Error, por favor selecciona un producto disponible.')