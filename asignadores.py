#Asignadores
#Operadores de asignacion, relacionales y logicos
#En programacion, una vairable esta fomado por un espacio en el sistema de almacenaje y un nombre simbolico
#que esta asociado a dicho espacio.

#este espacio contiene una cantidad de informacion conocida o desconocida, es decir, un valor.
#es diferente si se eligen numeros o palabras

variable1 = 5.2
variable2 = (2, 4, 6)

#operadores de asignacion
#los operadores de asignacion que se veran en el curso son:
# =, +=, *=, /=, //=, %=

print("La variable1", variable1)
variable1 += 3.2
print ("La variable1", variable1)

variable1 -= 17.2
print("La variable1", variable1)

#Ejemplo con **=
variable1 = 2
variable1 **= 3
print("La variable", variable1)

# Aplicando suma a cadenas

cad1 = "hola"
cad2 = "que hace"
print(cad1 + cad2)

#Operadores relacionales (siempre seran resultaod boleano)
#  <, >, ==, != (diferente)

# Operadores logicos
# or, and y not

#Segundo, las expresiones aritmeticas por sus propias reglas
# Tercero, las expresiones relacionales
# Cuarto, las expresiones logicas

#Controladores de flujo:
#Se trata de una estructura de control condiiconal. Los
#Nos permite evaluar si una o mas condiciones se cumplen para decir que accion vamos a ejecutar
#Esta evaluacion solo puede dar resultado boleano (V o F)

#If
#Permite dvidir el fujo de un programa en dos caminos
#se ejecuta siempre que la expresion que comprueba devuelva True

if True:
    print("caso positivo")

if "oracion":
    print("caso positivo")

# Ejemplo de if flase
condicional =  (5 - 16) and False
if condicional:
    print("La condicional es verdadera")
else:
    print("La condiiconal es falsa")

#si el cuarto numero no es igual a la suma de la fila, cambiar
#Si es igual, no hacer nada

#comando elif (si no se cumple condicional 1, analiza la siguiente)
condiiconal = 32
if condiiconal <10:
    print("condicional es chiquito")
elif condiiconal < 20:
    print ("condicional no es tan chiquito")
elif condicional <35:
    print ("condicional es grande")
else:
    print('no entro a ningun elif')

#Equivalencia con if else
condicional = 32
if condicional <10:
    print("condicional es chiquito")
else:
    if condicional <20:
        print("condicional es grande")
    else:
        print("no entró ningun elif")

# Comando pass (instruccion comodin! quita el error aunque esté ahí)
# Se le llama "herencia de clase" en donde un componente copia las propiedades
#de otro componente
if condicional != 0:
    pass

#Sentencia "for" (para) con listas
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for idx in numeros: #Para [variabel local] en [lista]
    print(idx) #cualquier palabra puede ser sistituida por "idx"
#Lo que tiene que imprimir es la lista de numeros en verical
