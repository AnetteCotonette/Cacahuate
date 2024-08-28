#Determinar si los tipos de dato "range" cumplen con las siguientes propiedaeds:

r = range(10)
# Intentar cambiar el valor del rango
try:
    r[0] = 5
except TypeError as e:
    print(f"Error: {e}")

# Intentar cambiar el rango en sí
try:
    r = range(5, 15)
    print(r)
except TypeError as e:
    print(f"Error: {e}")

# Conclusion, un dato tipo range es inmutable

# Determinar si un dato tipo range cumple con la suma

r1 = range(1, 15)
r2 = range(1, 10)

try:
    result = (r1 + r2)
print(result)

# Conclusion no se pueden sumar los rangos

# Definir si el dato range puede ser producto de  entero (multiplicacion

rango = range(2, 7)
r3 = range(3, 8)
multiplicacion = rango * r3
print(multiplicacion)

#Conclusion no se puede

#Definir si se puede hacer splicing

r_slice = r[1:5]
print(r_slice)
#Si se puede

#Conversion a lista y a tupla

r = range(1, 10)
list_r = list(r)
print(list_r)

# Funcion len

r = range(1, 10, 2)
length_r = len(r)
print(length_r)