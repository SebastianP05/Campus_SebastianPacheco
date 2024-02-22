
print('Bienvenido a tu calculador de notas.')

nota1=(int(input('Por favor ingresa 3 notas. (Calificacion de 0 a 5)' )))
nota2=(int(input('Ingresa otra màs.')))
nota3=(int(input('Ahora ingresa la ultima.')))

suma=nota1+nota2+nota3
promedio=suma/3

if promedio >3:
    print('Felicidades, tu promedio es de:',promedio,'(APROBADO)')
elif promedio <3:
    print('Lastimosamente tu promedio es de:',promedio,'(REPROBADO)')