#Tipos de datos boleanos
#Representan uno de dos posibles valores: True o False

valor1 = True #TRUE
valor2 = False
print("tipos de valoes boleanos:", valor1, valor2)
print("usando type:", type(valor1), type(valor2))

print("usando and", valor1 and valor2)
print("usando or", valor1 or valor2)

#Conversiones a boleano
print("entero 0 a boleano", bool(0))
print("entero 1 a booleano", bool(1))

#Conversiones a boleano de stirngs
print("str a boleano", bool(""))
print("str a boleano", bool(""))
print("str boleno", bool("a"))

#Cadena nula: ""

print("lista vacion [] a boleano", bool([]))
print("tupla vacia () a boleano", bool(()))
print("diccionario vacio {} a boleano", bool({}))

#DICCIONARIO {}
#SOn usados para almacenar datos en formatos key: value

diccionario1 = dict()
print("ej de diccionario:", diccionario1, "su tipo es:", type(diccionario1))
diccioario1 = {"llave1": "lobo", "llave2": -82.654,34: "cosa", "llave4": [2,3,4]}



#Slicing  a diccionario
print(diccioario1["llave2"])
print(diccionario1["llave4"])
print(diccionario1[34])

#SETS
#Los conjutnos son una colecicon de valores no ordenados que no admiten duplicados enre {} y separaos por comas
set1 = {3, 6, "azul"}
print("ej de conjunto", set1, "de tipo:", type(set1))

set1 = {3, 8, 13, "jaja", "jeje", 3}

print("ej de conjunto:", set1)
