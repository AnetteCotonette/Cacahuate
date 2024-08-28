# Ejemplos de diccionarios
#Un diccionario es una estrucura de datos qu permite almacenar y organizar elementos
# en pares clave-valor.

mi_diccionario = {
    "animal": "Leon",
    "color": "naranja",
    "habitat": "selva"
}

# 1. pop()
color = mi_diccionario.pop("color")
print(f"pop: {color}")  # Imprime 25
print(f"Diccionario después de pop: {mi_diccionario}")

# 2. get()
habitat = mi_diccionario.get("habitat")
print(f"get: {habitat}")

# 3. copy()
copia_diccionario = mi_diccionario.copy()
print(f"copy: {copia_diccionario}")

# 4. keys()
claves = mi_diccionario.keys()
print(f"keys: {claves}")

# 5. items()
items = mi_diccionario.items()
print(f"items: {items}")  #

# 6. clear()
mi_diccionario.clear()
print(f"clear: {mi_diccionario}")

# Reiniciando el diccionario
mi_diccionario = {"animal": "Leon", "color": "naranja", "habitat": "selva"}

# 7. fromkeys()
nuevas_claves = ["a", "b", "c"]
nuevo_diccionario = dict.fromkeys(nuevas_claves, 0)
print(f"fromkeys: {nuevo_diccionario}")

# 8. popitem()
ultima_clave, ultimo_valor = mi_diccionario.popitem()
print(f"popitem: Clave - {ultima_clave}, Valor - {ultimo_valor}")
print(f"Diccionario después de popitem: {mi_diccionario}")

# 9. setdefault()
habitat = mi_diccionario.setdefault("habitat", "selva")
print(f"setdefault: {habitat}")
print(f"Diccionario después de setdefault: {mi_diccionario}")

# 10. update()
mi_diccionario.update({"color": "a veces cafe", "habitat": "a veces jungla"})
print(f"update: {mi_diccionario}")

# 11. values()
valores = mi_diccionario.values()
print(f"values: {valores}")