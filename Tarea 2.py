from traceback import print_list
#Crear una lista original
mis_listas = ["hola","como","estas"]

#Agregar un elemento al final de la lista con append
mis_listas.append("yo")
mis_listas.append("al")
mis_listas.append("cien")

print(mis_listas)


#Agregar varios elementos al final de la lista con extend
segunda_lista =["gracias", "por", "preguntar"]

mis_listas.extend(segunda_lista)
print(mis_listas)

#Agregar un elemento en un posicion especifica de la lista con .insert

tercera_lista = ("que","tal","el perro")

#Agregar "y" en la posicion 1
tercera_lista.insert (1,9)



print(tercera_lista)

#Eliminar un elemento especifico en la lista con .remove

cuarta_lista = (3, 6, 9, 12)
cuarta_lista.remove(6)
print(cuarta_lista)

#ELiminar y devolver un elemento de una lista en una posicion especifica con .pop
quinta_lista=("tu", "yo", "nosotros")
ultimo_elemento = quinta_lista.pop(3)

print(ultimo_elemento)

#eliminar todos los elementos de la lista

sexta_lista = (11, 23, 54)
sexta_lista.clear()
print(sexta_lista)

# .index se isa para encontrar la primera ocurrencia de un elemento en una lista y devuelve su indice.
septima_lista = ("a", "b", "c", "d")

#Encontrar el indice del elemento "c"
indice=septima_lista.index("c")
print(indice)


#.count se usa para contar cuantas veces aparece un elemento especifico en una lista
octava_lista = (12, 32, 34, 76)
posicion= octava_lista.count(12)
print(posicion)

# Ordenar los elementos de una lista en su lugar con .sort

novena_lista = (3, 7, 45, 1, 5)
novena_lista.sort

print(novena_lista)

# Invertir el orden de los elementos de la lista con .reverse

decima_lista = [5, 6, 7, 8, 9]
decima_lista.reverse(decima_lista)

print(decima_lista)

#.Copy para cear una copia de una lista.

ultima_lista= ("caballo", "fogata", 'decente')
ultima_lista.copy

print(ultima_lista)



