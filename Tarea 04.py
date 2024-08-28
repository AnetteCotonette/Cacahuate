# Calificaciones:

calif_1 = 10
calif_2 = 7
calif_3 = 4

#promedio
valor1 = .50
valor2 = .35
valor3 = .50

promedio = (calif_1*valor1) + (calif_2*valor2) + (calif_3*valor3)
print(promedio)

#Matriz
matriz = [ [1, 1, 1, 3], [2, 2, 2, 7], [3, 3, 3, 9], [4, 4, 4, 13] ]

# Corregir la matriz

for fila in matriz:
    suma = sum(fila[:3]) #Sumar los pirmeros 3 valores de la fila
    if fila[3] != suma:
        fila[3] = suma
        print(fila)



