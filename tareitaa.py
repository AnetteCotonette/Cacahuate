import pandas as pd

# Solicitar el número de columnas
num_columns = int(input("Introduce el número de columnas del DataFrame: "))

# lista vacía para los datos
data = []

# Pedir los datos para cada columna
for i in range(num_columns):
    column_data = input(f"Introduce los datos de la columna {i + 1}, separados por comas: ").split(',')
    data.append(column_data)

# Pedir los nombres de las columnas
column_names = input(f"Introduce los nombres de las {num_columns} columnas, separados por comas: ").split(',')

# Pedir los nombres de las filas
num_rows = len(data[0])  # Suponemos que todas las columnas tendrán la misma longitud
row_names = input(f"Introduce los nombres de las {num_rows} filas, separados por comas: ").split(',')

# Crear el DataFrame
df = pd.DataFrame({column_names[i]: data[i] for i in range(num_columns)}, index=row_names)

# Mostrar el DataFrame
print("\nDataFrame generado:")
print(df)
