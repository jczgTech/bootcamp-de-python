#El primer tipo de dato compuesto que veremos sera la lista

lista = ["Camilo Zuñiga", "tecnotutoriales Jheyson Galvis", True, 1.72]
print(lista)

#La tupla es una lista que no se puede modificar

tupla = ("Camilo Zuñiga", "tecnotutoriales Jheyson Galvis", True, 1.72)
print(tupla[1])


# Creando un conjunto o set
# Un conjunto no admite elementos duplicados

conjunto = {"Camilo Zuñiga", "Tecnotutoriales Jheyson Galvis", True, 1.72, 1.72}
print(conjunto)

# Creando un diccionario
diccionario = {
    "nombre": "Camilo",
    "apellido": "Zuñiga",
    "estatura": 1.72,
    "esta feliz": True
}

print(diccionario["esta feliz"])
print(diccionario["nombre"])
print(diccionario["apellido"])
print(diccionario["estatura"])