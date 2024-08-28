#TUPLAS
#Es una coleccion de elementos  distintos y ordenados
# cuya caractersitca es que estan encerrados por parentisis y separados por comass
tupla = (3, 2, "ocho")
print("la tupla", tupla, "es de tipo", type(tupla))


#Como caracteristica principal de la tupla, cuando tenemos una tupla con 1 elemento
tupla = (5)

#Verdadera forma de definir un tupla con un elemento
tupla = ('5',)

print('La tuppla de 1 eleento es:', tupla, 'es de tipo', type(tupla))
print('Su cantidad de elemento es:', len(tupla))

#Slicing
tupla = (3, 6, 'ocho', 'lobo', 'chocolate', 'tierra'[9.2], 'cosa')
print('tupla:', tupla)
print('aplicando slicing:', tupla[4])

#Mutabilidad (no tiene la apacidad de redifinir su valor una vez definidio, es decir, es NO MUTABLE

#suma de tuplas
tupla1, tupla2, = (1, 2, 3), ('cosa,', 'casa', 'ronquido')
print('suma de tuplas:', tupla1 + tupla2)
#invertir utplas a listas
print("cnvirtiendo tupla a lista:", list(tupla)),"tiene tipo:", type (list(tupla))

#Resumen: caracteristicas cmo mutabilidad,

#RANGO (sucesion de numeros enteros)
rango1 = range(5)
print('ejemplo de rango:', rango1, 'rango1 es de tipo:', type(rango1))

#Conversion de range a lista
print('convirtiendo el rango a lista:', list(rango1))

